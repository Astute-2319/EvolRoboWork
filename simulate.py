from simulation import SIMULATION
import sys

direct_or_gui = sys.argv[1]
solution_id = sys.argv[2]

simulation = SIMULATION(direct_or_gui, solution_id)
simulation.Run()