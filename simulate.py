import pybullet as p
import time

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

for iter in range(0,1000):
    p.stepSimulation()
    print(iter)
    time.sleep(1/60)

p.disconnect()

