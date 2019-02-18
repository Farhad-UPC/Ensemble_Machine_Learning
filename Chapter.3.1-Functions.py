#Functions
#Functions are a construct to structure programs. 
#They are known in most programming languages, sometimes also called subroutines or procedures. 
#Functions are used to utilize code in more than one place in a program. 

'''def function-name(Parameter list):
    statements, i.e. the function body'''
    
#Cmath => Mathematical functions for complex numbers
#cmath.sqrt(x) => Return the square root of x. This has the same branch cut as log().
#math => The math module is a standard module in Python and is always available. To use mathematical functions under this module, you have to import the module using import math.
#from math import*      => we can use floor() instead of math.floor()
#print(pow(x,y))
#print(pow(x,y,z))   =>    (x^y)%z

print("""Hello
World!""")
print('----------------------------')

def add(x1, y1):
    return x1 + y1

print ("add(4,5) = ", add(4,5))
print('----------------------------')


def Even_Odd(number):
    if (number%2==0):
        print ("Number is Even")
    else:
        print ("Number is Odd")
        
number = int (input("Enter your number (Even_Odd):"))
Even_Odd(number)
print('----------------------------')
def Func1(number):
    if (number >= 0):
        return True
    return False
        
number = int (input("Enter your number (Func1):"))
print (Func1(number))
print('----------------------------')
def Factorial(number):
    if number == 0:
        return 1
    else:
        return number*Factorial(number -1)
    
number = int (input("Enter your number (factorial):"))
print(Factorial(number))
print('----------------------------')
def Absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number

# Output: 4
print("Absolute_value(4) = ", Absolute_value(4))

# Output: 4
print("Absolute_value(-4) = ", Absolute_value(-4))
