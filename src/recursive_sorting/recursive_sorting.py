# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr_a, arr_b):
    # elements = len(arr_a) + len(arr_b)
    # merged_arr = [0] * elements

    # TO-DO
    merged_arr = []
    ldex = 0
    rdex = 0
    while ldex < len(arr_a) and rdex < len(arr_b):
        if arr_a[ldex] < arr_b[rdex]:
            merged_arr.append(arr_a[ldex])
            ldex += 1
        else:
            merged_arr.append(arr_b[rdex])
            rdex += 1
    if ldex == len(arr_a):
        merged_arr.extend(arr_b[rdex:])
    else:
        merged_arr.extend(arr_a[ldex:])
    return merged_arr


print(merge([2, 4], [1, 3]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    array_length = len(arr)
    if array_length < 2:
        return arr
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
