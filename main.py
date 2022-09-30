import tkinter
import numpy
import random
import sys


def draw_point(_canvas, _point, size):
    size /= 2

    y = _point[0]
    x = _point[1]
    x1 = x - size + offset
    y1 = y - size + offset
    x2 = x + size + offset
    y2 = y + size + offset
    _canvas.create_oval(x1, y1, x2, y2)


def draw_points(_canvas, _area):
    for index in range(len(_area)):

        position = _area[index]
        # print(position)
        draw_point(_canvas, position, 2)


def create_map(_row, _column):
    area = []
    counter = 0
    for curr_row in range(_row):
        for curr_column in range(_column):
            area.append([curr_row * step, curr_column * step])
            counter += 1
    #  print(area)
    return area


def draw_obstacles(canvas, obstacle):
    pass


# obstacle = [[190, 0], [130, 40]]
# canvas.create_line(obstacle[0][0] - offset, obstacle[0][1] + offset, obstacle[1][0] + offset, obstacle[1][1] - offset)


r = 20
c = 100
step = 10
ySelection = [i for i in range(0, r * step, step)]
xSelection = [i for i in range(0, c * step, step)]
obstacles = []
# obstacle generation
for i in range(10):
    y = random.choice(ySelection)
    x = random.choice(xSelection)
    y1 = random.choice(ySelection)
    x1 = random.choice(xSelection)
    obstacles.append([[x, y], [x1, y1]])
###########


# print(ySelection, xSelection)
top = tkinter.Tk()
area = create_map(r, c)  # x -> <0,190> step 10 y -> <0,990
offset = 5

canvas = tkinter.Canvas(top, bg="white", height=r * step + 50, width=c * step + 50)
draw_points(canvas, area)
canvas.pack()
top.mainloop()
print('obstacles ', obstacles)
