def binary_search(arr,x):
    result = 0
    mid = round(len(arr)/2)
    if arr[mid] < x:
        for index,element in enumerate(arr[mid:]):
            if element == x:
               result = element
            pass
    else:
        element = 0
        while element != x:
            element = arr[mid]
            mid = mid-1
            if element == x:
               result = mid
               break
    print(result)

