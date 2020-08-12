#!/usr/bin/python3
# -*-coding:utf-8 -*-
# Author:Alex Li
import getpass

_username = 'dlj'
_password = 'dljdlj'
username = input("username:")
# password = getpass.getpass("password:")
password = input("password:")

# print(username, password)

if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")
