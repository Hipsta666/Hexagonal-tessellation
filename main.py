from turtle import *


# Branch develop.
# Branch for merging working branches.



# Branch feature-hexagon.
# Branch for writing a function that draws a regular hexagon based on the width.
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
        else:
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
    up()
    left(90)


# Branch feature-tiling.
# Branch for writing a function that performs surface tiling with hexagons.
# Further function
number_of_hexagons = int(input())
side_length = (500 / number_of_hexagons) / (3 ** (1 / 2))
for p in range(1, number_of_hexagons + 1):
    if p == 3 or p == 7 or p == 11 or p == 15 or p == 19:
        hexagon(-250, 250 - 1.5 * side_length * p, side_length,
                number_of_hexagons, "green", "red")
    elif p == 4 or p == 8 or p == 12 or p == 16 or p == 20:
        hexagon(-250 - ((3 ** (1 / 2)) * side_length) / 2,
                250 - 1.5 * side_length * p, side_length,
                number_of_hexagons, "green", "red")
    elif p % 2 != 0:
        hexagon(-250, 250 - 1.5 * side_length * p,
                side_length, number_of_hexagons, "red", "green")
    else:
        hexagon(-250 - ((3 ** (1 / 2)) * side_length) / 2,
                250 - 1.5 * side_length * p, side_length,
                number_of_hexagons, "red", "green")
mainloop()


# Branch feature-communication.
# Branch for writing a function that "talks to the user".

