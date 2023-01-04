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
