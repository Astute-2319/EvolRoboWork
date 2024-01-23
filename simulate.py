import pybullet as p
import time as t
physicsClient = p.connect(p.GUI)

p.setGravity(0,0,-9.8)
p.loadSDF("box.sdf")

for x in range(0, 1000):
    p.stepSimulation()
    t.sleep(1/60)
    print(x)

p.disconnect()