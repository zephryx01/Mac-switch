#!/usr/bin/env python3

import argparse
import random
import re
import shutil
import subprocess
import sys

MAC_RE = re.compile(r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$")


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
    print_red("                                               by zephryx")


def require_ifconfig():
    if shutil.which("ifconfig") is None:
        print_red("ifconfig not found. Install net-tools (e.g. `apt install net-tools`) and retry.")
        sys.exit(1)


def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(
            ["ifconfig", interface], stderr=subprocess.STDOUT
        ).decode("utf-8")
    except subprocess.CalledProcessError:
        print_red(f"Interface '{interface}' not found.")
        sys.exit(1)
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
    if not mac_address_search_result:
        print_red("Could not read MAC address.")
        sys.exit(1)
    return mac_address_search_result.group(0)

def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

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

    require_ifconfig()

    if args.mac and not MAC_RE.match(args.mac):
        print_red(f"'{args.mac}' is not a valid MAC address (expected format xx:xx:xx:xx:xx:xx).")
        sys.exit(1)

    current_mac = get_current_mac(args.interface)
    print(f"Current MAC address for {args.interface}: {current_mac}")

    new_mac = args.mac if args.mac else generate_random_mac()
    if not args.mac:
        print(f"Changing MAC address randomly to: {new_mac}")

    change_mac(args.interface, new_mac)

    resulting_mac = get_current_mac(args.interface)
    if resulting_mac.lower() == new_mac.lower():
        print(f"MAC address successfully changed to: {resulting_mac}")
    else:
        print_red(f"Failed to change MAC address. Interface still reports: {resulting_mac}")
        sys.exit(1)

if __name__ == "__main__":
    main()
