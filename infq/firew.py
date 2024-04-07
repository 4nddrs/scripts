import sys
import subprocess

def run_netsh_command(arguments):
    # Execute the netsh command with the provided arguments
    try:
        subprocess.call(["netsh"] + arguments)
    except subprocess.CalledProcessError as e:
        print("Error executing netsh command:", e)
        sys.exit(1)

def turn_on_firewall():
    # Execute the netsh advfirewall command to turn on the firewall
    print("Turning on the firewall...")
    run_netsh_command(["advfirewall", "set", "allprofiles", "state", "on"])
    print("Firewall turned on successfully.")

def turn_off_firewall():
    # Execute the netsh advfirewall command to turn off the firewall
    print("Turning off the firewall...")
    run_netsh_command(["advfirewall", "set", "allprofiles", "state", "off"])
    run_netsh_command(["advfirewall", "set", "allprofiles", "firewallpolicy", "blockinbound,allowoutbound"])
    print("Firewall turned off successfully.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py [on|off]")
        sys.exit(1)
    
    option = sys.argv[1].lower()
    if option == "on":
        turn_on_firewall()
    elif option == "off":
        turn_off_firewall()
    else:
        print("Invalid option. Please select 'on' or 'off'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
