# Возвращает список простых чисел до limit включительно.
def primes_up_to(limit: int) -> list[int]:
    primes = []

    # Перебираем все числа от 2 до limit
    for num in range(2, limit + 1):
        is_prime = True

        # Проверяем делители от 2 до корня из num
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


if __name__ == "__main__":
    result = primes_up_to(100)
    print(f"Простые числа до 100: {result}")
