#!/bin/bash

echo -n "Enter Interface: "
read iface
echo -n "Enter file name: "
read filename

tcpdump -i $iface -w ${filename}.pcap
