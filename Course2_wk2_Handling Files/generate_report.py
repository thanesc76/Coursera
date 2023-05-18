# generate employees.csv
with open("employees.csv","w") as file:
  file.write('Full Name, Username, Department\n')
  file.write('Audrey Miller, audrey, Development\n')
  file.write('Arden Garcia, ardeng, Sales\n')
  file.write('Bailey Thomas, baileyt, Human Resources\n')
  file.write('Blake Sousa, sousa, IT infrastructure\n')
  file.write('Cameron Nguyen, nguyen, Marketing\n')
  file.write('Charlie Grey, greyc, Development\n')
  file.write('Chris Black, chrisb, User Experience Research\n')
  file.write('Courtney Silva, silva, IT infrastructure\n')
  file.write('Darcy Johnsonn, darcy, IT infrastructure\n')
  file.write('Elliot Lamb, elliotl, Development\n')
  file.write('Emery Halls, halls, Sales\n')
  file.write('Flynn McMillan, flynn, Marketing\n')
  file.write('Harley Klose, harley, Human Resources\n')
  file.write('Jean May Coy, jeanm, Vendor operations\n')
  file.write('Kay Stevens, kstev, Sales\n')
  file.write('Lio Nelson, lion, User Experience Research\n')
  file.write('Logan Tillas, tillas, Vendor operations\n')
  file.write('Micah Lopes, micah, Development\n')
  file.write('Sol Mansi, solm, IT infrastructure\n')

import csv

def read_employees(csv_file_location):
  with open(csv_file_location) as csv_dict:
    csv.register_dialect('empDialect', skipinitialspace = True, strict = True)
    employee_file = csv.DictReader(csv_dict, dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
      employee_list.append(data)
  return employee_list

employee_list = read_employees('employees.csv')

print(employee_list)  # first result

def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

dictionary = process_data(employee_list)

print(dictionary)  # second result

def write_report(dictionary, report_file):
  with open(report_file,'w+') as f:
    for k in sorted(dictionary):
      f.write(str(k) + ':' + str(dictionary[k]) + '\n')
    f.close()

write_report(dictionary, 'report.txt')
