from structure import instance
from algorithms import tabu
from constructives import greedy

inst = instance.readInstance("../instances/MDG-a_1_n500_m25.txt")
inst2 = inst.copy()
inst['p'] = 3
inst2['p'] = inst['p']
inst['p'] = 10

print(inst2['p'])
print(inst['p'])

sol = greedy.construct(inst)
print(sol['of'])
print(sol['sol'])
sol = tabu.execute(inst, 5, 15)
print(sol['sol'])

