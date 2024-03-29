# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:01:52 2024

@author: MyHome
"""
# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...Jamhsid 
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.




# name= input('What is your name?\n>>>')
# if name.lower() !='Jamshid':
#     print(f"Sorry, {name.title()} we are waiting for Jamshid")
# else:
#     print("Hi Jamshid")


# COMPARING NUMBERS

# answer = float(input("12x6 nechchiga teng?>>>"))
# if answer !=72:
#      print("Wrong answer!")
# else:
#     print("You are so smart!")
    
# age = int(input("How old are you?>>>"))
# if age >=18:
#         print("Welcome")
# else:
#         print("you cant eneter")
  
# login = input("Yangi login tanlang:")
# if len(login)<=5: # login uzunligini tekshiramiz
#     print("Login 5 harfdan ko'proq bo'lishi shart!")        

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car=='gm':
    print(car.upper())
  else:
    print(car.title())