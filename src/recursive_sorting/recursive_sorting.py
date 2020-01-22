# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #    While your data set contains more than one item, split it in half
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[0 : mid])
        right = merge_sort(arr[mid:])
        return(merge(left, right))
    #  Start merging your single lists of one element together into larger, sorted sets

 

list1 = [5,4,3,2,1]
merge_sort(list1)
print(list1)
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
