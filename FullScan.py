#!/us/bin/env python


import os
import subprocess
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException

iprange = [x for x in range(1,254)]

#fill iprange list with 1-254


def scan_sweep(netRange):
    ipUprange = []
    devnulls=open(os.devnull, 'w')
    for i in netRange:
        response = subprocess.call(["ping -c 1 10.0.0." + str(i)], stdout=devnulls, stderr=devnulls, shell=True)
        if response == 0:
            print "10.0.0." + str(i) + " is up"
            ipUprange.append("10.0.0." + str(i))
        else:
            print "10.0.0." + str(i) + " is down"
    return ipUprange




def do_scan(netRange):
    parsed=None
    for i in netRange:
        scanner = NmapProcess(i, options="-sV --top-ports 100")
        rc = scanner.run()

        if scanner.rc == 0:
            parsed = NmapParser.parse(scanner.stdout)
            for host in parsed.hosts:
                if len(host.hostnames):
                    tmp_host=host.hostnames.pop()
                else:
                    tmp_host=host.address

                print("Nmap Scan Report for {0} ({1})".format(tmp_host,host.address))
                print("Host is {0}".format(host.status))
                print("  PORT     STATE         SERVICE")
                for serv in host.services:
                    pserv="{0:>5s}/1{1:3s}  {2:12s}  {3}".format(str(serv.port), serv.protocol, serv.service)
                    if len(serv.banner):
                        pserv+=" ({0})".format(serv.banner)
                print pserv
        else:
            print scanner.stderr

'''
def print_scan(nmap_report):
    print("Starting Nmap {0} at {1}".format(nmap_report.version, nmap_report.started))

    for host in nmap_report.hosts:
        if len(host.hostnames):
            tmp_host=host.hostnames.pop()
        else:
            tmp_host=host.address

        print("Nmap scan report for {0} ({1})".format(tmp_host, host.address))
        print("Host is {0}.".format(host.status))
        print("  PORT     STATE         SERVICE")

        for serv in host.services:
            pserv="{0:>5s}/{1:3s}  {2:12s}  {3}".format(str(serv.port), serv.protocol, serv.service)
            if len(serv.banner):
                pserv+=" ({0})".format(serv.banner)
            print(pserv)
    print(nmap_report.summary)
'''

#report = do_scan(scan_sweep(iprange))
#if report:
#    print print_scan(report)
#else:
#    print("No results returned")
do_scan(scan_sweep(iprange))
