#simple interest calculator
pricipal_amout = float(input("Enter the pricipal amount: "))
rate = float(input("Enter the rate: "))
time = int(input("Enter the time: "))
simple_interest = (pricipal_amout * rate * time) / 100

print(f"Your simple interest is: {simple_interest}")