from AC3MapColoringSolver import AC3MapColoringSolver
from AC3 import *

class AC3MRVLCVMapSolver(AC3MapColoringSolver):
    def count_conflict(self,csp,state,color):
        cnt =0
        for neighbor in csp.adjList[state]:
            if color in csp.domains[neighbor]:
                cnt +=1
        return cnt

    def popMin(self,array,key):
        minimum,idx = float("inf"),0
        for i in range(len(array)):
            if key(array[i]) < minimum:
                idx  =i
                minimum = key(array[i])
        array[idx],array[-1] = array[-1],array[idx]
        return array.pop()


    def solveMapColoring(self,states,neighbors):
        csp = self.buildCspProblem(states, neighbors)

        if not AC3(csp, makeArcQueue(csp)):
            print("No solution could be found.")
            return False

        uncertain = []
        for state, colors in csp.domains.items():
            if len(colors) > 1:
                uncertain.append(state)
        self.backtrack(csp, uncertain)

        if not self.backtrack(csp, uncertain):
            return False

        if self.backtrack(csp, uncertain):
            self.print_solution(csp)

    def backtrack(self, csp, uncertain):
        if not uncertain:
            return True
        X = self.popMin(uncertain, key=lambda X: len(csp.domains[X]))
        removals = defaultdict(set)
        # Sort the values in domain in the order of LCV and loop in that order
        domainlist = list(csp.domains[X])
        domainlist.sort(key=lambda x: self.count_conflict(csp, X, x))
        for x in domainlist:
            domainX = csp.domains[X]
            csp.domains[X] = set([x])
            if AC3(csp, makeArcQueue(csp), removals):
                retval = self.backtrack(csp, uncertain)
                if retval:
                    return True
            csp.restore_domains(removals)
            csp.domains[X] = domainX
        uncertain.append(X)
        return False

    def print_solution(self, csp):
        for state, colors in csp.domains.items():
            if len(colors) == 1:
                # Assuming each color is represented as an integer
                print(f"{state}: Color {next(iter(colors)) + 1}")
            else:
                print(f"{state}: No solution found")

