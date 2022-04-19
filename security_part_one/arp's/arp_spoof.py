#! /usr/bin/env python3

import scapy.all as scapy
import time
import sys

def get_mac(ip):
	arp.request = scopy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scarp.srp(arp_request_broadcast, timeout=1, verbase=False)[0]
	return answered_list[0][1]
