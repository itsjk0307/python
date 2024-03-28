# Python Functions 


# def say_hi():
#     """Salom beruvchi func"""
#     print("HI Jamshid")
    
# say_hi()


# def say_hi(name):
#     print(f"Hi {name.title()}!")
    
# say_hi("Jamshid")



# def full_name(name, surname):
#     print(F"Hi mister {name.title()} {surname.title()}")
    
    
# full_name("Jamshid", "Khaytbaev")
# full_name(surname="Khaytbaev", name="Jamshid")
# def count_age(born, current_year=2024):
#     print(f"you are {current_year-born} years old my boy!")

# count_age(2001)

# def calcute_birth_year(name, age):
#     from datetime import datetime
    
#     current_date = datetime.now()
#     birth_year = current_date.year-age
#     print(f"{name}'s birth year is: {birth_year}")
    
    
# name = input("Enter your name:")
# age = int(input("Enter your age:"))

# calcute_birth_year(name ,age)   

# def calculate(number):
#     num1 = number * 2
#     num2 = number * 3
#     print(f"num1 ning kavdatrati {num1}ga teng ")
#     print(f"num2 ning kubi {num2}ga teng ")
 
# number  = float(input("Enter any number:"))
# calculate(number)

# def calculate(number):
#     if number % 2 != 0:
#         print("This number is odd")
#     else:
#         print("This number is even")

# number = int(input("Enter any number: "))  # Removed print() around input()

# calculate(number)


# def calculateFunction(number1, number2):
#     if number1 > number2:
#         print(f"{number1} is larger than {number2}")
#     elif number1 < number2:  # Changed "else if" to "elif"
#         print(f"{number1} is smaller than {number2}")
#     else:  # Removed incorrect assignment and fixed indentation
#         print(f"{number1} and {number2} are equal")

# number1 = int(input("Enter number one: "))
# number2 = int(input("Enter number two: "))

# calculateFunction(number1, number2)


# def print_numbers(x, y=2):
#     print("X:", x)
#     print("Y:", y)
    
# x=input("Enter number X:")
# print_numbers(x)




def tekshir(son):
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} soni {i} ga qoldiqsiz bo'linadi.")

son = int(input("Son kiriting: "))
tekshir(son)





     








































 