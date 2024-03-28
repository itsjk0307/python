# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:25:50 2024

@author: MyHome
"""

fruits = ['apple', 'mango', 'banana']
print(fruits[0])

# Yangi element qo'shish append, insert,
fruits.append('grape')
print(fruits)
fruits.insert(0, 'dragon fruit')
print(fruits)

 # Elementni o'chirish remove, 
del fruits[0]
print(fruits)
fruits.remove("apple")
print(fruits)


# # Elementni sug'urib olish
grocery = ['oil', 'onion', 'banana', 'meat']
thing = grocery.pop()  # pop() removes the last element by default, so no need for the index
print(f"I bought {thing} from the market.")
print(f"I have to buy {grocery}.")


# # RO'YXATNI TARTIBLASH sorting lists
cars=['bmw','mers ','volvo','gm','audi', 'tesla']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)



# RO'YXATNI AYLANTIRISH

fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)


# RO'YXATNING UZUNLIGINI BILISH

fruits = ['pear','banana','apple','watermelon','lemon']
print(len(fruits))





# range() FUNKTSIYASI
# Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. 
# list()
#  funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:

numbers= list(range(0,11))
print(numbers)



# range()
 # yordamida qadamni ham berishimiz mumkin:
     
juft_sonlar = list(range(0,21,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)


# RO'YXATNI KESISH

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:4] # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars) 


# RO'YXATDAN NUSXA OLISH COPYING NUMBERS 
sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)


# TUPLES - O'ZGARMAS RO'YXAT

tomonlar = (20, 30, 55.2)
print(tomonlar)


toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])






























