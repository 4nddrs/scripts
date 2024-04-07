import sys
import subprocess
from colorama import Fore, Style
import os

def run_netsh_command(arguments):
    # Execute the netsh command with the provided arguments
    try:
        subprocess.call(["netsh"] + arguments, stdout=open(os.devnull, 'wb'), stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print("Error executing netsh command:", e)
        sys.exit(1)

def turn_on_firewall():
    # Execute the netsh advfirewall command to turn on the firewall
    print(Fore.LIGHTBLUE_EX + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(Fore.GREEN+"Turning on the firewall...")
    run_netsh_command(["advfirewall", "set", "allprofiles", "state", "on"])
    print(Fore.LIGHTBLUE_EX + "--------------------------------")
    print(Fore.GREEN+"Firewall turned on successfully.")
    print(Fore.LIGHTBLUE_EX + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

def turn_off_firewall():
    # Execute the netsh advfirewall command to turn off the firewall
    print(Fore.YELLOW + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(Fore.RED+"Turning off the firewall...")
    run_netsh_command(["advfirewall", "set", "allprofiles", "state", "off"])
    run_netsh_command(["advfirewall", "set", "allprofiles", "firewallpolicy", "blockinbound,allowoutbound"])
    print(Fore.YELLOW + "--------------------------------")
    print(Fore.RED+"Firewall turned off successfully. Be Careful!")
    print(Fore.YELLOW + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "--------------------------------")
        print(Fore.RED + "Usage: python script.py [on|off]")
        print(Fore.RED + "--------------------------------")
        sys.exit(1)
    
    option = sys.argv[1].lower()
    if option == "on":
        turn_on_firewall()
    elif option == "off":
        turn_off_firewall()
    else:
        print( Fore.RED + "--------------------------------------------")
        print( Fore.RED + "Invalid option. Please select 'on' or 'off'.")
        print( Fore.RED + "--------------------------------------------")
        sys.exit(1)

if __name__ == "__main__":
    main()
