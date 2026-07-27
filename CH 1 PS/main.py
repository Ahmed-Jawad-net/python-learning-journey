first_name = "Jawad"
print(f"Hello {first_name}")
food = "Pizza"
print (f"My favorite food is {food}")

price = 999
txt = f"The price of the pizza is {price} rupees"
print(txt)  

#Numbers/Integers formatting
age = 23
print(f"you are {age} years old")

quantity = 3
print(f"You bought {quantity} pizzas")

num_of_students = 30 
print(f"There are {num_of_students} students in the class")

#float formatting
priceis = 10.99
print(f"The price of the pizza is  ${priceis} rupees")

cgpa = 3.21
print(f"My current CGPA is {cgpa}")

distance = 4.4
print(f"I ran {distance} kilometers today")

#Boolean formatting
is_student = False 

for_sale = False
is_online = True
if is_online:
    print("You are online")
else:
    print("You are offline")

#____________________________________________________________________________________________
# Typecasting = the  process of converting one data type to another data type
# int() = converts a data type to an integer
# float() = converts a data type to a float
# str() = converts a data type to a string  

name = "Jawad Ahmed"
age = 23
cgpa = 3.21
is_Student = True
cgpa = int(cgpa) #typecasting from float to int
print(cgpa)
#age = float(age) #typecasting from int to float
#print(age)
age = str(age) #typecasting from int to string
#age += "1" #concatenating a string with an integer (converted to string)
print(age)
name = bool(name) #typecasting from string to boolean
print(name)