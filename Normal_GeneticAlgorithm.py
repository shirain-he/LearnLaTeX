# 导入测试所用到的库
mport numpy as np
import copy
import matplotlib.pyplot as plt
import seaborn as sns

# 导入我们需要用到的遗传相关函数
from Genetic_Algorithm_N_Queen import fitness_function
from Genetic_Algorithm_N_Queen import softmax, mutation
from Genetic_Algorithm_N_Queen import GA

# 调用种群数为100的遗传函数GA
GeneticDict, Queen = GA(size = 100)

# 测试结果
-----------------------------------
Generation :  0
current max fitnessvalue: 24
Generation :  1
current max fitnessvalue: 25
Generation :  2
current max fitnessvalue: 26
Generation :  3
current max fitnessvalue: 25
Generation :  4
current max fitnessvalue: 24
Generation :  5
current max fitnessvalue: 26

--中间遗传过程省略--

Generation :  1769
current max fitnessvalue: 25
Generation :  1770
Find Target!
[6 4 2 0 5 7 1 3]

总遗传代数：1770代
计算总耗时： 15.8s