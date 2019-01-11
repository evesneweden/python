import paramiko
import os.path
import time
import sys
import re


#Checking username/passord file
user_file = input("\n# Enter user file path and name: ")

#Verify validity of password file
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")

else:
    print("\n* File {} does not exist. Please check and try again. \n".format(user_file))
    sys.exit()


#Checking Commands files
cmd_file = input("\n# Enter commands file path and name: ")

#Verifying the validity of the commands file
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid . Sending command(s) to device(s)...\n")

else:
    print("\n* File {} does not exist. Please check and try again.\n".format(cmd_file))
    sys.exit()

#Open SSH connection to the device
def ssh_connection(ip):

    global user_file #make the variables defined outside of the function globally accessible to the function
    global cmd_file

    try: #This means to test the code that follows below, if it fails, then raise exceptions
        #Define the SSH paramters
        selected_user_file = open(user_file, 'r')

        #Start from begining of file with seek
        selected_user_file.seek(0)

        #Read the username from the file given in the user_file global variable
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        #Start from beginning of line looking for the password
        selected_user_file.seek(0)

        #Read from files
        password = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        #Logging into the device
        session = paramiko.SSHClient() #make an object for the SSHClient function from paramiko

        #Allow auto accepting of unkown host keys. We suggest not doing this in prod
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect using username and password
        session.connect(ip.rstrip("\n"), username = username, password = password)

        #Start interactive shell session on the device
        connection = session.invoke_shell()

        #Set terminal length for output and disable pagination
        connection.send("enable\n") #send text to the terminal
        connection.send("terminal length 0\n")

        #Enter global conf mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        #Open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')

        #start from begining of line
        selected_cmd_file.seek(0)

        #Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        #close the files
        selected_user_file.close()
        selected_cmd_file.close()

        #Checking command output for IOS syntax errors
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {}".format(ip))

        else:
            print("\nDone for device {}\n".format(ip))

        #Test for reading command output
        print(str(router_output) + "\n")

        #Close session
        session.close()

    except paramiko.AuthenticationException:
        print("* Invalid username or password\n* Please check the username/password file or the device configuration.")
        print("*Closing program... Bye!")
