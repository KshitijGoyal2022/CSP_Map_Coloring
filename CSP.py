class CSP():
    def __init__(self,variables=[], adjList={},domains={}):
        self.variables = variables
        self.adjList = adjList
        self.domains = domains

    def restore_domains(self,removals):
        for X in removals:
            self.domains[X] |= removals[X]


