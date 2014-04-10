#!/usr/bin/env python
#
#       This script automates whois queries. Feed the script a file with IP Addresses, one per line,
#       that you wish to query and whocheck.py will return the culstomer and organization names.
#        
#       Author: Joseph Key
#       Contact: bloodwolf2685@gmail.com
#       

import re, os, subprocess
import os
from prettytable import PrettyTable
from sys import argv

script, ip_add = argv

ip_file = open(ip_add)
ip_file1 = ip_file.read().split('\n')

z = PrettyTable(['IP Address', 'Organization'])
z.padding_width = 1

for line in ip_file1:
        proc = subprocess.Popen(["whois %r" % line], stdout=subprocess.PIPE, shell=True)
        (whois, err) = proc.communicate()

        Org_pattern = 'OrgName:.*'
        find_org = re.findall(Org_pattern, whois)

        proc = subprocess.Popen(["whois %r" % line], stdout=subprocess.PIPE, shell=True)
        (whois_cust, err) = proc.communicate()

        Cust_pattern = 'CustName:.*'
        find_cust = re.findall(Cust_pattern, whois_cust)

        for item in find_org:
                firstsplit  = re.split(':', item)
                firstsplit[1] = firstsplit[1].lstrip()
                z.add_row([line, firstsplit[1]])

        for item in find_cust:
                firstsplit = re.split(':', item)
                firstsplit[1] = firstsplit[1].lstrip()
                z.add_row([line, firstsplit[1]])

print z
