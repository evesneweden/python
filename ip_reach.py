import sys
import subprocess

#Checking IP reachability
def ip_reach(list):

  for ip in list:
    ip = ip.rstrip("\n") #strip the newlines from the IPs in the list argument we supply
    #Call the subprocess module method and give it the ping string that you substitue with the ip. Send stdout and stderr to devnull so it keeps screen clean
    ping_reply = subprocess.call('ping %s /n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if ping_reply == 0:
        print("\n* {} is reachable :)\n".format(ip))
        continue #If ping reply gives the echo reply then continue the loop instead of ending

    else:
        print('\n* {} not reachable. Check connectivty and try again.'.format(ip))
        sys.exit()
