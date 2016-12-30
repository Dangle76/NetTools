#!/bin/bash

subnetMask=$(ifconfig -a eth0 | grep inet | grep -v inet6 | awk  '{print $4}');
bCast=$(ifconfig -a eth0 | grep inet | grep -v inet6 | awk  '{print $6}');

#echo $subnetMask;
#echo $bCast;



#Import Gateway and subnet, run NMAP on the entire network

networkFinal=$(python get_Gateway.py "$bCast" "$subnetMask"); #invoke python script to attain network and CIDR subnet into variable
echo $networkFinal #Print Result
nmap -v -F $networkFinal | grep -v down #Run NMAP against result
