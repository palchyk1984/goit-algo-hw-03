import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order-1, size/3)
            t.left(angle)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    # Налаштування для turtle
    window = turtle.Screen()
    window.bgcolor("sky blue")

    flake = turtle.Turtle()
    flake.speed(0)  # Найвища швидкість

    # Відкриваємо діалогове вікно для вводу рівня рекурсії
    order = turtle.textinput("Введіть рівень рекурсії", "Будь ласка, введіть рівень рекурсії:")
    if order is not None:  # Перевіряємо, чи користувач ввів число
        order = int(order)
        size = 300  # Довжина сторони трикутника

        flake.penup()
        flake.goto(-size/2, size/3)
        flake.pendown()

        koch_snowflake(flake, order, size)

        flake.hideturtle()
    else:
        print("Рівень рекурсії не було введено.")

    window.mainloop()

if __name__ == "__main__":
    main()
