#!/us/bin/env python


import os

iprange = [x for x in range(1,254)]

#fill iprange list with 1-254



for i in iprange:
    response = os.system("ping -c 1 10.0.0." + str(i)) 
    if response == 0:
        print "10.0.0." + str(i) + " is up"
    else:
        print "10.0.0." + str(i) + " is down"


