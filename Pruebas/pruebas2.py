import time
s = {1, 2, 3, 4, 5}
t = s.copy()
s.remove(2)
print(t)
print(s)
t = s
print(t)


listA = [1, 2, 3, 4, 5, 6, 7]
listB = [1, 2, 7, 8, 9]

inicio1 = time.time_ns()
listSub = [elem for elem in listA if elem not in listB]
for elem in listSub:
    print(elem)
final1 = time.time_ns() - inicio1

inicio2 = time.time_ns()
for elem in listA:
    if elem not in listB:
        print(elem)
final2 = time.time_ns() - inicio2

print("tiempo 1: " + str(final1))
print("tiempo 2: " + str(final2))

listA.remove(3)
listA.append(3)
print(listA)

