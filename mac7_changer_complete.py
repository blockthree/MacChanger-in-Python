import subprocess 
import optparse
import re

def getoptions():
    parser = optparse.OptionParser()
    parser.add_option("--i","--interface",dest="inf",help="interface")
    parser.add_option("--m","--mac",dest="mac",help="mac")
    (options,arguments)=parser.parse_args()
    if not options.inf:
        parser.error("interface not defined")
    elif not options.mac:
        parser.error("mac not specfied")    
    else:
        return options

def mac_changer(inf,mac):
    print("current interface"+inf+"mac is"+mac)    
    subprocess.call(["ifconfig",inf,"down"])  
    subprocess.call(["ifconfig",inf,"hw","ether",mac]) 
    subprocess.call(["ifconfig",inf,"up"])  

def mac_cg(inf):
    interfaceread = subprocess.check_output(["ifconfig",options.inf])
    #print(interfaceread)

    fi = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",interfaceread)
    if fi:
        return fi.group(0)
        #print("ip address found")
    else:
        print("mac address not found") 



options = getoptions()

macdrress = mac_cg(options.inf)
print("current mac address"+str(macdrress))

mac_changer(options.inf,options.mac)
macdrress = mac_cg(options.inf)
if macdrress==options.mac:
    print("new mac address"+macdrress)
else:
    print("not changed")    

  

 





