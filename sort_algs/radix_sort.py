def counting_sort(arr: list, position: int) -> list:
    """
    Сортує масив arr, використовуючи підрахунок для певного розряду, вказаного в position.

    Параметри:
        arr (list): Масив цілих чисел для сортування.
        position (int): Позиція розряду, за яким відбувається сортування (1 для одиниць, 10 для десятків, тощо).

    Повертає:
        list: Масив цілих чисел, відсортований за вказаним розрядом.
    """
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Рахунок входжень певного розряду
    for i in range(0, size):
        index = arr[i] // position % 10
        count[index] += 1

    # Оновлення count[i] так, щоб він показував позицію наступного входження своєї цифри
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Побудова вихідного масиву
    i = size - 1
    while i >= 0:
        index = arr[i] // position % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

    return arr


def radix_sort(arr: list) -> list:
    """Сортування масиву за розрядами.

    Параметри:
        arr (list): Масив цілих чисел для сортування.

    Повертає:
        list: Масив цілих чисел, відсортований за розрядами.
    """
    arr = arr.copy()
    # Визначення максимального числа для визначення кількості розрядів
    max_num = max(arr)
    position = 1
    # Виконання counting_sort для кожного розряду
    while max_num // position > 0:
        r = counting_sort(arr, position)
        position *= 10
    return r


if __name__ == "__main__":
    arr = [3, 89, 67, 254, 9, 21, 185, 4, 62]
    print("Вихідний масив:", arr)
    print("Відсортований масив:", radix_sort(arr))
