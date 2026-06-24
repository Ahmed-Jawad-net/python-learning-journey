def myfunc():

        global x # this will make the variable x a global variable, which means it can be accessed and modified outside of the function as well.
        x = "awesome"
        y = "Fantastic"
myfunc()
y="Language"
print("Python is " + x)
print("Python is " + y) #it will not print "Python is Fantastic" because the variable y is a local variable that is only accessible within the myfunc() function. When we try to print y outside of the function, it will result in a NameError because y is not defined in that scope.it will print "Python is Language" because we have assigned a new value "Language" to the variable y outside of the function. This new value will be used when we print y, and it will not affect the value of y inside the myfunc() function.
