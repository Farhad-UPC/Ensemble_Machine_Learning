#Tuple
tuple1 = ("a","e","f","g",12,18.35,14.1)
print ('tuple1 = ',tuple1)
print ('type = ',type(tuple1))
print('----------------------------')
tuple2 = 2,3,4,"a","e","ff",12.5
print ('tuple2 = ',tuple2)
print ('type = ',type(tuple1))
print('----------------------------')
a = tuple1[0]
print ('tuple1[0] = ',a)
print('----------------------------')
b = tuple1[-7]
print ('tuple1[-7] = ',b)
print('----------------------------')
c = tuple1[1:3]
print ('tuple1[1:3] = ',c)
print('----------------------------')
d = tuple1[:]
print ('tuple1[:] = ',d)
print('----------------------------')
e = tuple1[-2:-4]  #no answer
print ('tuple1[-2:-4] = ',e)
print('----------------------------')
tuple3 = ("a",)
tuple4 = (2,)
tuple5 = ("a")
tuple6 = (2)
tuple7 = "a",
print ('tuple3 = ',type(tuple3))
print ('tuple4 = ',type(tuple4))
print ('tuple5 = ',type(tuple5))
print ('tuple6 = ',type(tuple6))
print ('tuple7 = ',type(tuple7))
print('----------------------------')
# tuple object does not support item assignment
#tuple1[1] = 8796
#print ('tuple1[1] = 8796 ',tuple1[1])
tuple8 = tuple3 + tuple4
print ('tuple8 = ',tuple8)
print('----------------------------')
tuple9 = ("a",)+(2,)
print ('tuple9 = ',tuple9)
print('----------------------------')
tuple10 = ("a",)+tuple9[:]
print ('tuple10 = ',tuple10)
print('----------------------------')
tuple11 = (12,)+tuple1[3:]
print ('tuple11 = ',tuple11)
print('----------------------------')
tuple12 = ("a",)*4
print ('tuple12 = ',tuple12)
print('----------------------------')
tuple13 = tuple1 * 2
print ('tuple13 = ',tuple13)
print('----------------------------')
print ('a in tuple1 = ',"a" in tuple1)
print('----------------------------')
print ('a not in tuple1 = ',"j" not in tuple1)
print('----------------------------')
print ('length of tuple13  = ',len(tuple13))
print('----------------------------')
tuple14 = (('a',12,13.5),(14,15,16,'ab'))
print ('tuple14 = ',tuple14)
print('tuple14[1][0] = ',tuple14[1][0])
print ('type (tuple14) = ',type(tuple14))
print('----------------------------')
tuple15 = ("a","b","c")
first,second,third = tuple15 
print(tuple15 [1])
print('----------------------------')
print ('second =', second)
print('----------------------------')
#name.count(x)     // number of repetition of x
#name.index(x)     // show number of index   0,...
print ('tuple15.count(a) =', tuple15.count("a"))
print('----------------------------')
print ('tuple15.index(a) =', tuple15.index("a"))
print('----------------------------')
