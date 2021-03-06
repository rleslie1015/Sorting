# TO-DO: complete the helper function below to merge 2 sorted arrays
# Merge 2 sorted arrays
def merge( arrA, arrB ):
    total_elements = len( arrA ) + len( arrB )
    print(total_elements)
    merged_arr = [0] * total_elements
    # TO-DO
    a = 0
    b = 0
    for i in range(total_elements):
        # Check if either list is empty, if so append the other
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # Otherwise, compare and append the smallest of the two
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else: 
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #    While your data set contains more than one item, split it in half
    # base case
    if len(arr) <= 1:
        return arr
    # divide in half
    else:
        mid = len(arr) // 2
        left = arr[ : mid ]
        right = arr[ mid : ]
        # sort the left and right
        left = merge_sort(left)
        right = merge_sort(right)
    #  Start merging your single lists of one element together into larger, sorted sets
        #merge together
        return merge(left, right)
    
 

list1 = [5,4,3,2,1]
print("merge sort")
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
