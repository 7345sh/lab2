# Выводит таблицу умножения 10x10
def multiplication_table(size: int = 10) -> None:
    # Оформление
    print()
    print(f"     Таблица умножения от 1 до {size}")
    print()
    print("     ", end="")
    for j in range(1, size + 1):
        print(f"{j:4}", end="")
    print()
    print("     " + "_" * (4 * size))

    # Вывод таблицы
    for i in range(1, size + 1):
        print(f"{i:3} |", end="")
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()


if __name__ == "__main__":
    multiplication_table()
