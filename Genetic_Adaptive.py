# 更新适应度函数
def update_fitness_score(individual):
    value = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if individual[i] != individual[j]:
                x = j - i
                y = abs(individual[i] - individual[j])
                if x != y:
                    value += 1
    return value


# 交叉产生后代
def hybridization(bianyi1):
    # 选择两个父本
    first = select()
    second = select()
    selected_parents = copy.deepcopy([parent[first], parent[second]])
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
    if may > bianyi1:
        selected_parents[0] = mutation(selected_parents[0])
    may = random.random()
    if may > bianyi1:
        selected_parents[1] = mutation(selected_parents[1])
    # 更新适应度
    first_fit = update_fitness_score(selected_parents[0])
    second_fit = update_fitness_score(selected_parents[1])

    # 加入到子代中
    children.append(selected_parents[0])
    children.append(selected_parents[1])
    children_fitness.append(first_fit)
    children_fitness.append(second_fit)
    return