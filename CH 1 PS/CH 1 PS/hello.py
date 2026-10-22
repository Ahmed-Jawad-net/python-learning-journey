# print ("Hello, World")
# Ask user for their name

name = input("What's your name ? ")
# Say hello to user 

print("Hello, " + name ) # one large argument , + is used to concatenate strings
print("Hello, \"Friends\"") # to print double quotes inside a string, we use the escape character \ before the double quotes")

#print("Hello, ", end="") # end is used to change the default end character which is a new line, here we set it to an empty string so that the next print statement will continue on the same line
#print(name) # one argument, prints the name on the same line as "Hello, "
#print("Hello,", name) #two arguments, is used to separate arguments, adds a space between them"
print(f"Hello, {name}!") # f-string is a way to format strings in Python, it allows us to embed expressions inside string literals, using curly braces {}. The expression inside the curly braces is evaluated at runtime and the result is inserted into the string. In this case, {name} will be replaced with the value of the variable name.