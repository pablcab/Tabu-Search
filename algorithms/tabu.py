from structure import solution, instance
import random
from constructives import greedy, crandom
from movestrategy import msfirstimprove, msbestimprove


def execute(inst, iters, tenure):
    # random.seed(1309)
    # print("Tiempo de ejecución: " + str(t_ex))
    # sol = greedy.construct(inst)
    sol = crandom.constructrand(inst)
    # i = msfirstimprove.improve(sol, t_ex, tenure)
    msbestimprove.improve(sol, iters, tenure)
    # print("Número de cambios: " + str(i))
    print("\tMejor valor: " + str(sol['of']))
    return sol
