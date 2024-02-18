from collections import defaultdict
from MapColoringCSP import MapColoringCSP

class MapColoringSolver(object):
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
        domains = {state: {"red", "green", "blue", "yellow"} for state in states}  # Assuming 4 different colors
        return MapColoringCSP(variables, adjList, domains)

    def solveMapColoring(self,states,neighbors):
        pass

