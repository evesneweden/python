import sys
import ipaddress

#Check the octets of the IP
def ip_addr_valid(list):

    for ip in list:
      ip = ip.rstrip("\n") #strip the new line character from the list
      #print(ip)
      #octet_list = ip.split(".") #strip the IP by the delimited "."
      #address = ipaddress.ip_address(ip)
      address = ipaddress.ip_address(ip)

      if address.is_reserved == False or address.is_loopback == False or address.is_unspecified == False or address.is_mulitcast == False:
          continue
      #if (len(octet_list) == 4) and (1 <= int(octet_list[0])  <= 223) and (int(octet_list[0]) !=127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
     #  continue
      else:
        print('\n* There was an invalid IP address in the file: {} :(\n'.format(list))
        sys.exit()
