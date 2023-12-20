def cocktail_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        # Проход слева направо
        for i in range(left, right):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        right -= 1
        # Проход справа налево
        for i in range(right, left, -1):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        left += 1
    print(arr)
