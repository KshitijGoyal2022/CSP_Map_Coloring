class CSP():
    def __init__(self,variables=[], adjList={},domains={}):
        self.variables = variables
        self.adjList = adjList
        self.domains = domains

    def restore_domains(self,removals):
        for X in removals:
            self.domains[X] |= removals[X]

    # Used in min-conflict algorithm
    def nconflicts(self,X1,x,assignment):
        """
        Return the number of conflicts X1=x has with other variables
        Subclasses may implement this more efficiently
        """
        def conflict(X2):
            return self.conflicts(X1,x,X2,assignment[X2])
        return sum(conflict(X2) for X2 in self.adjList[X1] if X2 in assignment)

    def conflicted_vars(self,current):
        return [var for var in self.variables if self.nconflicts(var,current[var],current)>0]


