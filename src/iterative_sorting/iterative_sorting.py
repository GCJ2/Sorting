# TO-DO: Complete the selection_sort() function below 
array = [1, 1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def selection_sort(arr):
    for i in range(len(arr)):
        # print(arr)
        # Loop through entire array
        mindex = i
        # Set minimum index to i
        for j in range(i + 1, len(arr)):
            # print(f'i: {i}')
            # Nested loop that starts at the next element in array
            if arr[j] < arr[mindex]:
                # print(f'arr[j]: {arr[j]}, arr[mindex]: {arr[mindex]}')
                # If variable found in nested loop is < the mindex
                # print(f'mindex: {mindex}, j: {j}')
                mindex = j
                # print(f'mindex: {mindex}, j: {j}')
                # Set that lower value to the mindex
        arr[i], arr[mindex] = arr[mindex], arr[i]
        # Swap the two values

    return arr


print(selection_sort(array))


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


print(bubble_sort(array))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
