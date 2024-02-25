def insertion_sort(arr: list) -> list:
    """
    Сортує вхідний масив за допомогою алгоритму сортування вставками.

    Параметри:
        arr (list): Список, який потрібно відсортувати.

    Повертає:
        list: Відсортований масив.
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2]
    print(arr, insertion_sort(arr))
