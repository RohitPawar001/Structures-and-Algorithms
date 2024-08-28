def quicksort(arr:list[int]) -> list[int]:
    
    # if the len of the array is less than 1 i.e the array is already sorted
    if len(arr) <= 1:
        return arr
    
    # pivot is the middle element and also it can used to divide the array by smaller and larger element than pivot element
    pivot = arr[len(arr)//2]
    
    # left is subarray containing elements smaller than the pivot element
    left = [x for x in arr if x < pivot ]
    
    # middle is an element which is equal to the pivot element
    middle = [x for x in arr if x == pivot]
    
    # right is subarray containing the elements larger than the pivot element
    right = [x for x in arr if x > pivot]
    
    # recursively calling the quicksort function until we get the sorted array
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__maim__":
    arr = [1,4,5,2,6,78]
    sorted_array = quicksort(arr)
    print(sorted_array)