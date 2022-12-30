#!/usr/bin/env python3
import csv

f = open('employee.csv')
csv_f = csv.reader(f)

for row in csv_f:
    name, phone, role = row
    prin('Name: {} Phone: {} Role: {}'.format(name, phone, role))
    # row is a list: also valid row[0], row[1], row[2]

f.close()