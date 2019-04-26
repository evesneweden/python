import random #generates pseudo random numbers.
import sys
import ipaddress


#Checking IP address validity
while True:
    ip_address = input("Enter an IP address: ")

    #Lets split the IP address up by a period for now so we can check each number in the octect individually
    ip_octects = ip_address.split('.')
    #This will fail because we are splitting the IP and the ip address is checking for validity of the IP!
    valid_address = ipaddress.ip_interface(ip_octects)
    #binary version of the ip ip_address
    ipv4_address = ipaddress_IPv4Address(valid_address)
    binary_address = ipv4_address.packed
    # Check if the address entered is reserved, loopback, or is a multicast address. If they arent, break out of loop.
    if valid_address.network.is_reserved == False or valid_address.ip.is_loopback == False or valid_address.ip.is_multicast == False:
        break
    else:
        print('\n* You did not give a proper IP address: {}. Please check and try again.\n'.format(valid_address))
        continue

    binary_address = ipaddress_IPv4Address(valid_address)
