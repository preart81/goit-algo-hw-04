def selection_sort(arr: list) -> list:
    """
    Сортує список за допомогою алгоритму сортування вибором.

    Аргументи:
        arr (list): Вхідний список, який необхідно відсортувати.

    Повертає:
        list: Відсортований список.
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    numbers = [5, 3, 8, 4, 2]
    print(numbers, selection_sort(numbers))
