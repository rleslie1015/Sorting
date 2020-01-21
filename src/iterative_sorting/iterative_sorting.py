# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i 
        smallest_index = cur_index
        # TO-DO: find next smallest element
        #Loop through elements on right-hand-side of current index
        for j in range(i+1, len(arr)):
            a = arr[j]
            #find the smallest index
            if a < cur_index:
                smallest_index = a
        # Swap the element at current index with the smallest element found in above loop
        if(i != smallest_index):
            arr[i] = arr[smallest_index]
            arr[smallest_index] = arr[i]
            


    return arr

items = [9,4,5,6,8,1,3,7,2]
selection_sort(items)
print(items)

# TO-DO:  implement the Bubble Sort function below
# Bubble sort : Basically just goes throuht the list and compares two items and swaps those two items in order.
# The loop stops after a list has no more items to swap.
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        print(arr[i+1])
        print(arr[i])
        if arr[i] < arr[i+1]:
            smallest = arr[i]
            arr[i] = arr[i+1]
            print(arr[i])



    # for i in range(0, len(arr)):



    return arr
list2 = [5,4,3,2,1]
bubble_sort(list2)
print(list2)
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr