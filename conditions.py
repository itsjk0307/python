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

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car=='gm':
#     print(car.upper())
#   else:
#     print(car.title())
    
#  # BIR NECHTA SHARTLARNI TEKSHIRISH
    
 
# age = int(input("how old are you?>>>"))
# if age >= 4:
#     print("you dont need to pay")
# elif age <=12:
#      print(" you should pay 5000 won")
# else:
#     print("you shpuld pay 10000 won ")
    
    
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: # yosh bolalarga bepul
#     price = 0
# elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else: # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")    

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')
    
    
# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))

# # Convert the input to lowercase to simplify comparison
# kun_lower = kun.lower()

# # Check if it's either Saturday or Sunday and the temperature condition
# if kun_lower in ['shanba', 'yakshanba'] and harorat >= 30:
#     print("Cho'milgani ketdik!")
# elif kun_lower in ['shanba', 'yakshanba'] and harorat < 30:
#     print("Uyda dam olamiz!")
    
    
# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = True
# non = True
# kompot = True
# assorti = True 
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:    # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")    




# RO'YXAT TARKIBINI TEKSHIRISH in OPERATORI

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')
    
# not in OPERATORI    
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')
    

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    