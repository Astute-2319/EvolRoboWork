import constants as c
import copy
from solution import SOLUTION

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
    
    def Evolve(self):
        self.parent.Evaluate()
        for current_generation in range(c.number_of_generations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        pass

