# merge_sort function sort the array by using divide-conquer techinique
def merge_sort(array:list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    
    # finding the middle element to divide the array
    mid = len(array)//2
    
    # consistantly dividing the array by recursion
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    # to merge the arrray
    return merge(left,right)

# merge function merges the sorted aarray 
def merge(left,right):
    i =0
    j = 0
    result = []
    while i < len(left) and j <len(right):
        # if the left ith element is smaller than the right jth element it will append left element into result list
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        # if the left ith element is larger than the right jth element it will append right element into result list   
        else:
            result.append(right[j])
            j += 1
     
    # if the one array is exhausted       
    result += left[i:]
    result += right[j:]
    
    return result

if __name__ == "__main__":

    array = [1,2,4,5,63,7]
    merge_sorted_array = merge_sort(array)
    print(merge_sorted_array)