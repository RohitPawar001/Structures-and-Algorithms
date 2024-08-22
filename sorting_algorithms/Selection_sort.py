# selection sort function sort the array by partioning the array into sorted and  unsorted array
def selectionSort(arr:list[int]) -> list[int]:
    
    n = len(arr)
    # this outer loop is iterate over the arrray ie the sorted array
    for i in range(n):
        
        # asume that the first element is minimum
        min_idx = i
        
        # this loop iterate over the unsorted array
        for j in range(i+1,n):
            
            # if the element having minimum value found then the min_index is set to j
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # swapping
        arr[i],arr[min_idx] = arr[min_idx], arr[i]
        
    return arr
        
        
if __name__ == "__main__":     
    arr = [64, 25, 12, 22, 11]
    print("Unsorted array:", arr)
    sorted_arr = selectionSort(arr)
    print("Sorted array:", sorted_arr)