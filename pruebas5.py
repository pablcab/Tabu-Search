from constructives import greedy
from structure import solution, instance

inst = instance.readInstance("instances/MDG-a_1_n500_m25.txt")
sol = greedy.construct(inst)

bestsol = sol['sol'].copy()
bestsol.remove(440)
sol['sol'].remove(0)
print(bestsol)
print(sol['sol'])

