# Student Marks Calcualtor 
Math = int(input("Enter your math subject marks: "))
Comp = int (input("Enter your Comp subject marks: "))
Eng = int(input("Enter you Eng Subject Marks: "))
total_Marks = Math + Comp + Eng
avg_marks = (total_Marks/3)
print(f"Your total marks is : {total_Marks} ")
print(f"Your Avg marks is: {avg_marks:.2f}")
