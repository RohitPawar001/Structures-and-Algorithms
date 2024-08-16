# binary_search function implements the binary search in an sorted array

def binary_search(arr:list[int],
                element_to_search:int) -> int:
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        
        mid = (low+high)//2
        # if the element in the array at index mid is greater then the element it increament the mid by 1
        
        if arr[mid] < element_to_search:
            low = mid + 1
        # if the element in the array at index mid is less then the element it decreament the mid by 1 
          
        elif arr[mid] > element_to_search:
            high = mid - 1
        # if the element at index mid in array is equal to the element then it will return the index
        
        else:
            return mid
    
    # if element not found in the array it will return -1  
    return -1


if __name__ == "__main__":
    
    array = [1,2,3,4,5,6]
    element = 5
    
    result = binary_search(array,element)
    if result != -1:
        print(f"The element {element} found at position {result}")
    else:
        print(f"The element {element} is not present in the array")