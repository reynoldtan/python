#!/usr/bin/env python3
import csv

hosts = [['workstation.local', '192.168.25.46'], ['webserver.cloud', '10.2.5.6']]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writeer(hosts_csv)
    # writer.writerows (all) or writer.writerow (1 row)
    writer.writerows(hosts)