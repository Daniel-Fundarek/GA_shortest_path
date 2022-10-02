import tkinter
import numpy
import random
import sys

import numpy as np

import GeneticAlgorithm
import matplotlib as mpl
import matplotlib.pyplot as plt


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


def create_obstacles(c, step, num):
    # obstacle generation
    _obstacles = []
    for i in range(0, c * step, step * 2):
        x = i
        x1 = i + 10  # random.randrange(10, 80, 10)
        y = random.choice(ySelection)
        y1 = random.choice(ySelection)
        _obstacles.append([[x, y], [x1, y1]])

    return _obstacles
    ###########


def create_map(_row, _column):
    area = []
    counter = 0
    for curr_row in range(_row):
        for curr_column in range(_column):
            area.append([curr_row * step, curr_column * step])
            counter += 1

    # print(area)
    return area


def draw_obstacles(canvas, _obstacles):
    for _obstacle in _obstacles:
        x0 = _obstacle[0][0] - offset
        y0 = _obstacle[0][1] + offset
        x1 = _obstacle[1][0] - offset
        y1 = _obstacle[1][1] + offset
        canvas.create_line(x0, y0, x1, y1)


def draw_lines(canvas, _chromosome, area):
    for index in range(1, len(_chromosome)):
        point0 = area[_chromosome[index - 1] * 100 + index - 1]
        # print((_chromosome[index]) * 100 + index,_chromosome[index - 1],index)
        point1 = area[(_chromosome[index]) * 100 + index]
        # print(point0, point1)
        x0 = point0[1] + offset
        y0 = point0[0] + offset
        x1 = point1[1] + offset
        y1 = point1[0] + offset
        canvas.create_line(x0, y0, x1, y1, fill='green')


# obstacle = [[190, 0], [130, 40]]
# canvas.create_line(obstacle[0][0] - offset, obstacle[0][1] + offset, obstacle[1][0] + offset, obstacle[1][1] - offset)

# main
r = 20
c = 100
step = 10
generation = 29000
ga = GeneticAlgorithm
ySelection = [i for i in range(10, r * step, step)]
obstacles = create_obstacles(c, step, 100)
# chromosome = ga.generate_chromosome(100)
population = []
population = ga.generate_population(100, 100)

# print('population:', population)
# population = ga.mutate(population,0.6,50)
# population = ga.cross(population,0.6,50)
# population = ga.additive_mutate(population, 0.6, 50, [-3, 3])
# print('population:', population)
top = tkinter.Tk()
area = create_map(r, c)  # x -> <0,190> step 10 y -> <0,990
offset = 5
fitness = []
evolution = []
multiplier = 1 / generation
for i in range(generation):
    fitness = ga.calculate_fitness(population, area, obstacles)
    newPop = []
    work1 = []
    work2 = []
    work3 = []
    work4 = []
    work5 = []
    work6 = []
    work7 = []
    [fitness, population] = ga.sort(population, fitness)
    evolution.append(min(fitness))
    newPop = ga.select_best(population, fitness, 3)
    newPop.extend(ga.select_random(population, fitness, 7))

    work1 = ga.select_best(population, fitness, 5)
    # print(work1)
    work1.extend(ga.select_random(population, fitness, 18))

    work2 = ga.select_random(population, fitness, 15)
    work3 = ga.select_best(population, fitness, 2)

    work1 = ga.additive_mutate(work1, i * multiplier, 3, [-3, 3])
    work2 = ga.cross(work2, 0.2, 50)
    work3 = ga.mutate(work3, 0.15, 3)

    work4 = ga.select_random(population, fitness, 14)
    work4.extend(ga.select_best(population, fitness, 1))

    work5 = ga.select_random(population, fitness, 13)
    work5.extend(ga.select_best(population, fitness, 1))

    work6 = ga.select_best(population, fitness, 1)

    work4 = ga.additive_mutate(work4, 0.2, 2, [-1, 1])
    work5 = ga.invert(work5, 0.3)
    work6 = ga.mutate(work6, i * multiplier, random.randint(1, 98))
    work7 = ga.generate_population(100, 20)
    newPop.extend(work1)
    newPop.extend(work2)
    newPop.extend(work3)
    newPop.extend(work4)
    newPop.extend(work5)
    newPop.extend(work6)
    newPop.extend(work7)
    population = newPop
    print(f'Evolution number:{i} fitness: {evolution[i]} ')
# drawing
print(evolution)
'''
x = [i for i in range(500)]
fig, ax = plt.subplots()
ax.plot(x,evolution)
fig.savefig("evolution.pdf")
fig.show()

# print('obstacles ', obstacles)

''''''
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()

'''
canvas = tkinter.Canvas(top, bg="white", height=r * step + 50, width=c * step + 50)
draw_points(canvas, area)
draw_obstacles(canvas, obstacles)
draw_lines(canvas, population[0], area)
canvas.pack()
top.mainloop()
