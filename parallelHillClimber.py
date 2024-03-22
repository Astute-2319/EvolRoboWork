import constants as c
import copy
import os
import pyrosim.pyrosim as pyrosim
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
        self.Evaluate(self.parents)

        for current_generation in range(c.number_of_generations):
            print("GENERATION", current_generation+1, "OF", c.number_of_generations)
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].my_id = self.next_available_id
            self.next_available_id += 1
        # self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()
        # self.child.Mutate()
        # self.child.Set_ID(self.next_available_id)
        # self.next_available_id += 1
            
    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation('DIRECT')
        
        for i in solutions:
            solutions[i].Wait_For_Simulation()

    def Select(self):
        for i in self.parents.keys():
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Show_Best(self):
        best_parent = self.parents[0]
        for i in self.parents.keys():
            if self.parents[i].fitness < best_parent.fitness:
                best_parent = self.parents[i]
        print("BEST PARENT: ", best_parent.my_id)
        print("BEST FITNESS: ", best_parent.fitness)
        best_parent.Start_Simulation('GUI')

    def Print(self):
        for i in self.parents.keys():
            print("\n Fitness of Parent: " + str(self.parents[i].fitness) + " Fitness of Child: " + str(self.children[i].fitness))
        # print("\n***** PARENT: ", self.parent.fitness, " CHILD: ", self.child.fitness, "*****")
