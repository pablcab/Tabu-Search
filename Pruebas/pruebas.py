import time
inicio = time.time()
cont = time.time() - inicio
i = 0
while cont < 10:
    i += 1
    cont = time.time() - inicio
print(i)
print(cont)

inicio = time.time()
i = 0
while i < 28177561:
    i += 1
cont = time.time() - inicio
print(cont)
