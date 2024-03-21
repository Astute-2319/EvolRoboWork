from simulation import SIMULATION
import sys

direct_or_gui = sys.argv[1]

simulation = SIMULATION(direct_or_gui)
simulation.Run()