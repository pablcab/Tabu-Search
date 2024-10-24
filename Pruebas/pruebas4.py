import time

inicio = time.time_ns()
l =[]
for i in range(100):
    l.append(i)
inicio = time.time_ns()
T = 98 in l
final1 = time.time_ns() - inicio

inicio = time.time_ns()
s = set()
for i in range(100):
    s.add(i)
inicio = time.time_ns()
T = 98 in s
final2 = time.time_ns() - inicio

print("listas: " + str(final1))
print("sets: " + str(final2))
