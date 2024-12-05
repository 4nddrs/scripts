#!/usr/bin/env python3

import ipaddress
import sys
from colorama import Fore, Style


def to_binary_string(ip):
    return ".".join([f"{int(octet):08b}" for octet in str(ip).split(".")])

def calculate_network_info(cidr):
    network = ipaddress.IPv4Network(cidr, strict=False)
    return {
        "address": str(network.network_address),
        "address_bin": to_binary_string(network.network_address),
        "netmask": str(network.netmask),
        "netmask_bits": network.prefixlen,
        "netmask_bin": to_binary_string(network.netmask),
        "wildcard": str(ipaddress.IPv4Address(int(network.hostmask))),
        "wildcard_bin": to_binary_string(network.hostmask),
        "network": str(network.network_address) + f"/{network.prefixlen}",
        "network_bin": to_binary_string(network.network_address),
        "host_min": str(network.network_address + 1),
        "host_min_bin": to_binary_string(network.network_address + 1),
        "host_max": str(network.broadcast_address - 1),
        "host_max_bin": to_binary_string(network.broadcast_address - 1),
        "broadcast": str(network.broadcast_address),
        "broadcast_bin": to_binary_string(network.broadcast_address),
        "hosts_count": network.num_addresses - 2,
        "class_type": "Class C" if network.network_address < ipaddress.IPv4Address('224.0.0.0') else "Class D or E",
        "private": network.is_private
    }

def validate_input(cidr):
    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
        return network
    except ValueError:
        print("Entrada no válida. Por favor, ingrese una dirección IP válida en formato CIDR (ej. 192.168.14.12/24).")
        return None

def main(cidr):
    network = validate_input(cidr)
    if network:
        info = calculate_network_info(cidr)
        private_str = "Private Internet" if info["private"] else "Public Internet"
        print(Fore.YELLOW +  f"Address:" + Fore.WHITE+  f"   {info['address']:<15}  " +Fore.LIGHTRED_EX + f"    {info['address_bin']}")

        print(Fore.YELLOW + f"Netmask:" +Fore.WHITE+  f"   {info['netmask']} = {info['netmask_bits']}" +Fore.LIGHTMAGENTA_EX + f"   {info['netmask_bin']}")

        print(Fore.YELLOW + f"Wildcard:" +Fore.WHITE+ f"  {info['wildcard']:<15}" +Fore.LIGHTRED_EX + f"      {info['wildcard_bin']}")

        print(Fore.LIGHTRED_EX +"=>")
        print(Fore.YELLOW + f"Network:" +Fore.WHITE+  f"   {info['network']:<15}" +Fore.LIGHTMAGENTA_EX + f"      {info['network_bin']}")

        print(Fore.YELLOW + f"HostMin:" +Fore.WHITE+  f"   {info['host_min']:<15}" +Fore.LIGHTRED_EX + f"      {info['host_min_bin']}")

        print(Fore.YELLOW + f"HostMax:" +Fore.WHITE+  f"   {info['host_max']:<15}" +Fore.LIGHTMAGENTA_EX + f"      {info['host_max_bin']}")

        print(Fore.YELLOW + f"Broadcast:" +Fore.WHITE+  f" {info['broadcast']:<15}" +Fore.LIGHTRED_EX + f"      {info['broadcast_bin']}")
        
        print(Fore.YELLOW + f"Hosts/Net:" +Fore.WHITE+  f" {info['hosts_count']}"+Fore.LIGHTMAGENTA_EX +f"                  {info['class_type']}, {private_str}")
    else:
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: ipcalc.py <dirección IP/CIDR>")
        sys.exit(1)

    cidr = sys.argv[1]
    main(cidr)
