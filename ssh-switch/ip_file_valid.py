import os.path 
import sys

#Chek the IP address file and content validity
def ip_file_valid():

    #Prompt user for file name containg the ips
    ip_file = input("\n# Enter IP file path and name (e.g D:\MyApps\myfile.txt): ")

    #Checking if the file exists
    if os.path.isfile(ip_file) == True: #isfile checks that the file exists
        print("\n* IP file is valid :)\n") #if file exists do this

    else:
        print("\n* File {} does not exist. Please check and try again.\n".format(ip_file))
        sys.exit()
	#Whatever filename you passed to the ip_file variable gets substituted in the using the format function

    #OPen user selected file for reading
    selected_ip_file = open(ip_file, 'r')

    #Start from beginning of the file with seek
    selected_ip_file.seek(0)

    #Read each line in the file
    ip_list = selected_ip_file.readlines()

    #Close the file once done
    selected_ip_file.close()

    return ip_list #return this value from the function
