#!/usr/bin/python

from netaddr import *
import pprint
import sys

broadcast_Import = sys.argv[1]
netmask_Import = sys.argv[2]

broadcast = IPAddress(broadcast_Import)
netmask = IPAddress(netmask_Import)



ipnet = IPNetwork(str(broadcast) + '/' + str(netmask))
ipnet = IPNetwork (str(ipnet.network) + '/' + str(netmask))
print ipnet
