# linear search function searches the element linearly in array
def linear_search(array:list[int],
        search_element:int) -> int:
    
    # for loop used to iterate over the elements from an array
    #if the element found in arry it will return index of element else return -1
    
    for element_index in range(0,len(array)):
        if array[element_index] == search_element:
            return element_index 
             
    return -1


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    element = 5
    presense = linear_search(arr,element)
    if presense == -1:
        print(f"The element {element} not present in array")
    else:
        print(f"The element {element} present in the position {presense}")
    