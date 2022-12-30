#!/usr/bin/env python3
import csv

# https://docs.python.org/3/library/csv.html

# READ
# software.csv - has column name (key) instead of index.
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print('{} has {} users'.format(row['name'], row['users']))


# WRITE
users = [{'name': 'Rose Jones', 'username': 'rosej'},
  {'name': 'Alfred Potter', 'username': 'alfredp'},
  {'name': 'Felix Reed', 'username': 'felixr'}
]

keys = ['name', 'username']

with open('user.csv', 'w') as users:
    writer = csv.DictWriter(users, fieldnames=keys)
    writer = writeheader()
    writer = writerows(users)

  
# Excercise on a virtual machine.
#!/usr/bin/env python3
import csv

#@csv_file_location: absolute path to employee.csv
#headers: Name, Department
def read_employee(csv_file_location):
    with open(csv_file_location) as file:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(file, dialect='empDialect')

    employee_list = []
    for emp in employee_file:
        employee_list.append(emp)
    
    return employee_list

def process_data(employee_list):
    department_list = []
    for emp in employee_list:
        department_list.append(emp['Department'])
  
    department_data = {}
    # set department list to remove redundancy.
    for dep in set(department_list):
        department_data[ dep ] = department_list.count(dep)

    return department_data


def write_report(dictionary, report_file):
    with open(report_file, 'w+') as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[ k ] + '\n'))



# employee_file = '/home/student/data/employee.csv'
# report_file = '/home/student/data/report.txt'
# employee_list = read_employee(employee_file)
# dictionary = process_data(employee_list)
# write_report(dictionary, report_file)