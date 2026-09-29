# Сортирует список по возрастанию методом пузырька.
def bubble_sort(arr: list[int]) -> list[int]:
    result = arr.copy()

    # Внешний цикл: сколько элементов уже отсортировано с конца
    # (последний больше не сортируем)
    for i in range(len(result) - 1):
        swapped = False

        # Внутренний цикл: проход по ещё не отсортированной части
        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # Если за проход не было обменов, то список уже отсортирован
        if not swapped:
            break

    return result


if __name__ == "__main__":
    data = [1, 3, -8, 4, 2, -5, -7, 0]
    print(f"Исходный список: {data}")
    print(f"Отсортированный: {bubble_sort(data)}")
