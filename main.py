from turtle import *

# The function that draws a regular hexagon based on the width.
def hexagon(x, y, size_length, number, light_1, light_2):
    up()
    goto(x, y)
    speed(0)
    down()
    right(90)
    pencolor("black")
    for count in range(number):
        if count % 2 == 0:
            begin_fill()
            color("black", light_2)
            for _ in range(6):
                forward(size_length)
                left(60)
            end_fill()
            left(120)
            fd(size_length)
            rt(60)
            fd(size_length)
            left(30)
            right(90)
            end_fill()
        else:
            begin_fill()
            color("black", light_1)
            for _ in range(6):
                forward(size_length)
                left(60)
            end_fill()
            left(120)
            fd(size_length)
            rt(60)
            fd(size_length)
            left(30)
            right(90)
            end_fill()
    up()
    left(90)


# The function that performs surface tiling with hexagons.
# Further function
def mosaic(number, length, color_one, color_two):
    for p in range(1, number + 1):
        if p == 3 or p == 7 or p == 11 or p == 15 or p == 19:
            hexagon(-250, 250 - 1.5 * length * p, length,
                    number, color_one, color_two)
        elif p == 4 or p == 8 or p == 12 or p == 16 or p == 20:
            hexagon(-250 - ((3 ** (1 / 2)) * length) / 2,
                    250 - 1.5 * length * p, length,
                    number, color_one, color_two)
        elif p % 2 != 0:
            hexagon(-250, 250 - 1.5 * length * p,
                    length, number, color_two, color_one)
        else:
            hexagon(-250 - ((3 ** (1 / 2)) * length) / 2,
                    250 - 1.5 * length * p, length,
                    number, color_two, color_one)


# The function that adapts the name of the text for the program.


# The function that "talks to the user".


# Test
first_color = str(input("Введите первый цвет:"))
second_color = str(input("Введите второй цвет:"))
number_of_hexagons = int(input())
side_length = (500 / number_of_hexagons) / (3 ** (1 / 2))
mosaic(number_of_hexagons, side_length, first_color, second_color)
mainloop()
