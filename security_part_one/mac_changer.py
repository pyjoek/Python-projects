import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="interface to work with")
parser.add_option("-m","--mac_add",dest="mac_address",help="change mac address")
parser.add_option("-p","--ip",dest="ip_address",help="change ip address")
(options, arguments) = parser.parse_args()

interface = options.interface
mac = options.mac_address
ip = options.ip_address

# change mac address using ifconfig
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac])
subprocess.call(["ifconfig",interface,"up"])

# change ip address using ifconfig
# subprocess.call(["ifconfig",interface,"inet",ip])
# subprocess.call(["ifconfig"])

# change mac address using ip link
# subprocess.call(["ip","link","set","dev",interface,"down"])
# subprocess.call(["ip","link","set","dev",interface,"address",mac])
# subprocess.call(["ip","link","set","dev",interface,"up"])

# change ip address using ip link
# subprocess.call(["ip","a","add","new ip/24","dev","eth0"])
# subprocess.call(["ip","link","show"])
