#Loops 
#while /  for in
#break/continue/pass     pass=>like nor

#while condition:
#           statement1
#          ...

a = int(input("Enter your Number:"))

while 0< a < 7:
    print (a)
    a = a-1
else:
    print("Finish!")
print('----------------------------')
b = 10
list_b= []

while b <= 200:
    c = b * 2
    list_b.append(c)
    b = b * 3
print(list_b)
print('----------------------------')
#we don't need to define variable (x) in advance
colors = ["red", "blue", "green"]
for x in colors:
  print(x)
print('----------------------------')
for x in "green":
  print(x)
print('----------------------------')
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.it is possible to specify the increment value by adding a third parameter: range(2, 10, 1)
for x in range(8):
  print(x)
print('----------------------------')
for x in range(2, 30, 4):
  print(x)
print('----------------------------')
d = "red"
e = "blue"
for x in d:        
    print(x + e)
print('----------------------------')
for a in range(1,5):
    for b in range(1,10):
        print(a+b)
print('----------------------------')
for x in range(7):
  print(x)
else:
  print("finished!") 
print('----------------------------')
for x in colors:
  if x == "blue":
    break
  print(x)
print('----------------------------')
for x in colors:
  print(x)
  if x == "blue":
    break
print('----------------------------')
for x in colors:
  if x == "blue":
    continue
  print(x)
print('----------------------------')
#pass Statement -> It is used when a statement is required syntactically but you do not want any command or code to execute.
for x in 'wellcome': 
   if x == 'c':
      pass
      print ("pass block")
   print ("x :", x)
print ("Finished!")
