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


def create_obstacles():
    pass


def create_map(_row, _column):
    area = []
    counter = 0
    for curr_row in range(_row):
        for curr_column in range(_column):
            area.append([curr_row * step, curr_column * step])
            counter += 1

    print(area)
    return area


def draw_obstacles(canvas, obstacles):
    for obstacle in obstacles:
        obstacle[0][0] -= offset
        obstacle[0][1] += offset
        obstacle[1][0] += offset
        obstacle[1][1] -= offset
        canvas.create_line(obstacle)
        # canvas.create_line(obstacle[0][0] - offset, obstacle[0][1] + offset, obstacle[1][0] + offset,obstacle[1][1] - offset)


def draw_lines(canvas, _chromosome, area):

    for index in range(1,len(_chromosome)):
        point0 = area[_chromosome[index-1] * 100 + index-1]
        point1 = area[(_chromosome[index] ) * 100 + index]
        print(point0,point1)
        x0 = point0[1] + offset
        y0 = point0[0] - offset
        x1 = point1[1] + offset
        y1 = point1[0] - offset
        canvas.create_line(x0,y0,x1,y1,fill='green')


def generate_chromosome(num_gennes):
    chromosome = []
    for i in range(num_gennes):
        chromosome.append(random.randint(0, 19))
    chromosome[0] = 10
    chromosome[99] = 10
    print(chromosome)
    return chromosome

# obstacle = [[190, 0], [130, 40]]
# canvas.create_line(obstacle[0][0] - offset, obstacle[0][1] + offset, obstacle[1][0] + offset, obstacle[1][1] - offset)


r = 20
c = 100
step = 10
ySelection = [i for i in range(10, r * step, step)]
xSelection = [i for i in range(0, c * step, step)]
obstacles = []
chromosome = []

# obstacle generation
for i in range(0, c * step, step * 10):
    #   x = random.choice(xSelection)
    # x1 = random.choice(xSelection)
    x = i
    x1 = i + random.randrange(10, 80, 10)
    y = random.choice(ySelection)
    y1 = random.choice(ySelection)
    obstacles.append([[x, y], [x1, y1]])
###########


# print(ySelection, xSelection)
top = tkinter.Tk()
area = create_map(r, c)  # x -> <0,190> step 10 y -> <0,990
chromosome = generate_chromosome(100)
offset = 5

canvas = tkinter.Canvas(top, bg="white", height=r * step + 50, width=c * step + 50)
draw_points(canvas, area)
draw_obstacles(canvas, obstacles)
draw_lines(canvas,chromosome,area)
canvas.pack()
top.mainloop()
print('obstacles ', obstacles)
