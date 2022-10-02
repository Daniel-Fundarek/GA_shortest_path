import random
from math import sqrt
import copy
from shapely.geometry import LineString


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def generate_chromosome(num_genes):
    chromosome = []
    for i in range(num_genes):
        chromosome.append(random.randint(0, 19))
    chromosome[0] = 10
    chromosome[99] = 10
    # print(chromosome)
    return chromosome


def generate_population(genes_number, population_size):
    population = []
    for i in range(population_size):
        population.append(generate_chromosome(genes_number))
    return population


# global mutation
def mutate(population, rate, genes_amount):
    _population = copy.deepcopy(population)
    population_indexes = random.sample(range(0, len(_population)), round(len(_population) * rate))

    for population_index in population_indexes:
        chromosome_indexes = random.sample(range(1, len(_population[population_index]) - 1), genes_amount)
        for chromosome_index in chromosome_indexes:
            _population[population_index][chromosome_index] = random.randint(0, 19)
    return _population


# additive mutation
def additive_mutate(population, rate, genes_amount, limit):
    _population = copy.deepcopy(population)
    population_indexes = random.sample(range(0, len(_population)), round(len(_population) * rate))

    for population_index in population_indexes:
        chromosome_indexes = random.sample(range(1, len(_population[0]) - 1), genes_amount)
        for chromosome_index in chromosome_indexes:
            _population[population_index][chromosome_index] += random.randrange(limit[0], limit[1])
            if not (0 <= _population[population_index][chromosome_index] <= 19):
                _population[population_index][chromosome_index] = 0
    return _population


# crossing 2 chromosommes in pop
def cross(population, rate, genes_amount):
    _population = copy.deepcopy(population)
    population_indexes = random.sample(range(0, len(_population)), round(len(_population) * rate))
    population_indexes1 = random.sample(range(0, len(_population)), round(len(_population) * rate))
    for (population_index, population_index1) in zip(population_indexes, population_indexes1):
        chromosome_indexes = random.sample(range(1, len(_population[0]) - 1), genes_amount)
        for chromosome_index in chromosome_indexes:
            holder = _population[population_index][chromosome_index]
            _population[population_index][chromosome_index] = _population[population_index][chromosome_index]
            _population[population_index1][chromosome_index] = holder

    return _population


def invert(population, rate):
    _population = copy.deepcopy(population)
    population_indexes = []
    population_indexes = random.sample(range(0, len(_population)), round(len(_population) * rate))
    for population_index in population_indexes:
        _population[population_index] = _population[population_index][::-1]
    return _population


def calculate_fitness(population, area, obstacles):
    fit = []
    for _chromosome in population:
        length = 0
        for index in range(1, len(_chromosome)):
            l = len(_chromosome)
            point0 = area[_chromosome[index - 1] * 100 + index - 1]
            point1 = area[_chromosome[index] * 100 + index]
            x0 = point0[1]
            y0 = point0[0]
            x1 = point1[1]
            y1 = point1[0]
            c1 = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
            a = Point(x0, y0)
            b = Point(x1, y1)
            if index % 2 == 0:
                c = Point(obstacles[int(index / 2)][0][0], obstacles[int(index / 2)][0][1])
                d = Point(obstacles[int(index / 2)][1][0], obstacles[int(index / 2)][1][1])
                x, y = get_intersect(a, b, c, d)
                if x != -50:
                    multiplier = min(abs(y - obstacles[int(index / 2)][0][1]), abs(y - obstacles[int(index / 2)][1][1]))
                    length += 4000 * (multiplier +1)
                # print('true')
                else:
                    pass
                # print('false')

            # line = LineString([(x0, y0), (x1, y1)])
            # second_line = LineString(obstacles[index])
            # if line.intersects(second_line):
            #     print('true')
            #     length += 300
            # else:
            #     print('false')
            # for obstacle in obstacles:
            #    second_line = LineString(obstacle)
            #    if(line.intersects(second_line)):
            #       length += 300
            length += c1
        fit.append(length)
    return fit


def get_intersect(A, B, C, D):
    # a1x + b1y = c1
    a1 = B.y - A.y
    b1 = A.x - B.x
    c1 = a1 * (A.x) + b1 * (A.y)

    # a2x + b2y = c2
    a2 = D.y - C.y
    b2 = C.x - D.x
    c2 = a2 * (C.x) + b2 * (C.y)

    # determinant
    det = a1 * b2 - a2 * b1

    # parallel line
    if det != 0:
        x = ((b2 * c1) - (b1 * c2)) / det
        y = ((a1 * c2) - (a2 * c1)) / det
        return (x, y)
    return -100, -100


def sort(population, fitness):
    sortedList = sorted(zip(fitness, population))
    p = []
    f = []
    p, f = zip(*sortedList)
    return list(p), list(f)


# sel best always sort- to save computation sort always on the top just once
def select_best(population, fitness, num):
    new_pop = []
    new_pop = population[:num]
    new_pop = copy.deepcopy(new_pop)
    return new_pop  # , fitness[::num]


def select_random(population, fitness, num):
    population_indexes = random.sample(range(0, len(population)), num)
    p = []
    f = []
    for i in population_indexes:
        p.append(population[i])
        f.append(fitness[i])
        new_pop = copy.deepcopy(p)
    return new_pop  # , f


def select_tourn(population, fitness, num):
    pass
