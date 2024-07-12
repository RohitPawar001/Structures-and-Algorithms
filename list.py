#allocating space in memory
mix_list = [1,"a",2,"b",3,"c"]
print(mix_list)


#list methods

mix_list.append("element") #append() adds an element to the list

mix_list.reverse() #reverse() used to reverse the elements of the list

mix_list.index("element") #index() gives the index of the given argument

mix_list.count("element") #count() it returns the no. of occurences of the element

mix_list.insert(0,"element_2") #insert() it insert the perticular element in an given index

mix_list.remove("element") #remove() it is used to remove an element from list

new_list = mix_list.copy() #copy() used to copy the one list to another

new_list.clear() #clear() used to clear the list

 
#relocation of memory space
del(mix_list)
del(new_list)
