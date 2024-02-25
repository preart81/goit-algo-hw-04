def bubble_sort(arr: list) -> list:
    """
    Сортує список за допомогою алгоритму сортування бульбашками.

    Аргументи:
        arr (list): Вхідний список, який необхідно відсортувати.

    Повертає:
        list: Відсортований список.
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2]
    print(arr, bubble_sort(arr))
