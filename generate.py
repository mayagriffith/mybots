import pyrosim.pyrosim as pyrosim


length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[x-2,y+2,z] , size=[length,width,height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length,width,height])

    pyrosim.End()

Create_World()
Create_Robot()



# pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1] , size=[length,width,height])


#25 TOWERS GENERATING CODE
# for col in range(0,5):
#     length = 1
#     width = 1
#     height = 1
#     for row in range(0, 5):
#         length = 1
#         width = 1
#         height = 1
#         for i in range(0, 10):
#             pyrosim.Send_Cube(name="Box", pos=[x+col,y+row,z+i] , size=[length,width,height])
#             length = length * .90
#             width = width * .90
#             height = height * .90


