#!/usr/bin/env python

from libnmap.process import NmapProcess

net = raw_input("Enter Net with CIDR")

nm = NmapProcess(net, options="-sV")
rc = nm.run()

if nm.rc==0:
    print nm.stdout
else:
    print nm.stderr
