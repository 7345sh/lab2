import matplotlib.pyplot as p


# Построение графика y = x^2
def plot_parabola() -> None:
    # Задаём значения x от -10 до 10
    x = list(range(-10, 11))
    # Вычисляем значения y
    y = [i ** 2 for i in x]

    # Настройка графика
    p.figure(figsize=(8, 6))
    p.plot(x, y, color="blue", linewidth=2, label="y = x^2")
    p.title("График функции y = x^2")
    p.xlabel("x")
    p.ylabel("y")
    p.axhline(0, color="black", linewidth=0.5)
    p.axvline(0, color="black", linewidth=0.5)
    p.grid(True, linestyle="--", alpha=0.5)
    p.legend()

    # Показать окно
    p.show()

    # Сохранить картинку
    p.savefig("plot.png")


if __name__ == "__main__":
    plot_parabola()
