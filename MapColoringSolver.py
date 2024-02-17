from collections import defaultdict
# from SudokuCSP import SudokuCSP
from CSP import CSP

class SudokuSolver(object):
    def addEdge(self, state1, state2, adjList):
        adjList[state1].add(state2)
        adjList[state2].add(state1)

    def buildCspProblem(self, states, neighbors):
        adjList = defaultdict(set)
        # Build graph (constraints) based on neighboring information
        for state1, adjStates in neighbors.items():
            for state2 in adjStates:
                self.addEdge(state1, state2, adjList)
        # Set domains (colors available for each state)
        variables = list(states.keys())
        domains = {state: set(range(4)) for state in states}  # Assuming 4 different colors
        return CSP(variables, adjList, domains)


# neighbors = {
#     "SCHLESWIG-HOLSTEIN":["HAMBURG","MECKLENBURG-VORPOMMERN","NIEDERSACHSEN"],
#     "HAMBURG":["SCHLESWIG-HOLSTEIN","NIEDERSACHSEN"],
#     "MECKLENBURG-VORPOMMERN":["BRANDENBURG","SACHSEN-ANHALT","NIEDERSACHSEN"],
#     "BREMEN":["NIEDERSACHSEN"],
#     "NORDRHEIN-WESTFALEN":["NIEDERSACHSEN","HESSEN","RHEINLAND-PFALZ"],
#     "BRANDENBURG":["BERLIN","MECKLENBURG-VORPOMMERN","SACHSEN-ANHALT","SACHSEN","NIEDERSACHSEN"],
#     "HESSEN":["NORDRHEIN-WESTFALEN","RHEINLAND-PFALZ","BADEN-WURTTENBERG","BAYERN","THURINGEN","NIEDERSACHSEN"],
#     "RHEINLAND-PFALZ":["SAAPLAND","HESSEN","NORDRHEIN-WESTFALEN","BADEN-WURTTENBERG"],
#     "BAYERN":["BADEN-WURTTENBERG","HESSEN","THURINGEN","SACHSEN"],
#     "SAAPLAND":["RHEINLAND-PFALZ"],
#     "THURINGEN":["HESSEN","BAYERN","SACHSEN","SACHSEN-ANHALT","NIEDERSACHSEN"],
#     "SACHSEN":["BRANDENBURG","SACHSEN-ANHALT","THURINGEN","BAYERN"],
#     "NIEDERSACHSEN":["BREMEN","HAMBURG","SCHLESWIG-HOLSTEIN","SACHSEN-ANHALT","THURINGEN","HESSEN","NORDRHEIN-WESTFALEN","MECKLENBURG-VORPOMMERN","BRANDENBURG"],
#     "BADEN-WURTTENBERG":["BAYERN","HESSEN","RHEINLAND-PFALZ"],
#     "BERLIN":["BRANDENBURG"]
# }

# states = {
#     "SCHLESWIG-HOLSTEIN": None,
#     "HAMBURG": None,
#     "MECKLENBURG-VORPOMMERN": None,
#     "BREMEN": None,
#     "NORDRHEIN-WESTFALEN": None,
#     "BRANDENBURG": None,
#     "HESSEN": None,
#     "RHEINLAND-PFALZ": None,
#     "BAYERN": None,
#     "SAARLAND": None,
#     "THÜRINGEN": None,
#     "SACHSEN": None,
#     "NIEDERSACHSEN": None,
#     "BADEN-WÜRTTEMBERG": None,
#     "BERLIN": None,
#     "SACHSEN-ANHALT": None
# }
    def solveMapColoring(self):
        pass
        # # Example usage of buildCspProblem with some hypothetical map data
        # states = {"State1": None, "State2": None}  # States as variables
        # neighbors = {"State1": ["State2", "State3"], "State2": ["State1", "State4"]}  # Adjacency info
        # csp, _ = self.buildCspProblem(states, neighbors)
        # # Here you would call an algorithm to solve the CSP, such as backtracking, AC3, etc.
        # solution = self.solveCSP(csp)
        # if solution:
        #     # Apply the solution
        #     for state, color in solution.items():
        #         states[state] = color
        # else:
        #     print("No solution found.")
