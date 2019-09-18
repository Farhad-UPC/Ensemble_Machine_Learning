#Dictionary
#The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples
dic1 = {1:"a",2:.258,3:"three",400:"b"}
print ('dic1 = ',dic1)
print('----------------------------')
dic2 = {"a":19,"b":20,"c":16}
print ('dic2 = ',dic2)
print ('dic2[a] = ',dic2['a'])
print('----------------------------')
#print ('dic2[1:2] = ',dic2[1:2])
dic3 = {}
print ('dic3 = ',dic3)
print('----------------------------')
dic3[1] = "one"
print ('dic3[1]= one => ',dic3)
print('----------------------------')
dic3[2] = "two"
dic3[3] = "three"
print ('dic3 = ',dic3)
print('----------------------------')
dic3['a'] = 1
print ('dic3[a] = 1 => ',dic3)
print('----------------------------')
dic3[1] = "four"
print ('dic3[1]= one => ',dic3)
print('----------------------------')
#print (dic3 * 2)               #unsupported operand type(s) for *: 'dict' and 'int'
#dic4 = dic2 + dic3
#print(dic4)                    #unsupported operand type(s) for +: 'dict' and 'dict'
#del dic4

dic5 = {(1,2):"a",(3,4):45,"b":2.5,(5,6):4} 
print ('dic5 = ',dic5)
print('----------------------------')
print ('dic5[(3,4)] =',dic5[(3,4)])
print('----------------------------')
print ('len(dic5) =',len(dic5))
print('----------------------------')
print ('dic5 == dic5 =>',dic5 == dic5)
print('----------------------------')
print ('dic5 != dic3 =>',dic5 != dic3)
print('----------------------------')
# --index-- in / not in dictionaryName
print ('(1,2) in dic5 =>',(1,2) in dic5)
print('----------------------------')
print ('(1,2) not in dic5 =>',(1,2) not in dic5)
print('----------------------------')
print ('a in dic5 =>','a' in dic5)  # a is not index
print('----------------------------')

#name.copy()
#name.clear()
#name.values()
#name.items()
#name.has_key(x)  // for version 2 and not work for version 3
#name.keys()
#name.get()    // dict.get(key, default = None)

dic6 = {10:"a",20:"b",30:"c",40:"d"}
print ('dic6 = ',dic6)
print('----------------------------')
dic7 = dic6.copy()
print ('dic7 = ',dic7)
print('----------------------------')
dic7.clear()
print ('dic7.clear() = ',dic7)
print('----------------------------')
print ('dic6.values() = ',dic6.values())
print('----------------------------')
print ('dic6.items() = ', dic6.items())
print('----------------------------')
print ('dic6.keys() = ', dic6.keys())
print('----------------------------')
print ('dic6.get(40) = ', dic6.get(40))
print('----------------------------')
