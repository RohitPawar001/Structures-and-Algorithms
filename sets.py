# To create the set it is enclose the elements within curly braces
# Sets are unorderd collection of elements

a = {1,2,3,2}
print(type(a)) 
b = {5,9,4,5,5} 

# some usefull set methods
a.union()
a.update()
a.intersection()
a.isdisjoint()
a.issubset()
a.superset()
a.intersection_update()
a.difference()
a.symmetric_difference()
a.symmetric_difference_update()
a.add()
a.remove()
a.pop()

#we can pass the arguments to the above methods

del(a)
del(b)
