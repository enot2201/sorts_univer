from configuration_data import random_data
from sorts.bubble_sort import bubble_sort
from sorts.cocktail_sort import cocktail_sort
from sorts.quick_sort import quick_sort
from search.binary_search import binary_search
import time

TrueConst = True
# ACTION_MAP = {'1': {
#             'name': 'bubble_sort',
#             'sort_type': bubble_sort(),
#         }
#     }


class Base:
    def check_method_of_input(self):
        """Получение способа задания массива"""
        print("Меню для сортировок")
        print("Как вы хотите задать входные данные?")
        print("1-вручную 2-рандомно 3-из файла")
        check_method = input()
        if check_method == "3":
            print("введите абсолютный путь в файлу")
            file_path = input()
            self.arr = self.input_from_file(file_path)
        elif check_method == "2":
            print("введите длинну массива")
            len_array = int(input())
            print("введите максимальный размер элемента массива")
            len_element_array = int(input())
            self.arr = random_data.generate_random_array(len_array, len_element_array)
            print("Хотите изменить элемент массива? Y/N")
            checker = input()
            while checker == "Y":
                print("введите индекс элемента массива который хотите заменить")
                orig_element = int(input())
                print("введите элемент на который хотите заменить")
                new_element = int(input())
                self.arr[orig_element] = new_element
                print(self.arr)
                print("Хотите изменить ещё один элемент? Y/N")
                checker = input()
        elif check_method == "1":
            print("введите массив")
            self.arr = [int(num) for num in input().split()]
        else:
            raise Exception("выберите другой вариант")
        if check_method == "1" or check_method == "3":
            print("Хотите узнать размерность массива? Y/N")
            checker = input()
            if checker == "Y":
                print(len(self.arr))
            elif checker == "N":
                pass
            else:
                raise Exception("Есть варианты только Y/N")
        print("Какой сортировкой вы хотите воспользоваться?")
        print("1-bubble sort,2-cocktail sort,3-quick sort")
        self.sort = input()

    def input_from_file(self, file_path):
        """Чтение массива из файла"""
        with open(file_path, "r") as f:
            arr = [[int(num) for num in line.split()] for line in f]
        return arr

    def base(self):
        """Основная функция"""
        while TrueConst == True:
            self.check_method_of_input()
            start_time = time.time()
            if self.sort == "1":
                bubble_sort(self.arr)
            elif self.sort == "2":
                cocktail_sort(self.arr)
            elif self.sort == "3":
                print(quick_sort(self.arr))
            elif self.sort == "4":
                print(quick_sort(self.arr))
                print("Какое число хотите найти?")
                x = int(input())
                binary_search(quick_sort(self.arr),x)
            elif self.sort == "all":
                print("bubble_sort")
                bubble_sort(self.arr)
                print(time.time() - start_time)
                start_time = time.time()
                print("cocktail_sort")
                cocktail_sort(self.arr)
                print(time.time() - start_time)
            else:
                raise Exception("нет такой сортировки")
            print(time.time() - start_time)


obj = Base()
obj.base()
