from AC3MRVLCVMapSolver import AC3MRVLCVMapSolver

from collections import defaultdict
from MapColoringCSP import MapColoringCSP

# neighbors= {
#     "KIGALI": ["NORTH","SOUTH","EAST"],
#     "EAST":["KIGALI","NORTH","SOUTH"],
#     "SOUTH":["WEST","NORTH","KIGALI","EAST"],
#     "WEST":["NORTH","SOUTH"],
#     "NORTH":["WEST","SOUTH","KIGALI","EAST"]
# }
#
# states ={
#     "KIGALI": None,
#     "EAST": None,
#     "SOUTH": None,
#     "WEST": None,
#     "NORTH": None
# }

neighbors = {
    "SCHLESWIG-HOLSTEIN":["HAMBURG","MECKLENBURG-VORPOMMERN","NIEDERSACHSEN"],
    "HAMBURG":["SCHLESWIG-HOLSTEIN","NIEDERSACHSEN"],
    "MECKLENBURG-VORPOMMERN":["BRANDENBURG","SACHSEN-ANHALT","NIEDERSACHSEN"],
    "BREMEN":["NIEDERSACHSEN"],
    "NORDRHEIN-WESTFALEN":["NIEDERSACHSEN","HESSEN","RHEINLAND-PFALZ"],
    "BRANDENBURG":["BERLIN","MECKLENBURG-VORPOMMERN","SACHSEN-ANHALT","SACHSEN","NIEDERSACHSEN"],
    "HESSEN":["NORDRHEIN-WESTFALEN","RHEINLAND-PFALZ","BADEN-WURTTEMBERG","BAYERN","THURINGEN","NIEDERSACHSEN"],
    "RHEINLAND-PFALZ":["SAARLAND","HESSEN","NORDRHEIN-WESTFALEN","BADEN-WURTTEMBERG"],
    "BAYERN":["BADEN-WURTTEMBERG","HESSEN","THURINGEN","SACHSEN"],
    "SAARLAND":["RHEINLAND-PFALZ"],
    "THURINGEN":["HESSEN","BAYERN","SACHSEN","SACHSEN-ANHALT","NIEDERSACHSEN"],
    "SACHSEN":["BRANDENBURG","SACHSEN-ANHALT","THURINGEN","BAYERN"],
    "NIEDERSACHSEN":["BREMEN","HAMBURG","SCHLESWIG-HOLSTEIN","SACHSEN-ANHALT","THURINGEN","HESSEN","NORDRHEIN-WESTFALEN","MECKLENBURG-VORPOMMERN","BRANDENBURG"],
    "BADEN-WURTTEMBERG":["BAYERN","HESSEN","RHEINLAND-PFALZ"],
    "BERLIN":["BRANDENBURG"]
}

states = {
    "SCHLESWIG-HOLSTEIN": None,
    "HAMBURG": None,
    "MECKLENBURG-VORPOMMERN": None,
    "BREMEN": None,
    "NORDRHEIN-WESTFALEN": None,
    "BRANDENBURG": None,
    "HESSEN": None,
    "RHEINLAND-PFALZ": None,
    "BAYERN": None,
    "SAARLAND": None,
    "THURINGEN": None,
    "SACHSEN": None,
    "NIEDERSACHSEN": None,
    "BADEN-WURTTEMBERG": None,
    "BERLIN": None,
    "SACHSEN-ANHALT": None
}

sol = AC3MRVLCVMapSolver()
sol.solveMapColoring(states=states, neighbors=neighbors)


# def addEdge(state1, state2, adjList):
#     adjList[state1].add(state2)
#     adjList[state2].add(state1)
#
#
# def buildCspProblem(states, neighbors):
#     adjList = defaultdict(set)
#     # Build graph (constraints) based on neighboring information
#     for state1, adjStates in neighbors.items():
#         for state2 in adjStates:
#             addEdge(state1, state2, adjList)
#     # Set domains (colors available for each state)
#     variables = list(states.keys())
#     domains = {state: set(range(4)) for state in states}  # Assuming 4 different colors
#     return MapColoringCSP(variables, adjList, domains)
#
# print(buildCspProblem(states,neighbors).domains)


