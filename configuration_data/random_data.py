import random


def generate_random_array(len_array, len_element_array):
    """Генерация массива рандомных чисел"""
    arr = [random.randint(0, len_element_array) for j in range(len_array)]
    print(arr)
    return arr
