import constants as c
import copy
from solution import SOLUTION
import time

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.next_available_id = 0
        self.parents = {}
        for i in range(0, c.population_size):
            self.parents[i] = SOLUTION(self.next_available_id)
            self.next_available_id += 1
    
    def Evolve(self):
        for i in self.parents:
            self.parents[i].Start_Simulation('GUI')
            # for current_generation in range(c.number_of_generations):
            #     self.Evolve_For_One_Generation()
        
        # time.sleep(7)

        for i in self.parents:
            self.parents[i].Wait_For_Simulation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        self.child.Set_ID(self.next_available_id)
        self.next_available_id += 1

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Show_Best(self):
        pass
        # self.parent.Evaluate('GUI')

    def Print(self):
        print("\n***** PARENT: ", self.parent.fitness, " CHILD: ", self.child.fitness, "*****")
