import random, time
from structure import solution

def improve(sol, t_ex, tenure):
    selected, unselected = createSelectedUnselected(sol)
    random.shuffle(unselected)
    tabulist = createTabuList(tenure)
    inicio = time.time()
    bestof = sol['of']
    bestsol = sol['sol'].copy()
    cont = 0
    paso_sol = 0
    paso_ten = 0
    i = 0
    while cont < t_ex:
        if paso_sol == sol['instance']['p']:
            paso_sol = 0
        if paso_ten == tenure:
            paso_ten = 0
        bestofvar = -1
        s = selected[paso_sol]
        ds = solution.distanceToSolution(sol, s)
        for u in unselected:
            if u not in tabulist:
                du = solution.distanceToSolution(sol, u, s)
                if du > ds:
                    bestofvar = du
                    bestu = u
                    break
                elif du > bestofvar:
                    bestu = u
                    bestofvar = du
        solution.removeFromSolution(sol, s, ds)
        solution.addToSolution(sol, bestu, bestofvar)
        selected[paso_sol] = bestu
        tabulist[paso_ten] = s
        unselected.remove(bestu)
        unselected.append(s)
        if sol['of'] > bestof:
            bestof = sol['of']
            bestsol = sol['sol'].copy()
        paso_sol += 1
        paso_ten += 1
        i += 1
        cont = time.time() - inicio
    sol['of'] = bestof
    sol['sol'] = bestsol
    return i


# def updatelists(selected, unselected, tabulist, paso_sol, paso_ten):



def createTabuList(tenure):
    tabulist = [-1]*tenure
    return tabulist


def createSelectedUnselected(sol):
    selected = []
    unselected = []
    n = sol['instance']['n']
    for v in range(n):
        if solution.contains(sol, v):
            selected.append(v)
        else:
            unselected.append(v)
    return selected, unselected
