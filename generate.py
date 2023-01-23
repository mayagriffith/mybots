import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

# pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1] , size=[length,width,height])
for col in range(0,5):
    length = 1
    width = 1
    height = 1
    for row in range(0, 5):
        length = 1
        width = 1
        height = 1
        for i in range(0, 10):
            pyrosim.Send_Cube(name="Box", pos=[x+col,y+row,z+i] , size=[length,width,height])
            length = length * .90
            width = width * .90
            height = height * .90


pyrosim.End()