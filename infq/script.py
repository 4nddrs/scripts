# -*- coding: utf-8 -*-

import sys
import re
import requests
from colorama import Fore, Style
import sys

def validar_ip(ip):
    # Validar que la dirección IP tenga el formato correcto y que cada octeto esté en el rango de 0 a 255
    patron_ip = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(patron_ip, ip):
        return True
    else:
        return False

def obtener_clase_ip(ip):
    primer_octeto = int(ip.split('.')[0])

    if 1 <= primer_octeto <= 126:
        return 'A'
    elif 128 <= primer_octeto <= 191:
        return 'B'
    elif 192 <= primer_octeto <= 223:
        return 'C'
    elif 224 <= primer_octeto <= 239:
        return 'D'
    elif 240 <= primer_octeto <= 255:
        return 'E'
    else:
        return None
    
def es_privada(ip):
    primer_octeto = int(ip.split('.')[0])
    if primer_octeto == 10:
        return True
    elif primer_octeto == 172 and 16 <= int(ip.split('.')[1]) <= 31:
        return True
    elif primer_octeto == 192 and int(ip.split('.')[1]) == 168:
        return True
    else:
        return False

def ip_a_binario(ip):
    octetos = ip.split('.')
    binario = []
    for octeto in octetos:
        binario.append(format(int(octeto), '08b'))  # Convertir cada octeto a binario y añadirlo a la lista
    return '.'.join(binario)  # Unir los octetos binarios con puntos para obtener la IP en binario

def obtener_detalles_ip(ip):
    try:
        respuesta = requests.get("http://ipinfo.io/{}/json".format(ip))
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos
        else:
            return None
    except Exception as e:
        print(Fore.RED + "Error when taking IP Address Details", e)
        return None

def IPoptions(ip):
    print(Fore.GREEN + "-------------------------------------------------------------")
    # Validar la dirección IP
    if validar_ip(ip):
        clase_ip = obtener_clase_ip(ip)
        if clase_ip:
            print(Fore.GREEN + "IP Class: {}".format(clase_ip) + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Invalid IP Address" + Style.RESET_ALL)
            return
    else:
        print(Fore.RED + "Invalid IP Address" + Style.RESET_ALL)
        return
    print("-------------------------------------------------------------")
        # Determinar si la dirección IP es privada o pública
    if es_privada(ip):
        print(Fore.YELLOW + "IP Type: Private" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "IP Type: Public" + Style.RESET_ALL)
    print("-------------------------------------------------------------")
    # Obtener detalles de la dirección IP        
    detalles_ip = obtener_detalles_ip(ip)
    if detalles_ip:
        print(Fore.MAGENTA + "Details:")
        print("        Geolocation: {}, {}, {}".format(detalles_ip.get('city', 'N/A'), detalles_ip.get('region', 'N/A'), detalles_ip.get('country', 'N/A')))
        print("        ISP: {}".format(detalles_ip.get('org', 'N/A')))
        
    else:
        print(Fore.BLUE + "IP Address Details:")
        print("    Geolocation: N/A")
        print("    ISP: N/A")
        print(Style.RESET_ALL)
    print("-------------------------------------------------------------")
    # Convertir la dirección IP a binario
    ip_binario = ip_a_binario(ip)
    print(Fore.BLUE + "IP Address Binary: {}".format(ip_binario) + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+ "-------------------------------------------------------------")

def validar_direccion_mac(mac):
    # Expresión regular para verificar el formato de la dirección MAC
    patron_mac = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'

    # Comprobar si la dirección MAC coincide con el patrón
    if re.match(patron_mac, mac):
        return True
    else:
        return False

def obtener_fabricante_direccion_mac(mac):
    # Extraer los primeros 3 bytes (OUI) de la dirección MAC
    oui = mac[:8].upper()

    # Consultar la API para obtener el fabricante asociado al OUI
    url = "https://api.macvendors.com/{}".format(oui)
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.text.strip()
        else:
            return "No disponible"
    except Exception as e:
        print("Error al obtener fabricante de dirección MAC:", e)
        return "Error"

    
def mac_options(mac): 
    # Validar la dirección MAC
    if validar_direccion_mac(mac):
        print(Fore.GREEN + "-------------------------------------------------------------")
        print(Fore.GREEN + "Valid MAC Address" + Style.RESET_ALL)
        print(Fore.MAGENTA + "-------------------------------------------------------------")
        print(Fore.MAGENTA + "MAKER: {}".format(obtener_fabricante_direccion_mac(mac)))
        print(Fore.MAGENTA + "-------------------------------------------------------------")
    else:
        print(Fore.RED + "-------------------------------------------------------------")
        print(Fore.RED + "Invalid MAC Address" + Style.RESET_ALL)
        print(Fore.RED + "-------------------------------------------------------------")
        return





    
def main():

    if len(sys.argv) == 3:
        if sys.argv[1] == 'ip':
            ip = sys.argv[2]
            IPoptions(ip)
        elif sys.argv[1] == 'mac':
            mac = sys.argv[2]
            mac_options(mac)
        else:
            print(Fore.RED + "Invalid argument. Please specify either 'ip' or 'mac' as the first argument.")
            sys.exit(0)
    else:
        print(Fore.RED + "Invalid number of arguments. Usage: python script.py ip <IP_address> or python script.py mac <MAC_address>")

if __name__ == "__main__":
    main()
