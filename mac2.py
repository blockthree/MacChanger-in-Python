import subprocess

subprocess.call("ifconfig eth0 down",shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:54:23:12:43",shell=True)
subprocess.call("ifconfig eth0 up",shell=True)