from structure import solution

def improve(sol, iters, tenure):
    selected, unselected, tabulist = createlists(sol)
    bestof = sol['of']
    bestsol = sol['sol'].copy()
    paso_sol = 0
    for _ in range(iters):
        if paso_sol == sol['instance']['p']:
            paso_sol = 0
        bestofvar = -1
        s = selected[paso_sol]
        ds = solution.distanceToSolution(sol, s)
        bestu = s
        for u in unselected:
            if u not in tabulist:
                du = solution.distanceToSolution(sol, u, s)
                if du > bestofvar:
                    bestu = u
                    bestofvar = du
        solution.removeFromSolution(sol, s, ds)
        solution.addToSolution(sol, bestu, bestofvar)
        selected[paso_sol] = bestu
        if len(tabulist) == tenure:
            tabulist.remove(tabulist[0])
        tabulist.append(s)
        unselected.remove(bestu)
        unselected.append(s)
        if sol['of'] > bestof:
            bestof = sol['of']
            bestsol = set(selected)
        paso_sol += 1
    sol['of'] = bestof
    sol['sol'] = bestsol


def createlists(sol):
    selected = []
    unselected = []
    tabulist = []
    n = sol['instance']['n']
    for v in range(n):
        if solution.contains(sol, v):
            selected.append(v)
        else:
            unselected.append(v)
    return selected, unselected, tabulist
