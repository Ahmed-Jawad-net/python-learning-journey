# first_name = "Jawad"
# print(f"Hello {first_name}")
# food = "Pizza"
# print (f"My favorite food is {food}")

# price = 999
# txt = f"The price of the pizza is {price} rupees"
# print(txt)

# #Numbers/Integers formatting
# age = 23
# print(f"you are {age} years old")

# quantity = 3
# print(f"You bought {quantity} pizzas")

# num_of_students = 30
# print(f"There are {num_of_students} students in the class")

# #float formatting
# priceis = 10.99
# print(f"The price of the pizza is  ${priceis} rupees")

# cgpa = 3.21
# print(f"My current CGPA is {cgpa}")

# distance = 4.4
# print(f"I ran {distance} kilometers today")

# #Boolean formatting
# is_student = False

# for_sale = False
# is_online = True
# if is_online:
#     print("You are online")
# else:
#     print("You are offline")

# #____________________________________________________________________________________________
# # Typecasting = the  process of converting one data type to another data type
# # int() = converts a data type to an integer
# # float() = converts a data type to a float
# # str() = converts a data type to a string

# name = "Jawad Ahmed"
# age = 23
# cgpa = 3.21
# is_Student = True
# cgpa = int(cgpa) #typecasting from float to int
# print(cgpa)
# #age = float(age) #typecasting from int to float
# #print(age)
# age = str(age) #typecasting from int to string
# #age += "1" #concatenating a string with an integer (converted to string)
# print(age)
# name = bool(name) #typecasting from string to boolean
# print(name)

# input() = allows user input (A function that prompts the user to enter data and return it as a string)
# name = input("What is your name? ")
# age = int( input("How old are you? "))
# # age = int(age) #typecasting from string to int
# age = age + 1

# print(f"Hello {name}!")
# print(f"You are {age} years old ")

# -----------------------------------------------------------------------------
# Exercise  Practice calculate the area of a rectangle
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width
# print(f"The area of the rectangle is {area}")

# -----------------------------------------------------------------------------
# Exercise Practice 2 Shopping cart program
# item = input("What item would you like to buy? ")
# price = float(input(f"What is the price of {item}? "))
# quantity = int(input(f"How many {item}s would you like to buy? "))
# Total = price * quantity
# print(f"You have purchased {quantity} {item}(s) ")
# print(f"Your Total bill is ${Total:.2f}")

# -----------------------------------------------------------------------------
# Arthematic operations
friend = 5
# friend +=1 #augmented assignment operator
# friend = friend - 2 
# friend -= 2 #augmented assignment operator
# friend = friend * 5
# friend *= 5 #augmented assignment operator
# friend = friend / 2 
# friend /= 2 #augmented assignment operator

# friend = friend ** 3
# friend **=3 #augmented assignment operator

# remainder = friend % 2
# friend %= 2 #augmented assignment operator
# print(f"You have {friend} friend's")

# Round() = rounds a number to the nearest integer or specified decimal places
w = 2
x = 3.44
y = -4
z = 5
# result = round(x) #rounds to the nearest integer
# print(f"The rounded value of {x} is {result}")
# result = abs(y) #returns the absolute value of a number
# print(f"The absolute value of {y} is {result}")
# result = pow(w, z) #returns the value of w raised to the power of z
# print(f"The value of {w} raised to the power of {z} is {result}")
# result = max(w, x, y, z) #returns the maximum value among the given numbers
# print(f"The maximum value among {w}, {x}, {y}, and {z} is {result}")
#result = min(w, x, y, z) #returns the minimum value among the given numbers
#print(f"the minimum value is {result}")
import math 

# print(math.pi)
# print(math.e)

# x = 9
# result = math.sqrt(x)
# print(f"The square root of {x} is {result}")
# result = math.ceil(x) #rounds up to the nearest integer
# print(f"The ceiling value of {x} is {result}")    

# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is {circumference:.2f}cm")
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is {round(area, 2)} cm^2")
# -----------------------------------------------------------------------------
#find the hypotenuse of a right triangle 
# a = float(input("Enter the A: "))
# b = float(input("Enter the B: "))

# c = math.sqrt(pow(a,2) + pow(b,2))
# print(f"Side C: {c:.2f}")
#------------------------------------------------------------------------------
# if = Do something if a condition is true
# else = Do something if the condition is false 
 
# age = int(input("Enter your age: "))

# if age >= 100:
#     print("You are too old to vote")
# elif age >=18:
#     print("You are eligible to vote ")
# elif age < 0:
#     print("Invalid age")


# else:
#     print("You are not eligible to vote")
# _-----------------------------------------------------------------------------
# response = input("Would you like some food? (Y/N) ")
# if response == "Y" or response == "y":
#     print("Here is some food")

# else:
#     print("No food for you")

#------------------------------------------------------------------------------

# name = input("What is your Full Name? " )
# if name == "":
#     print("You did not enter your  name") 
# else:
#     print(f"Hello {name}")

#-----------------------------------------------------------------------------

# for_sale = False
# if for_sale:
#     print("This item is for sale")
# else:
#     print("This item is not for sale")

#-----------------------------------------------------------------------------

# for x in "Banana":
#     print(x)

# -----------------------------------------------------------------------------
# a = "Hello,World!"
# print(a[4]) #prints the second character of the string
# print(len(a)) #prints the length of the string
#------------------------------------------------------------------------------


# txt = "The best things in life are free!"
# print("free" in txt) #returns True if the word "free" is present in the string

#-----------------------------------------------------------------------------

# txt = "The best things in life are free!"
# if "free" in txt:
#     print("Yes, 'free' is present in the string")
# else:
#     print("No, 'free' is not present in the string")

#-----------------------------------------------------------------------------
# txt = "The best things in life are free!"
# print("tree" not in txt) #returns True if the word "free" is not present in the string

#-----------------------------------------------------------------------------
# txt = "The best things in life are free!"
# if "Expensive" not in txt:
    # print("Yes, 'Expensive' is not present in the string")

#-----------------------------------------------------------------------------
b= "helloworld"
print(b[2:5]) #returns the characters from index 2 to 5 (not included)