#!/usr/bin/env python

from NetworkCat import Netcat

ip = raw_input("IP Address")
port = raw_input("port number")

nc = Netcat(ip, (int(port)))