# interpolation search function searches an target element in an array
def interpolation_search(arr:list[int],
                        target:int) -> int:
    
    low = 0
    high = len(arr) - 1 
    
    # the loop contineous util the condition becomes the false
    while low <= high and low <= target <= high:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # it will estimate the position of the target element based on the high and low values
        position = low + ((target - arr[low]) * (high - low)) // (high - low)
        
        # if the target is equal to the arr having the position element if true then it returns position
        if arr[position] == target:
            return position
        
        # if the target is greater than the array in the position element then it decreament the position by 1
        elif arr[position] > target:
            high = position -1
            
        #  if the target is greater than the array in the position element then it increament the position by 1
        else:
            low = position + 1
            
    # if the element not present in the array the function returns -1
    return -1
        
if __name__ == "__main__":
    
    array = [1,2,3,4,5,6]
    target_element = 4
    result = interpolation_search(array,target_element)
    if result != -1:
        print(f"The {target_element} found at index {result}")
    else:
        print(f"The element {target_element} is not present in the array.")