#Conditional Statements
#if/elif/else/while   => if+else=elif
#for variable in iterator:         iterator=> data structures in python => sequence,list,tuple,dictionary, set => run until there is element in structure
#             statements

#if condition:      => and/ or/ not/ !=/ ==/ <=/ >=/ </ >
#         statement1
#        statement2

a=int (input("Enter an integer Number:"))
if a >= 0:
    print(a,"is positive!")
if a < 0:
    print(a,"is nagative!")
print('----------------------------')
b=int (input("Enter an integer Number:"))
if b >= 0:
    print(b,"is positive!")
else:
    print(b,"is nagative!")
print('----------------------------')
if b > 0:
    print("The number is positive!\n")
elif b == 0:
    print("The number is zero!\n")
else:
    print("The number is nagative!\n")
print('----------------------------')
c = float (input("Enter a Number:"))
if -1<= c <=1:
    print("Yse!")
else:
    print("No!")
print('----------------------------')
d=50
if d % 5 == 0:
    if d % 10 == 0:
        print("Yes!")
print('----------------------------')
