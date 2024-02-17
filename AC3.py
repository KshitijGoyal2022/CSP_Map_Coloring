#Remember to delete from tail in arc consistency

from collections import defaultdict

def AC3(csp, queue=None, removals=defaultdict(set)):
    if queue is None:
        queue = [(Xt,X) for Xt in csp.adjList for X in csp.adjList[Xt]]

    while queue:
        #Xt --> Xh Delete from domain of Xt
        (Xt,Xh) = queue.pop()
        if remove_inconsistent_values(csp,Xt,Xh,removals):
            if not csp.domains[Xt]:
                return False
        elif len(csp.domains[Xt])>1:
            continue
        for X in csp.adjList[Xt]:
            if X != Xt:
                queue.append((X,Xt))

    return True

def remove_inconsistent_values(csp,Xt,Xh,removals):
    #Returns True if we remove a value
    revised = False

    #If Xt=x with Xh=y for every possible y,eliminate Xt=x
    for x in csp.domains[Xt].copy():
        for y in csp.domains[Xh]:
            if not csp.conflicts(*Xt,x,*Xh,y):
                break
        else:
            csp.domains[Xt].remove(x)
            removals[Xt].add(x)
            revised = True
    return True

def makeArcQueue(csp,Xs):
    return [(Xt,Xh) for Xh in Xs for Xt in csp.adjList[Xh]]
