import random
import sys
import ipaddress

#Checking IP address validity
while True:
    ip = input("Enter an IP Address: ")

    #Check the octets
    #valid_address = ipaddress.ip_address(ip)
    try:
        valid_address = ipaddress.ip_address(ip)
        print(valid_address)

    except:
        print("This {} was not valid".format(valid_address))
    #else:
    #    print("\nThe IP address is INVALID! Please retry!\n")
    #    sys.exit()
