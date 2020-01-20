# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i #i guess this is a temp var
        smallest_index = cur_index
        print(f'current index in outer loop {cur_index}')
        # TO-DO: find next smallest element
        
        #Loop through elements on right-hand-side of current index
        for j in range(cur_index+1, len(arr)):
            print(f'current index in innner loop {cur_index}')
            #find the smallest index
            if cur_index < j:
                # Swap the element at current index with the smallest element found in above loop
                j = smallest_index
                print(j)


    return arr

items = [9,4,5,6,8,1,3,7,2]
selection_sort(items)
print(items)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr