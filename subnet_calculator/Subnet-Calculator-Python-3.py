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
    no_subnet = ip_address.split("/")
    split_ip = no_subnet[0]
    octet_array = split_ip.split(".")
    print(octet_array)
    print(valid_address)
    no_cidr_ip = no_subnet[0]
    print(no_subnet)
    print(no_cidr_ip)
    mask_octets_binary = []
    for octet in no_subnet:
        mask_octets_binary.append(bin(int(octet)).lstrip('0b').zfill(8))
    binary_mask = "".join(mask_octets_binary)
    no_of_zeros = binary_mask.count("0")
    no_of_ones = 32 - no_of_zeros
    no_of_hosts = abs(2 ** no_of_ones - 2)
    print(no_of_hosts)
    print(binary_mask)
    print(no_of_zeros)

    print("The IP Address you gave in Binary is {}\n".format(mask_octets_binary))
    print(numpy.count_nonzero(mask_octets_binary))
    loopback = valid_address.ip.is_loopback
    private = valid_address.network.is_private
    multi_cast = valid_address.ip.is_multicast
    if loopback: print('\n* The address you provided: {} is the loopback!. Try again'.format(valid_address))
    elif private: print('\n* The address you provided: {} is a private IP. Try again'.format(valid_address))
    elif multi_cast: print('\n* The address you provided: {} is a multicast address! Try again'.format(valid_address))
    else: print('\n* Here is the IP address you gave: {}. Lets convert to binary!\n'.format(valid_address)); break

    print(numpy.count_nonzero(mask_octets_binary))
    print("The IP Address you gave in Binary is {}\n".format(mask_octets_binary))
