# bubbleSort function sort the array by swapping if the next element is smaller than the current element
def bubbleSort(arr:list[int]) -> list[int]:
    
    n = len(arr)
    
    # this loop iterate over the array
    for i in range(n):
        
        # swapped is used to check weather the arr is already sorted or need to be sorted
        swapped = False
        
        # this loop iterate over the swapped elements
        for j in range(0,n-i-1):
            
            # if the next element is greater than the current this will swap the elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # if any swapping has not done then it will break the loop
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    sorted_arr = bubbleSort(arr)
    print("Sorted array:", sorted_arr)