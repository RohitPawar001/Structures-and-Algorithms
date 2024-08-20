# binary search is performed to find the element
def binary_search(arr:list[int],
                key:int,
                low:int,
                high:int) -> int:
    
    while low <= high:
        mid =  (high+low)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# this function performs the exponential search
def exponential_search(array:list[int],
                    target:int):
    
    n = len(array)
    #if the target element found at 1st position it return 0
    if array[0] == target:
        return 0
    
    # if the target element not found at the position at 0 it will use binary search
    i = 1
    while i < n and array[i] <= target:
        i *= 2
    return binary_search(array, target, i // 2, min(i, n - 1))


if __name__ == "__main__": 
       
    arr = [1, 6, 13, 22, 34, 56, 78, 91, 105, 118]
    target = 56
    index = exponential_search(arr, target)

    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")
    
