"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random


def merge_sort(lst):
    if len(lst) > 1:
        center = len(lst) // 2
        left = lst[:center]
        right = lst[center:]

        merge_sort(left)
        merge_sort(right)

        left_idx = right_idx = list_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                lst[list_idx] = left[left_idx]
                left_idx += 1
            else:
                lst[list_idx] = right[right_idx]
                right_idx += 1
            list_idx += 1

        while left_idx < len(left):
            lst[list_idx] = left[left_idx]
            left_idx += 1
            list_idx += 1

        while right_idx < len(right):
            lst[list_idx] = right[right_idx]
            right_idx += 1
            list_idx += 1

        return lst


if __name__ == '__main__':
    random_list = [round(random.uniform(0, 50), 2) for _ in range(27)]

    print(random_list)
    print(merge_sort(random_list))
