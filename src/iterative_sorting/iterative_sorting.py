# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i #i guess this is a temp var
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for cur_index in range(0, len(arr) - 1):
            while cur_index > 0 and cur_index < i:
                if cur_index < smallest_index:
                    smallest_index = cur_index
              

        # TO-DO: swap




    return arr

items = [2,4,5,6,8,1,3,7,9]
selection_sort(items)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr