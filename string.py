# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:22:58 2024

@author: MyHome
"""

# f_string function
name='Jamshid'
surname="Khaytbaev"
full_name=f"{name} {surname}"
print(full_name)
print("Hello World!")
print("Hello \tWorld! ")
print('Hello \nWorld!')



# upper() va lower() metodlari
# title() va capitalize() metodlari
# strip(), rstrip() va lstrip() metodlari

name="Jamshid"
surname="Khaytbaev"
text=" I love you "
full_name=f" {name} {surname}"
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(full_name.capitalize())
print(text.strip())
print(text.lstrip())
print(text.rstrip())



# INPUT —FOYDALANUVCHI BILAN MULOQOT

name=input("What is your name?")
print("Hello " + name)