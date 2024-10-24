from structure import solution
import random


def constructrand(inst):
    sol = solution.createEmptySolution(inst)
    lista = random.sample(range(inst['n']), inst['p'])
    sol['sol'] = set(lista)
    sol['of'] = solution.evaluate(sol)
    return sol
