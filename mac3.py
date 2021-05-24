import subprocess

interface = input("enter your interface")
new_mac = input("enter your mac address")

print("changing mac address for "+interface+" mac address is "+new_mac)

subprocess.call(["ifconfig", interface ,"down"])
subprocess.call(["ifconfig", interface ,"hw","ether",new_mac])
subprocess.call(["ifconfig", interface ,"up"])