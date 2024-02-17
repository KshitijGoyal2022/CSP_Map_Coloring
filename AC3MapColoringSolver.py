#Used in the AC3MRVLCVMapSolver.py
import MapColoringSolver

class AC3MapSolver(MapSolver):
    def solveMapColoring(self):
        csp,assigned = self.buildCspProblem()