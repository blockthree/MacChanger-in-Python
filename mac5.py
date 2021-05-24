import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i","--interface",dest="interface",help="used to select interface")
parser.add_option("-m","--mac",dest="new_mac",help="change mac address")


(options,arguments) = parser.parse_args()

def macchanger(interface,new_mac):
    print("changing mac address for "+interface+" mac address is "+new_mac)
  
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])


macchanger(options.interface,options.new_mac)



