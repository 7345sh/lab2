# Вычисляет факториал числа n
def factorial(n: int) -> int:
    # Проверка на корректность условия
    if n < 0:
        raise ValueError("Факториал определён для неотрицательных чисел")

    # Вычисление
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


if __name__ == "__main__":
    try:
        n = int(input("Введите число n >= 0: "))
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print(f"Ошибка: {e}")
