import math

def jump_search(arr:list[int], key:int)  -> int:
    
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # finding the block where the key is present
    while arr[min(step, n)-1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1 
      
    # this loop performs the linear search  
    while arr[prev] < key:
        prev += 1 
        if prev == min(step,n):
            return -1
    
    # if the element not present in the list it will return -1 
    if arr[prev] == key:
        return prev
    
    return -1


if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    x = 55
    
    presense = jump_search(arr,x)
    
    if presense != -1:
        print(f"Element found at index {presense}")
    else:
        print("Element not found")
    