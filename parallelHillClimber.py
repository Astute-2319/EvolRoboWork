import constants as c
import copy
import os
import pyrosim.pyrosim as pyrosim
from solution import SOLUTION
import time

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf 2>nul")
        os.system("del fitness*.txt 2>nul")
        self.next_available_id = 0
        self.parents = {}
        for i in range(0, c.population_size):
            self.parents[i] = SOLUTION(self.next_available_id)
            self.next_available_id += 1
    
    def Evolve(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()
        for i in self.parents:
            self.parents[i].Start_Simulation('DIRECT')
        
        for i in self.parents:
            self.parents[i].Wait_For_Simulation()

        for current_generation in range(c.number_of_generations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        # self.Mutate()
        # self.child.Evaluate('DIRECT')
        # self.Print()
        # self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].my_id = self.next_available_id
            self.next_available_id += 1
        # self.child = copy.deepcopy(self.parent)

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
