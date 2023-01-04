# 种群大小
population_size = 8
# 父种群的编码列表
parent1 = []
parent2 = []
# 子种群的编码列表
children1 = []
children2 = []
# 父种群每个个体的适应度
parent_fitness1 = []
parent_fitness2 = []
# 子种群每个个体的适应度
children_fitness1 = []
children_fitness2 = []


# 初始化个体
def initial_individual():

    # 个体的编码
    individual = []
    # 8个编码
    for i in range(8):
        a = random.randint(0, 7)
        individual.append(a)
    # 计算生成的个体的适应度
    fit_score = update_fitness_score(individual)
    # 加入到种群中

    parent_fitness1.append(fit_score)
    parent1.append(individual)

    # 个体的编码
    individual = []
    # 8个编码
    for i in range(8):
        a = random.randint(0, 7)
        individual.append(a)
    # 计算生成的个体的适应度
    fit_score = update_fitness_score(individual)
    # 加入到种群中

    parent_fitness2.append(fit_score)
    parent2.append(individual)
    return


# 交叉产生后代
def hybridization():
    # 选择两个父本
    first = select1()
    second = select1()
    selected_parents = copy.deepcopy([parent1[first], parent1[second]])
    # 交换从pos1到pos2的基因
    pos1 = random.randint(0, 6)
    pos2 = random.randint(0, 6)
    # 保证pos1 <= pos2
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    # 交叉
    tmp = selected_parents[0][pos1:pos2]
    selected_parents[0][pos1:pos2] = selected_parents[1][pos1:pos2]
    selected_parents[1][pos1:pos2] = tmp
    # 一定的概率发生变异,假设概率为0.5
    may = random.random()
    if may > 0.5:
        selected_parents[0] = mutation(selected_parents[0])
    may = random.random()
    if may > 0.5:
        selected_parents[1] = mutation(selected_parents[1])
    # 更新适应度
    first_fit = update_fitness_score(selected_parents[0])
    second_fit = update_fitness_score(selected_parents[1])

    # 加入到子代中
    children1.append(selected_parents[0])
    children1.append(selected_parents[1])
    children_fitness1.append(first_fit)
    children_fitness1.append(second_fit)

    # 选择两个父本
    first = select2()
    second = select2()
    selected_parents = copy.deepcopy([parent2[first], parent2[second]])
    # 交换从pos1到pos2的基因
    pos1 = random.randint(0, 6)
    pos2 = random.randint(0, 6)
    # 保证pos1 <= pos2
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    # 交叉
    tmp = selected_parents[0][pos1:pos2]
    selected_parents[0][pos1:pos2] = selected_parents[1][pos1:pos2]
    selected_parents[1][pos1:pos2] = tmp
    # 一定的概率发生变异,假设概率为0.5
    may = random.random()
    if may > 0.5:
        selected_parents[0] = mutation(selected_parents[0])
    may = random.random()
    if may > 0.5:
        selected_parents[1] = mutation(selected_parents[1])
    # 更新适应度
    first_fit = update_fitness_score(selected_parents[0])
    second_fit = update_fitness_score(selected_parents[1])

    # 加入到子代中
    children2.append(selected_parents[0])
    children2.append(selected_parents[1])
    children_fitness2.append(first_fit)
    children_fitness2.append(second_fit)
    return


while t < 100:
    # 父种群的编码列表
    parent1 = []
    parent2 = []
    # 子种群的编码列表
    children1 = []
    children2 = []
    # 父种群每个个体的适应度
    parent_fitness1 = []
    parent_fitness2 = []
    # 子种群每个个体的适应度
    children_fitness1 = []
    children_fitness2 = []
    # 初始化个体
    t = t + 1
    cc.append(main())