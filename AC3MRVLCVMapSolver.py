from AC3MapColoringSolver import AC3MapColoringSolver
from AC3 import *
import MapColoringGUI


class AC3MRVLCVMapSolver(AC3MapColoringSolver):
    def count_conflict(self, csp, state, color):
        cnt = 0
        for neighbor in csp.adjList[state]:
            if color in csp.domains[neighbor]:
                cnt += 1
        return cnt

    def popMin(self, array, key):
        minimum, idx = float("inf"), 0
        for i in range(len(array)):
            if key(array[i]) < minimum:
                idx = i
                minimum = key(array[i])
        array[idx], array[-1] = array[-1], array[idx]
        return array.pop()

    def solveMapColoring(self, country_choice, states, neighbors, color_choices):
        csp = self.buildCspProblem(states, neighbors, color_choices) #Creates the CSP using the inputted information

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
            self.print_solution(csp,country_choice)

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

    def print_solution(self, csp,country_choice):
        states_colors = {}
        for state, colors in csp.domains.items():
            if len(colors) == 1:
                states_colors[state] = next(iter(colors))
                print(f"{state} ----> Color {next(iter(colors))}")
            else:
                print(f"{state}: No solution found")
        print(states_colors)
        MapColoringGUI.ColorCountry(states_colors=states_colors,country_choice=country_choice)
