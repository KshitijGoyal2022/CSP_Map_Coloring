from AC3MRVLCVMapSolver import AC3MRVLCVMapSolver

neighbors = {
    "Schleswig-Holstein":["Hamburg","Mecklenburg-Vorpommern","Niedersachsen"],
    "Hamburg":["Schleswig-Holstein","Niedersachsen"],
    "Mecklenburg-Vorpommern":["Brandenburg","Sachsen-Anhalt","Niedersachsen"],
    "Bremen":["Niedersachsen"],
    "Nordrhein-Westfalen":["Niedersachsen","Hessen","Rheinland-Pfalz"],
    "Brandenburg":["Berlin","Mecklenburg-Vorpommern","Sachsen-Anhalt","Sachsen","Niedersachsen"],
    "Hessen":["Nordrhein-Westfalen","Rheinland-Pfalz","Baden-Württemberg","Bayern","Thüringen","Niedersachsen"],
    "Rheinland-Pfalz":["Saarland","Hessen","Nordrhein-Westfalen","Baden-Württemberg"],
    "Bayern":["Baden-Württemberg","Hessen","Thüringen","Sachsen"],
    "Saarland":["Rheinland-Pfalz"],
    "Thüringen":["Hessen","Bayern","Sachsen","Sachsen-Anhalt","Niedersachsen"],
    "Sachsen":["Brandenburg","Sachsen-Anhalt","Thüringen","Bayern"],
    "Niedersachsen":["Bremen","Hamburg","Schleswig-Holstein","Sachsen-Anhalt","Thüringen","Hessen","Nordrhein-Westfalen","Mecklenburg-Vorpommern","Brandenburg"],
    "Baden-Württemberg":["Bayern","Hessen","Rheinland-Pfalz"],
    "Berlin":["Brandenburg"]
}

states = {
    "Schleswig-Holstein": None,
    "Hamburg": None,
    "Mecklenburg-Vorpommern": None,
    "Bremen": None,
    "Nordrhein-Westfalen": None,
    "Brandenburg": None,
    "Hessen": None,
    "Rheinland-Pfalz": None,
    "Bayern": None,
    "Saarland": None,
    "Thüringen": None,
    "Sachsen": None,
    "Niedersachsen": None,
    "Baden-Württemberg": None,
    "Berlin": None,
    "Sachsen-Anhalt": None
}

sol = AC3MRVLCVMapSolver()
sol.solveMapColoring(states=states, neighbors=neighbors)



