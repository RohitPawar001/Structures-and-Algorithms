#ByteArray is same as list except it is specifically build for storing bytes datastructure

#to declare the bytearray we need to typecast the iterable bu using bytearray()

byte_array = bytearray([1,2,3,5,3,3])
print(type(byte_array))
#<class 'bytearray'>

array = [5,6,5,8]
# some usefull methods in bytearray

byte_array.reverse()
byte_array.remove(1)
byte_array.appene(1)
byte_array.insert(0,1)
byte_array.pop(1)
byte_array.extend(array)


del(byte_array)
del(array)
