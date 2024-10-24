from structure import instance
from algorithms import tabu
from constructives import greedy, crandom
import time

inst = instance.readInstance("instances/MDG-a_2_n500_m25.txt")

# sol = greedy.construct(inst)
for _ in range(1):
    sol = crandom.constructrand(inst)
    print(sol['of'])
    # print(sol['sol'])
    inicio = time.time()
    sol = tabu.execute(inst, 1000, 6)
    final = time.time() - inicio
    print("Tiempo: " + str(final))
    # print(sol['sol'])
