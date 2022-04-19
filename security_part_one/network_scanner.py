import optparse
import scapy.all as scapy

parser = optparse.OptionParser()

parser.add_option("--ip",dest="ip",help="put you ip address")

(options, arguments) = parser.parse_args()

ip = options.ip

def scan(ip):
	scapy.arping(ip)
	
scan(ip)
