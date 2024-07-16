# Dictionary is an collection of key and value pairs enclosed within curley braces

marks = {"steve":56,"Iron_man":99,"vision":89,"Hulk":72}

# we can access the elements from dictionary with the help of key 
# also we can update the value with the help of key as follows

marks["steve"] = 59

#some comman usefull methods of dictionary

marks.items()  #by using this method we can access key as well as the value

copied_dict = marks.copy()

marks.get("steve",0) # if the key found in dict then it returns value associated with the key else return default as 0.

marks.keys() # it returns all the keys from the dict

marks.pop("steve") # it remove the specified element

marks.popitem() # it removes the last inserted value and return as a tuple

marks.update({"Thor":500}) # it add another dictionary to the old one

marks.values() # it returns all the values from dictionary as a list.


del(marks)
del(copied_dict)