# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    for i in range(len(arr)):
        # Loop through entire array
        mindex = i
        # Set minimum index to i
        for j in range(i + 1, len(arr)):
            # Nested loop that starts at the next element in array
            if arr[j] < arr[mindex]:
                # If variable found in nested loop is < the mindex
                mindex = j
                # Set that lower value to the mindex
        if mindex != i:
            # If mindex source j != mindex source i
            arr[i], arr[mindex] = arr[mindex], arr[i]
            # Swap the two values

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    # Set a value for the length of the array
    for i in range(n - 1):
        # Loop through the array minus the last element
        # Once the arr[-2] is sorted, arr[-1] will be as well
        for j in range(n - 1 - i):
            # Nested loop that loops over the array
            # -1 skips the last item in the array
            # -i skips the last item that was just sorted
            if arr[j] > arr[j + 1]:
                # If the current index is greater than the following index
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Swap them
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
