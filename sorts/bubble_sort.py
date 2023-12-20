def bubble_sort(arr):
    """сортировка пузырьком"""
    len_arr = len(arr)
    # Проходим по всем элементам массива
    for i in range(len_arr):
        checker = 0
        # Последние i элементов уже отсортированы, поэтому их не рассматриваем
        for j in range(0, len_arr - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
                checker = 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not checker:
            break
    print(arr)
