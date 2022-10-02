import random
from math import sqrt
import copy

def generate_chromosome(num_genes):
    chromosome = []
    for i in range(num_genes):
        chromosome.append(random.randint(0, 19))
    chromosome[0] = 10
    chromosome[99] = 10
    #print(chromosome)
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
        chromosome_indexes = random.sample(range(1, len(_population[0]) - 1), genes_amount)
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


def calculate_fitness(population, area):
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
            c = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
            length += c
        fit.append(length)
    return fit


def sort(population, fitness):
    sortedList = sorted(zip(fitness,population))
    p =[]
    f = []
    p , f = zip(*sortedList)
    return list(p),list(f)


# sel best always sort- to save computation sort always on the top just once
def select_best(population, fitness, num):
    new_pop = []
    new_pop = population[:num]
    new_pop = copy.deepcopy(new_pop)
    return new_pop#, fitness[::num]


def select_random(population, fitness, num):
    population_indexes = random.sample(range(0, len(population)), num)
    p = []
    f = []
    for i in population_indexes:

        p.append(population[i])
        f.append(fitness[i])
        new_pop = copy.deepcopy(p)
    return new_pop#, f


def select_tourn(population, fitness, num):
    pass