#!/usr/bin/python3
# -*-coding:utf-8 -*-
# Author:Alex Li
name = input("username:")
age = int(input("age:"))  # integer
print(type(age), type(str(age)))
job = input("job:")
salary = input("Salary:")
# print(username,password)

info = '''
-----info of %s -----
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name, name, age, job, salary)
print(info)
info2 = '''
-----info of {_name} -----
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)

print(info2)
info3 = '''
-----info of {0} -----
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)

print(info3)