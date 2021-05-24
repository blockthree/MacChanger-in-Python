import subprocess
import optparse


def machanger():
    parser = optparse.OptionParser()


    parser.add_option("-i","--interface",dest="interface",help="used to select interface")
    parser.add_option("-m","--mac",dest="new_mac",help="change mac address")

    return parser.parse_args()

def mac(interface,new_maca):
    print("changing mac address for "+interface+" mac address is "+new_maca)

    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_maca])
    subprocess.call(["ifconfig",interface,"up"])  

(options,arguments)=machanger()
mac(options.interface,options.new_mac)  
