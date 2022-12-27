import numpy as np
import copy


# 普通选择算子遗传算法：适应度函数
def fitness_function(individual):
    value = 0
    for i in range(7):
        for j in range(i+1, 8, 1):
            if individual[i] != individual[j]:
                x_distance = np.abs(individual[j] - individual[i])
                y_distance = j - i
                if x_distance != y_distance:
                    value += 1
    return value


# 普通选择算子遗传算法：把适应度函数转化为概率分布
def softmax(input):
    input = np.array(input, dtype=np.float)
    input = np.exp(input)
    output = input / input.sum()
    return output


# 随机变异
def mutation(individual, prob=0.1):
    p = np.random.rand(8)
    individual[p > prob] = np.random.choice(range(8), 8)[p > prob]

    return individual


# Genetic Algorithm
def GA(size=4):
    # 默认种群大小为4，可以多试几个，效果不一样
    size = size
    num_generation = 0
    population = []
    Generation_Fitness = {}
    for i in range(size):
        population.append(np.random.choice(range(8), 8))
    while (True):
        fitness_list = []
        selection = []
        print("Generation : ", num_generation)

        for individual in population:
            fitness_value = fitness_function(individual)
            if fitness_value == 28:
                print("Find Target!")
                print(individual)
                Generation_Fitness[num_generation] = 28
                return Generation_Fitness, individual
            fitness_list.append(fitness_value)
        Generation_Fitness[num_generation] = max(fitness_list)
        print("current max fitnessvalue:" + str(max(fitness_list)))

        # Selection is Here自然选择在这里
        prob = softmax(fitness_list)
        select_id = np.random.choice(range(size), size, replace=True, p=prob)
        for idx in select_id:
            selection.append(population[idx])
        num_pair = int(size/2)
        position = np.random.choice(range(1, 7, 1), num_pair, replace=True)

        # Crossover is Here基因片段的交叉互换在这里
        for i in range(0, size, 2):
            start = position[int(i/2)]
            tempa = copy.deepcopy(selection[i][start:])
            tempb = copy.deepcopy(selection[i+1][start:])
            selection[i][start:] = tempb
            selection[i+1][start:] = tempa

        # Mutation is Here变异在这里
        for i in range(size):
            selection[i] = copy.deepcopy(mutation(selection[i], prob=0.8))
        population = selection
        num_generation += 1
