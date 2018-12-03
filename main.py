from turtle import *
from random import *


def hex(length):
    """Function draws a hexagon outline."""
    end_fill()
    lt(120)
    fd(length)
    rt(60)
    fd(length)
    lt(30)
    rt(90)
    end_fill()


def hexagon(x, y, size_length, number, light_1, light_2):
    """The function that draws a regular hexagon based on the width."""
    up()
    goto(x, y)
    speed(0)
    down()
    rt(90)
    for count in range(number):
        if count % 2 == 0:
            begin_fill()
            color(light_1, light_2)
            for _ in range(6):
                forward(size_length)
                lt(60)
            hex(size_length)
        else:
            begin_fill()
            color(light_2, light_1)
            for _ in range(6):
                forward(size_length)
                lt(60)
            hex(size_length)
    up()
    lt(90)


def mosaic(number, length, color_one, color_two):
    """The function that performs surface tiling with hexagons."""
    colors = ['powderblue', 'darkkhaki', 'antiquewhite',
              'linen', 'beige', 'lightgray', 'azure', 'oldlace',
              'peachpuff', 'teal', 'peru', 'lightpink', 'slateblue',
              'rosybrown', 'olive']
    backcolor = choice(colors)
    Screen().bgcolor(backcolor)
    for p in range(1, number + 1):
        if p == 3 or p == 7 or p == 11 or p == 15 or p == 19:
            hexagon(-300, 300 - 1.5 * length * p, length,
                    number, color_one, color_two)
        elif p == 4 or p == 8 or p == 12 or p == 16 or p == 20:
            hexagon(-300 - ((3 ** (1 / 2)) * length) / 2,
                    300 - 1.5 * length * p, length,
                    number, color_one, color_two)
        elif p % 2 != 0:
            hexagon(-300, 300 - 1.5 * length * p,
                    length, number, color_two, color_one)
        else:
            hexagon(-300 - ((3 ** (1 / 2)) * length) / 2,
                    300 - 1.5 * length * p, length,
                    number, color_two, color_one)



def colors():
    """The function that adapts the name of the color for the program."""
    our_color = str(input("Введите первый цвет: "))
    new_color = ''
    our_color_1 = ' ' + our_color.lower() + ' '
    text = ' черный желтый красный зеленый синий оранжевый' \
                             ' пурпурный розовый зелёный жёлтый чёрный '
    while our_color_1 not in text:
        our_color = input("'{}' не является верным значением. Пожалуйста,"
                          " повторите попытку: ".format(our_color))
        our_color_1 = ' ' + our_color.lower() + ' '

    else:
        if our_color_1 in " желтый жёлтый ":
            new_color = "yellow"
        elif our_color_1 in " зеленый зелёный ":
            new_color = "green"
        elif our_color_1 in " красный ":
            new_color = "red"
        elif our_color_1 in " синий ":
            new_color = "navy"
        elif our_color_1 in " оранжевый ":
            new_color = "coral"
        elif our_color_1 in " пурпурный ":
            new_color = "mediumvioletred"
        elif our_color_1 in " розовый ":
            new_color = "hotpink"
        elif our_color_1 in " черный чёрный ":
            new_color = "black"
        return new_color


def number():
    """The function that "talks to the user"."""
    num = input("Введите количество шестиугольников: ")
    while num.isdigit() == False or int(num) > 20 or int(num) < 4:
        num = input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
    return int(num)


def main():
    """Main function performing all operations."""
    print('Выберете цвет из палитры: желтый, красный, '
          'синий, зеленый, розовый, пурпурный, оранжевый, черный.')
    color_1 = colors()
    color_2 = colors()
    number_hex = number()
    side_length = (500 / number_hex) / (3 ** (1 / 2))
    mosaic(number_hex, side_length, color_1, color_2)
    mainloop()


if __name__ == '__main__':
    main()
