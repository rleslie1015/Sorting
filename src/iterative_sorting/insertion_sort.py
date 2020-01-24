#insertion sort from guided project
items = [2,4,5,6,8,1,3,7,9]
def insertion_sort(items):
    # Split the list into sorted and unsorted
    # For each element in unsorted...
    for i in range(1, len(items)):
        # Insert that element into the correct place in sorted by: 
        # Store the element in a temp variable
        temp = items[i]
        # Shifting all larger sorted elements to the right by 1
        j = i 
        while j > 0 and temp < items[j - 1]:
            items[j] = items[j - 1]
            j-=1  
        # Insert the elemnt after the first smaller element
        items[j] = temp
    return items

insertion_sort(items)
print(items)