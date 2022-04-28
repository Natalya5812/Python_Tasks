# 30. Вычислить число π c заданной точностью d
# 	Пример: при d = 0.001,  = 3.141. 10-1d≤10-10

import os
import random
import math
math.pi
os.system("cls")

deg = random.randint (1,10)
d = 10**-deg
print (f'При заданной точности {d}, π = {round (math.pi,deg)}')

