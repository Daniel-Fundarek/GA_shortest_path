import tkinter

import numpy


def draw_point(_canvas, _point, size):
    offset_x = 5
    y = _point[0]
    x = _point[1]
    x1 = x - size + offset_x
    y1 = y - size
    x2 = x + size + offset_x
    y2 = y + size
    _canvas.create_oval(x1, y1, x2, y2)


def draw_points(_area, _row, _c):
    for curr_row in range(_row):
        for curr_column in range(_c):
            position = _area[curr_row][curr_column]
            draw_point(canvas, position, 2)


r = 20
c = 100


def create_map(_row, _column):
    area = numpy.zeros((_row, _column), list)
    for curr_row in range(_row):
        for curr_column in range(_column):
            area[curr_row][curr_column] = [curr_row * 30, curr_column * 10]
    print(area)
    return area


area = create_map(r, c)
obsticle = [(190, 0), (150, 40)]
top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg="white", height=r * 30, width=c * 10)

canvas.pack()
top.mainloop()
