# MACSwitch
```MACSwitch``` is a versatile tool designed for changing the MAC (Media Access Control) address of network interfaces on Linux systems. Whether you're concerned about privacy, bypassing MAC address filtering, or performing network experiments, ```MACSwitch``` provides a convenient way to modify your network interface's MAC address.


![Example](https://github.com/m1dn1ghtMHR/Mac-switch/blob/main/usage.png)


## Features
- **MAC Address Randomization:** MACSwitch allows you to generate and assign random MAC addresses to your network interfaces for enhanced privacy and anonymity.
- **Custom MAC Address:** Users can specify a custom MAC address to set on their network interface, providing flexibility in MAC address configuration.
- **Interface Detection:** MACSwitch automatically detects available network interfaces on the system, simplifying the process of selecting the interface to modify.
- **Undo Changes:** MACSwitch includes an option to revert to the original MAC address, restoring the network interface to its default configuration.
- **Cross-Platform Compatibility:** MACSwitch is compatible with Linux distributions, providing a consistent experience across different environments.
## Usage
To start using ```MACSwitch```, simply specify the network interface using ```-i``` or ```--interface``` and the desired MAC address using ```-m``` or ```--mac```.

## Example usage:
```
python3 macswitch.py -i <interface> -m 00:11:22:33:44:55
```
## Installation

> Clone the MACSwitch repository from GitHub:
```
git clone https://github.com/m1dn1ghtMHR/Mac-switch.git
```
> Navigate to the MACSwitch directory:
```
cd Mac-switch
```
> Ensure you have Python 3 installed on your system.

> Run MACSwitch using Python:
```
python3 macswitch.py -i <interface> -m 00:11:22:33:44:55
```
> To revert back to your original MAC address
```
python3 macswitch.py -i <interface> -m <original_mac_address>
```
### Contributing
Contributions to MACSwitch are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

# Disclaimer
MACSwitch is intended for educational and legal purposes only. Unauthorized use of this tool against networks or devices without proper authorization may violate local laws and regulations.

