def binary_search(arr:list[int],
                element_to_search:int) -> int:
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        
        mid = (low+high)//2
        if arr[mid] < element_to_search:
            low = mid + 1
        elif arr[mid] > element_to_search:
            high = mid - 1
        else:
            return mid
        
    return -1

if __name__ == "__main__":
    array = [1,2,3,4,5,6]
    element = 5
    
    result = binary_search(array,element)
    if result != -1:
        print(f"The element {element} found at position {result}")
    else:
        print(f"The element {element} is not present in the array")