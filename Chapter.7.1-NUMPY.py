# Import Library of Numpy
import numpy as np  

# Version of Numpy
np.__version__   

#NumPy is an N-dimensional array type called ndarray
#NumPy rank 1 array
x1 = np.array([1, 2, 3, 4,5])
print ('x1 =', x1) 
print ('------------------------------')
print ('type (x1) =', type (x1))
print ('------------------------------')
print ('x1.shape =', x1.shape)
print ('------------------------------')
print ('x1.size =', x1.size) # number of elements
print ('------------------------------')
print (x1[0],',',x1[1],',',x1[2],',',x1[3]) #Prints "1 2 3 4"
print ('------------------------------')
x1[3] = 0
print (x1) # Change an element
#A data type object (an instance of numpy.dtype class) describes how the bytes in the fixed-size block of memory corresponding to an array item should be interpreted.
'''#int8 = Byte (-128 to 127)
#int16 = Integer (-32768 to 32767)
#int32 = Integer (-2147483648 to +2147483647)
#int64 = Integer (-9223372036854775808 to +9223372036854775807)
#Boolean = (True or False) stored as a byte
#float = Shorthand for float64 : Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
#complex = Shorthand for complex128 : Complex number
#int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc. '''
    
x1a = np.array([1, 2, 3, 4] , dtype='float') #Desired data type of array, optional
#x1a = np.array([1, 2, 3, 4] , dtype='i1')
#x1a = np.array([1, 2, 3, 4] , dtype= complex)
print ('x1a =', x1a) 
print ('------------------------------')
print ('type (x1a) =', type (x1a))
print ('------------------------------')
print ('x1a.dtype =', x1a.dtype)
print ('------------------------------')
print ('x1a.itemsize =', x1a.itemsize) # 8 byte
print ('------------------------------')
print ('x1a.size =', x1a.size)
print ('------------------------------')
print ('x1a.shape =', x1a.shape)
print ('------------------------------')
x1b = np.array([[.25, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]])
print (x1b.dtype) #dtype is float
print ('------------------------------')
print ('x1b.shape =', x1b.shape) #(4,4)
print ('------------------------------')
x1ba = x1b [0:2,1:3]
print ('x1ba [0:2,1:3] : ', x1ba)
print ('------------------------------')
print ('x1b [0,2] : ', x1b [0,2])
print ('------------------------------')
x1b [0,2] = 17
print ('x1b = ', x1b)
print ('------------------------------')
print ('x1ba : ', x1ba) # has changed   3=>17
print ('------------------------------')
x1ba = +x1b [0:2,1:3] #x1ba dosen't depend on x1b
x1b [0,2] = 125
print ('------------------------------')
print ('x1b = ', x1b)
print ('------------------------------')
print ('x1ba : ', x1ba) # dosen't change
print ('------------------------------')
x1c = np.array([[.25, 2, 3, 4],[8],[9, 10, 11, 12],[13, 14, 15, 16]])
print ('x1c.shape =', x1c.shape) #(4,)
print ('------------------------------')
x1d = x1a.copy()
print('x1d =',x1d)
print ('------------------------------')
print ('x1d is x1a =', x1d is x1a) # False
print ('------------------------------')
print('x1d.ndim =',x1d.ndim) # dimension
