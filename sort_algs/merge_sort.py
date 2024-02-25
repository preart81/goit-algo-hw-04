def merge_sort(arr: list) -> list:
    """
    Сортує список за допомогою алгоритму сортування злиттм.

    Аргументи:
        arr (list): Вхідний список, який необхідно відсортувати.

    Повертає:
        list: Відсортований список.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left: list, right: list) -> list:
    """
    Об'єднує два відсортованих списки в один відсортований список.

    Параметри:
        left (list): перший відсортований список.
        right (list): другий відсортований список.

    Повертає:
        list: Об'єднаний відсортований список від найменшого до найбільшого елемента.
    """
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2]
    sorted_arr = merge_sort(arr)
    print(arr, sorted_arr)
