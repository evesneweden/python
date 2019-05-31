import random #generates pseudo random numbers.
import sys
import ipaddress
import numpy

while True:
    ip_address = input("Enter an IP address: ")
    valid_address = ipaddress.ip_interface(ip_address)
    loopback = valid_address.ip.is_loopback
    private = valid_address.network.is_private
    multi_cast = valid_address.ip.is_multicast
    if loopback: print('\n* The address you provided: {} is the loopback!. Try again'.format(valid_address))
    elif private: print('\n* The address you provided: {} is a private IP. Try again'.format(valid_address))
    elif multi_cast: print('\n* The address you provided: {} is a multicast address! Try again'.format(valid_address))
    else: print('\n* Here is the IP address you gave: {}. Lets convert to binary!\n'.format(valid_address)); break
    mask_octets_binary = []
    binary_octet = bin(int(valid_address)).lstrip('0b')
    mask_octets_binary.append(binary_octet.zfill(8))
    print("The IP Address you gave in Binary is {}\n".format(mask_octets_binary))


###TEST CODE
while True:
    ip_address = input("Enter an IP address: ")
    valid_address = ipaddress.ip_interface(ip_address)
    split_ip = ip_address.split(".")
    mask_octets_binary = []
    binary_octet = bin(int(split_ip[0])).lstrip('0b')
    mask_octets_binary.append(binary_octet.zfill(8))
    print(mask_octets_binary)
    loopback = valid_address.ip.is_loopback
    private = valid_address.network.is_private
    multi_cast = valid_address.ip.is_multicast
    if loopback: print('\n* The address you provided: {} is the loopback!. Try again'.format(valid_address))
    elif private: print('\n* The address you provided: {} is a private IP. Try again'.format(valid_address))
    elif multi_cast: print('\n* The address you provided: {} is a multicast address! Try again'.format(valid_address))
    else: print('\n* Here is the IP address you gave: {}. Lets convert to binary!\n'.format(valid_address)); break

    print(numpy.count_nonzero(mask_octets_binary))
    print("The IP Address you gave in Binary is {}\n".format(mask_octets_binary))
