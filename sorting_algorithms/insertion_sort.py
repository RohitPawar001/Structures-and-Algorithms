
def insertionSort(array:list[int]) -> list[int]:
    
    # finding the length of the array
    n = len(array)
    
    # if the length of the array is smaller than the 1 that means array is already sorted
    if n <= 1:
        return array
    
    # iterating through the array from the second element of the aray to the length of the array
    for i in range(1,n):
        j = i
        
        # this loop will insert the the smallest element until the one previous elemement is less than the current element
        while j > 0 and array[j - 1] > array[j]:
            array[j-1],array[j] = array[j],array[j-1]
            j -= 1
     
     
if __name__ == "__main__":       
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print(arr)