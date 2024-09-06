#!/usr/bin/env python3

import subprocess
import argparse
import re
import random

def print_red(text):
    RED = '\033[31m'
    RESET = '\033[0m'
    print(RED + text + RESET)

def banner():
    banner = """

███╗░░░███╗░█████╗░░█████╗░░██████╗░██╗░░░░░░░██╗██╗████████╗░█████╗░██╗░░██╗
████╗░████║██╔══██╗██╔══██╗██╔════╝░██║░░██╗░░██║██║╚══██╔══╝██╔══██╗██║░░██║
██╔████╔██║███████║██║░░╚═╝╚█████╗░░╚██╗████╗██╔╝██║░░░██║░░░██║░░╚═╝███████║
██║╚██╔╝██║██╔══██║██║░░██╗░╚═══██╗░░████╔═████║░██║░░░██║░░░██║░░██╗██╔══██║
██║░╚═╝░██║██║░░██║╚█████╔╝██████╔╝░░╚██╔╝░╚██╔╝░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    """
    print(banner)
    print_red("                                               by zephryx01")

def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print_red("Could not read MAC address.")

def generate_random_mac():
    random_mac = [0x00, 0x16, 0x3e,
                  random.randint(0x00, 0x7f),
                  random.randint(0x00, 0xff),
                  random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, random_mac))

def main():
    parser = argparse.ArgumentParser(description="MACSwitch - A tool for changing MAC addresses on Linux systems")
    parser.add_argument("-i", "--interface", help="Interface to change MAC address (e.g., eth0)", required=True)
    parser.add_argument("-m", "--mac", help="New MAC address to assign")
    args = parser.parse_args()

    banner()
    print("")

    current_mac = get_current_mac(args.interface)
    print(f"Current MAC address for {args.interface}: {current_mac}")

    if args.mac:
        new_mac = args.mac
    else:
        new_mac = generate_random_mac()
        print(f"Changing MAC address randomly to: {new_mac}")

    change_mac(args.interface, new_mac)
    if new_mac:
        print(f"MAC address successfully changed to: {new_mac}")
    else:
        print_red("Failed to change MAC address.")

if __name__ == "__main__":
    main()
