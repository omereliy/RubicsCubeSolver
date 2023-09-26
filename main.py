import string

import numpy as np

import RubikCube

cube: RubikCube.RubiksCube = RubikCube.RubiksCube()
#  print(cube.cube[3])

# cube.right_rot()
# print("+++++++++++++++right+++++++++++++++++++++++++++++\n")
# print(cube.cube)


cube.scramble("U\' R2 D2 U\' B' L\' D L\' U B U' L\' D\' R\' D\' R U L2 B2 L F\' L R\' D' U2 R\' D U\' B\'")
print("===============MROT=================")
print(cube.cube)





