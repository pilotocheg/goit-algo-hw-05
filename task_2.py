def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter = 0
    closest_or_eq = None

    while low <= high and closest_or_eq is None:
        mid = (high + low) // 2
        iter += 1

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            closest_or_eq = arr[mid]

    if closest_or_eq is None:
        if arr[mid] < x:
            mid += 1
        if mid < len(arr):
            closest_or_eq = arr[mid]

    return (iter, closest_or_eq)
