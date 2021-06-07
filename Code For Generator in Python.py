#table generator

from num2words import num2words
print("Welcome to Table Generator!")
x=1
n=int(input("please enter any number: "))
if n>0:
        print("Table of ", num2words(n))
        while x <= 10:
         print(n, " * " , x ,"=", n * x )
         x += 1
else:
        print("Please enter number greater than 0")
        
