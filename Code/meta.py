import random
import pygal

matrix_size = 10
chance_to_mutate = 0.1
graded_retain_percent = 0.2
chance_retain_nongrated = 0.05
population_count = 10000
generation_count_max = 1000
graded_individual_retain_count = int(population_count * graded_retain_percent)


def get_random_town(matrix):
    """ Return a random town from the matrix. """
    town = random.randint(1, len(matrix)-1)
    return town, matrix[town]


def get_random_individual(matrix):
    """ Create a new random individual. """
    individual = [0]
    individual_list = [matrix[0]]
    for _ in range(len(matrix)-1):
        town, neighbors = get_random_town(matrix)
        individual.append(town)
        individual_list.append(neighbors)
    individual.append(0)
    individual_list.append(matrix[0])
    return individual, individual_list


def get_random_population(matrix):
    """ Create a new random population, made of 'population_count' individual. """
    population = []
    population_list = []
    for _ in range(population_count):
        individual, individual_list = get_random_individual(matrix)
        population.append(individual)
        population_list.append(individual_list)
    return population, population_list


def neighbors_check(individual, individual_list):
    """ Check if all the cities from an individual are actually neighbors """
    fitness = 0
    for elem in individual:
        if individual.count(elem) > 1 and elem != 0:
            return False, fitness

    for i in range(len(individual_list)):
        if individual[i] == 0:
            continue
        else:
            if individual_list[i][individual[i+1]] == 0:
                return False, fitness
            else:
                fitness += individual_list[i][individual[i+1]]
                continue
    return True, fitness


def grade_population(population, population_list):
    """ Grade the population. Return a list of tuple (individual, fitness) sorted from most graded to less graded. """
    graded_individual = []
    for i in range(len(population_list)):
        state, fitness = neighbors_check(population[i], population_list[i])
        if state:
            graded_individual.append([population[i], population_list[i], fitness])
    return sorted(graded_individual, key=lambda x: x[2], reverse=True)


def evolve_population(population, population_list, best_fitness, matrix):
    """ Make the given population evolving to his next generation. """
    length_of_cycle = len(matrix)
    middle_length_of_cycle = length_of_cycle // 2

    # Get individual sorted by grade (top first), the average grade and the solution (if any)
    raw_graded_population = grade_population(population, population_list)
    average_grade = 0
    graded_population = []
    for individual, individual_list, fitness in raw_graded_population:
        average_grade += fitness
        graded_population.append([individual, individual_list])
        if best_fitness == 0 or fitness < best_fitness:
            best_fitness = fitness
    average_grade /= population_count

    # Filter the top graded individuals
    parents = [graded_population[-1][0]]
    parents_list = [graded_population[-1][1]]

    # Randomly add other individuals to promote genetic diversity
    for individual, individual_list in graded_population[:-1]:
        if random.random() < chance_retain_nongrated:
            parents.append(individual)
            parents_list.append(individual_list)

    # Mutate some individuals
    for i in range(len(parents)):
        if random.random() < chance_to_mutate:
            place_to_modify = int(random.random() * length_of_cycle)
            parents[i][place_to_modify], parents_list[i][place_to_modify] = get_random_town(matrix)

    # Crossover parents to create children
    parents_len = len(parents)
    desired_len = population_count - parents_len
    children = []
    children_list = []
    while len(children) < desired_len:
        father_rand = random.randint(0, len(parents)-1)
        father = parents[father_rand]
        father_list = parents_list[father_rand]
        mother_rand = random.randint(0, len(parents)-1)
        mother = parents[mother_rand]
        mother_list = parents_list[mother_rand]
        if True:  # father != mother:
            child = father[:middle_length_of_cycle] + mother[middle_length_of_cycle:]
            child_list = father_list[:middle_length_of_cycle] + mother_list[middle_length_of_cycle:]
            children.append(child)
            children_list.append(child_list)

    # The next generation is ready
    parents.extend(children)
    parents_list.extend(children_list)
    return parents, parents_list, average_grade, best_fitness


def random_adjacency_matrix(n):
    matrix = [[random.randint(0, 15) for _ in range(n)] for _ in range(n)]

    # No vertex connects to itself
    for i in range(n):
        matrix[i][i] = 0

    # If i is connected to j, j is connected to i
    for i in range(n):
        for j in range(n):
            matrix[j][i] = matrix[i][j]

    return matrix


def main():
    """ Main function. """

    for _ in range(4):
        print(" ")
        matrix = random_adjacency_matrix(matrix_size)
        for i in range(len(matrix)):
            print(matrix[i])
        population, population_list = get_random_population(matrix)
        print(" ")

        # Make the population evolve
        i = 0
        log_avg = []
        best_fitness = 0
        while i < generation_count_max:
            parents, parents_list, average_grade, best_fitness =\
                evolve_population(population, population_list, best_fitness, matrix)
            for i in range(len(parents)):
                population = parents[i]
                population_list = parents_list[i]
            if i & 1 == 1:
                print('Current grade: %.2f' % average_grade, '(%d generation)' % i)
            if i & 1 == 1:
                log_avg.append(average_grade)
            i += 1

        line_chart = pygal.Line(show_dots=False, show_legend=False)
        line_chart.title = 'Fitness evolution'
        line_chart.x_title = 'Generations'
        line_chart.y_title = 'Fitness'
        line_chart.add('Fitness', log_avg)
        line_chart.render_to_file('bar_chart.svg')

        # Print the solution
        print('The best path : {path} , with a {travel} km travel.'.format(path=population, travel=best_fitness))
        print('Total of generation : %d' % i)


if __name__ == '__main__':
    main()
