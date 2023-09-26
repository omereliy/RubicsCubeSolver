import numpy as np


class RubiksCube:
    def __init__(self):  # initialization of the cube as a solved cube
        self.cube = np.array([  # each sub array represents a row on R,B,O,G while on y,W it represents a row if it
            # would've faced us
            [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # Upper face (white)
            [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # Down face (yellow)
            [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # Left face (green)
            [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # Right face (blue)
            [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # Front face (red)
            [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]  # Back face (orange)
        ], dtype=str)

        self.faces = {
            'U': 0,  # Upper face (white)
            'D': 1,  # Down face (yellow)
            'L': 5,  # Left face (green)
            'R': 4,  # Right face (blue)
            'F': 2,  # Front face (red)
            'B': 3  # Back face (orange)
        }

    def solve(self):  # TODO implement this!
        print(self.cube + 7)

    @staticmethod
    def parse_scramble(s: str):
        array = s.split()
        ret: list = []
        for move in array:
            if len(move) == 2 and move[1] == '2':
                ret.append(move[0])
                ret.append(move[0])
            elif len(move) == 3 and move[2] == '2':
                ret.append(move[:1])
                ret.append(move[:1])
            else:
                ret.append(move)
        return ret

    def scramble(self, scramble_algorithm: str):
        steps = self.parse_scramble(scramble_algorithm)
        while len(steps) > 0:
            print("====================")
            print(steps[0])
            print("====================")
            if steps[0] == 'R':
                self.right_rot()
                steps = steps[1:]
            elif steps[0] == 'L':
                self.left_rot()
                steps = steps[1:]
            elif steps[0] == 'U':
                self.up_rot()
                steps = steps[1:]
            elif steps[0] == 'D':
                self.down_rot()
                steps = steps[1:]
            elif steps[0] == 'F':
                self.front_rot()
                steps = steps[1:]
            elif steps[0] == 'B':
                self.back_rot()
                steps = steps[1:]
            elif steps[0] == 'L\'':
                self.left_tag_rot()
                steps = steps[1:]
            elif steps[0] == 'R\'':
                self.right_tag_rot()
                steps = steps[1:]
            elif steps[0] == 'U\'':
                self.up_tag_rot()
                steps = steps[1:]
            elif steps[0] == 'D\'':
                self.down_tag_rot()
                steps = steps[1:]
            elif steps[0] == 'B\'':
                self.back_tag_rot()
                steps = steps[1:]
            elif steps[0] == 'F\'':
                self.front_tag_rot()
                steps = steps[1:]

    def print_state(self):
        print(self.cube)

    def right_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['R']] = np.rot90(self.cube[self.faces['R']], -1)  # 90 deg rot of the right face

        self.cube[self.faces['U']][0][2], self.cube[self.faces['U']][1][2], self.cube[self.faces['U']][2][2] = (
            pre_rot_cube[self.faces['F']][0][2], pre_rot_cube[self.faces['F']][1][2],
            pre_rot_cube[self.faces['F']][2][2])
        self.cube[self.faces['U']][1][2] = pre_rot_cube[self.faces['F']][1][2]
        self.cube[self.faces['U']][2][2] = pre_rot_cube[self.faces['F']][2][2]

        self.cube[self.faces['F']][0][2] = pre_rot_cube[self.faces['D']][0][2]
        self.cube[self.faces['F']][1][2] = pre_rot_cube[self.faces['D']][1][2]
        self.cube[self.faces['F']][2][2] = pre_rot_cube[self.faces['D']][2][2]

        self.cube[self.faces['B']][0][2] = pre_rot_cube[self.faces['U']][0][2]
        self.cube[self.faces['B']][1][2] = pre_rot_cube[self.faces['U']][1][2]
        self.cube[self.faces['B']][2][2] = pre_rot_cube[self.faces['U']][2][2]

        self.cube[self.faces['D']][0][2] = pre_rot_cube[self.faces['B']][0][2]
        self.cube[self.faces['D']][1][2] = pre_rot_cube[self.faces['B']][1][2]
        self.cube[self.faces['D']][2][2] = pre_rot_cube[self.faces['B']][2][2]

    def right_tag_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['R']] = np.rot90(self.cube[self.faces['R']], 1)  # 90 deg rot of the right face
        self.cube[self.faces['F']][0][2] = pre_rot_cube[self.faces['U']][0][2]
        self.cube[self.faces['F']][1][2] = pre_rot_cube[self.faces['U']][1][2]
        self.cube[self.faces['F']][2][2] = pre_rot_cube[self.faces['U']][2][2]

        self.cube[self.faces['D']][0][2] = pre_rot_cube[self.faces['F']][0][2]
        self.cube[self.faces['D']][1][2] = pre_rot_cube[self.faces['F']][1][2]
        self.cube[self.faces['D']][2][2] = pre_rot_cube[self.faces['F']][2][2]

        self.cube[self.faces['U']][0][2] = pre_rot_cube[self.faces['B']][0][2]
        self.cube[self.faces['U']][1][2] = pre_rot_cube[self.faces['B']][1][2]
        self.cube[self.faces['U']][2][2] = pre_rot_cube[self.faces['B']][2][2]

        self.cube[self.faces['B']][0][2] = pre_rot_cube[self.faces['D']][0][2]
        self.cube[self.faces['B']][1][2] = pre_rot_cube[self.faces['D']][1][2]
        self.cube[self.faces['B']][2][2] = pre_rot_cube[self.faces['D']][2][2]

    def left_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['L']] = np.rot90(self.cube[self.faces['L']], -1)  # 90 deg rot of the right face
        self.cube[self.faces['F']][0][0] = pre_rot_cube[self.faces['U']][0][0]
        self.cube[self.faces['F']][1][0] = pre_rot_cube[self.faces['U']][1][0]
        self.cube[self.faces['F']][2][0] = pre_rot_cube[self.faces['U']][2][0]

        self.cube[self.faces['D']][0][0] = pre_rot_cube[self.faces['F']][0][0]
        self.cube[self.faces['D']][1][0] = pre_rot_cube[self.faces['F']][1][0]
        self.cube[self.faces['D']][2][0] = pre_rot_cube[self.faces['F']][2][0]

        self.cube[self.faces['U']][0][0] = pre_rot_cube[self.faces['B']][0][0]
        self.cube[self.faces['U']][1][0] = pre_rot_cube[self.faces['B']][1][0]
        self.cube[self.faces['U']][2][0] = pre_rot_cube[self.faces['B']][2][0]

        self.cube[self.faces['B']][0][0] = pre_rot_cube[self.faces['D']][0][0]
        self.cube[self.faces['B']][1][0] = pre_rot_cube[self.faces['D']][1][0]
        self.cube[self.faces['B']][2][0] = pre_rot_cube[self.faces['D']][2][0]

    def left_tag_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['L']] = np.rot90(self.cube[self.faces['L']], 1)  # 90 deg rot of the right face

        self.cube[self.faces['U']][0][0] = pre_rot_cube[self.faces['F']][0][0]
        self.cube[self.faces['U']][1][0] = pre_rot_cube[self.faces['F']][1][0]
        self.cube[self.faces['U']][2][0] = pre_rot_cube[self.faces['F']][2][0]

        self.cube[self.faces['F']][0][0] = pre_rot_cube[self.faces['D']][0][0]
        self.cube[self.faces['F']][1][0] = pre_rot_cube[self.faces['D']][1][0]
        self.cube[self.faces['F']][2][0] = pre_rot_cube[self.faces['D']][2][0]

        self.cube[self.faces['B']][0][0] = pre_rot_cube[self.faces['U']][0][0]
        self.cube[self.faces['B']][1][0] = pre_rot_cube[self.faces['U']][1][0]
        self.cube[self.faces['B']][2][0] = pre_rot_cube[self.faces['U']][2][0]

        self.cube[self.faces['D']][0][0] = pre_rot_cube[self.faces['B']][0][0]
        self.cube[self.faces['D']][1][0] = pre_rot_cube[self.faces['B']][1][0]
        self.cube[self.faces['D']][2][0] = pre_rot_cube[self.faces['B']][2][0]

    def up_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['U']] = np.rot90(self.cube[self.faces['U']], -1)  # 90 deg rot of the right face
        self.cube[self.faces['F']][0] = pre_rot_cube[self.faces['R']][0]
        self.cube[self.faces['R']][0] = pre_rot_cube[self.faces['B']][2, ::-1]
        self.cube[self.faces['B']][2] = pre_rot_cube[self.faces['L']][0, ::-1]
        self.cube[self.faces['L']][0] = pre_rot_cube[self.faces['F']][0]

    def up_tag_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['U']] = np.rot90(self.cube[self.faces['U']], 1)  # 90 deg rot of the right face

        self.cube[self.faces['F']][0] = pre_rot_cube[self.faces['L']][0]
        self.cube[self.faces['R']][0] = pre_rot_cube[self.faces['F']][0]
        self.cube[self.faces['B']][2] = pre_rot_cube[self.faces['R']][0, ::-1]
        self.cube[self.faces['L']][0] = pre_rot_cube[self.faces['B']][2, ::-1]

    def down_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['D']] = np.rot90(self.cube[self.faces['D']], -1)  # 90 deg rot of the right face
        self.cube[self.faces['R']][2] = pre_rot_cube[self.faces['F']][2]
        self.cube[self.faces['B']][0] = pre_rot_cube[self.faces['R']][2, ::-1]
        self.cube[self.faces['L']][2] = pre_rot_cube[self.faces['B']][0, ::-1]
        self.cube[self.faces['F']][2] = pre_rot_cube[self.faces['L']][2]

    def down_tag_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['D']] = np.rot90(self.cube[self.faces['D']], 1)  # 90 deg rot of the right face

        self.cube[self.faces['F']][2] = pre_rot_cube[self.faces['R']][2]
        self.cube[self.faces['R']][2] = pre_rot_cube[self.faces['B']][0, ::-1]
        self.cube[self.faces['B']][0] = pre_rot_cube[self.faces['L']][2, ::-1]
        self.cube[self.faces['L']][2] = pre_rot_cube[self.faces['F']][2]

    def front_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['F']] = np.rot90(self.cube[self.faces['F']], -1)  # 90 deg rot of the right face
        self.cube[self.faces['U']][2] = np.array(
            [[pre_rot_cube[self.faces['L']][2][2], pre_rot_cube[self.faces['L']][1][2],
              pre_rot_cube[self.faces['L']][0][2]]])

        self.cube[self.faces['R']][0][0] = pre_rot_cube[self.faces['U']][2][0]
        self.cube[self.faces['R']][1][0] = pre_rot_cube[self.faces['U']][2][1]
        self.cube[self.faces['R']][2][0] = pre_rot_cube[self.faces['U']][2][2]

        self.cube[self.faces['D']][0] = np.array(
            [[pre_rot_cube[self.faces['R']][2][0], pre_rot_cube[self.faces['R']][1][0],
              pre_rot_cube[self.faces['R']][0][0]]])

        self.cube[self.faces['L']][0][2] = pre_rot_cube[self.faces['D']][0][0]
        self.cube[self.faces['L']][1][2] = pre_rot_cube[self.faces['D']][0][1]
        self.cube[self.faces['L']][2][2] = pre_rot_cube[self.faces['D']][0][2]

    def front_tag_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['F']] = np.rot90(self.cube[self.faces['F']], 1)  # 90 deg rot of the right face

        self.cube[self.faces['L']][2][2] = pre_rot_cube[self.faces['U']][2][0]
        self.cube[self.faces['L']][1][2] = pre_rot_cube[self.faces['U']][2][1]
        self.cube[self.faces['L']][0][2] = pre_rot_cube[self.faces['U']][2][2]

        self.cube[self.faces['U']][2] = np.array(
            [[pre_rot_cube[self.faces['R']][0][0], pre_rot_cube[self.faces['R']][1][0],
              pre_rot_cube[self.faces['R']][2][0]]])

        self.cube[self.faces['R']][2][0] = pre_rot_cube[self.faces['D']][0][0]
        self.cube[self.faces['R']][1][0] = pre_rot_cube[self.faces['D']][0][1]
        self.cube[self.faces['R']][0][0] = pre_rot_cube[self.faces['D']][0][2]

        self.cube[self.faces['D']][0] = np.array(
            [[pre_rot_cube[self.faces['L']][0][2], pre_rot_cube[self.faces['L']][1][2],
              pre_rot_cube[self.faces['L']][2][2]]])

    def back_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['B']] = np.rot90(self.cube[self.faces['B']], -1)  # 90 deg rot of the right face
        self.cube[self.faces['U']][0] = np.array(
            [[pre_rot_cube[self.faces['R']][0][2], pre_rot_cube[self.faces['R']][1][2],
              pre_rot_cube[self.faces['R']][2][2]]])

        self.cube[self.faces['R']][0][2] = pre_rot_cube[self.faces['D']][2][2]
        self.cube[self.faces['R']][1][2] = pre_rot_cube[self.faces['D']][2][1]
        self.cube[self.faces['R']][2][2] = pre_rot_cube[self.faces['D']][2][0]

        self.cube[self.faces['D']][2] = np.array(
            [[pre_rot_cube[self.faces['L']][0][0], pre_rot_cube[self.faces['L']][1][0],
              pre_rot_cube[self.faces['L']][2][0]]])

        self.cube[self.faces['L']][0][0] = pre_rot_cube[self.faces['U']][0][2]
        self.cube[self.faces['L']][1][0] = pre_rot_cube[self.faces['U']][0][1]
        self.cube[self.faces['L']][2][0] = pre_rot_cube[self.faces['U']][0][0]

    def back_tag_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['B']] = np.rot90(self.cube[self.faces['B']], 1)  # 90 deg rot of the right face

        self.cube[self.faces['R']][0][2] = pre_rot_cube[self.faces['U']][0][0]
        self.cube[self.faces['R']][1][2] = pre_rot_cube[self.faces['U']][0][1]
        self.cube[self.faces['R']][2][2] = pre_rot_cube[self.faces['U']][0][2]

        self.cube[self.faces['D']][2] = np.array(
            [[pre_rot_cube[self.faces['R']][2][2], pre_rot_cube[self.faces['R']][1][2],
              pre_rot_cube[self.faces['R']][0][2]]])

        self.cube[self.faces['L']][0][0] = pre_rot_cube[self.faces['D']][2][0]
        self.cube[self.faces['L']][1][0] = pre_rot_cube[self.faces['D']][2][1]
        self.cube[self.faces['L']][2][0] = pre_rot_cube[self.faces['D']][2][2]

        self.cube[self.faces['U']][0] = np.array(
            [[pre_rot_cube[self.faces['L']][2][0], pre_rot_cube[self.faces['L']][1][0],
              pre_rot_cube[self.faces['L']][0][0]]])

    def middle_rot(self):
        self.right_rot()
        self.left_tag_rot()
        self.x_tag_rot()

    def middle_tag_rot(self):
        self.right_tag_rot()
        self.left_rot()
        self.x_rot()

    def y_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['U']] = np.rot90(self.cube[self.faces['U']], 1)
        self.cube[self.faces['D']] = np.rot90(self.cube[self.faces['D']], -1)

        self.cube[self.faces['F']] = pre_rot_cube['R']

        self.cube[self.faces['L']] = pre_rot_cube['F']
        self.cube[self.faces['B']][0] = pre_rot_cube['L'][2, ::-1]
        self.cube[self.faces['B']][1] = pre_rot_cube['L'][1, ::-1]
        self.cube[self.faces['B']][2] = pre_rot_cube['L'][0, ::-1]
        self.cube[self.faces['R']][0] = pre_rot_cube['B'][2, ::-1]
        self.cube[self.faces['R']][1] = pre_rot_cube['B'][1, ::-1]
        self.cube[self.faces['R']][2] = pre_rot_cube['B'][0, ::-1]

    def y_tag_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['U']] = np.rot90(self.cube[self.faces['U']], -1)
        self.cube[self.faces['D']] = np.rot90(self.cube[self.faces['D']], 1)

        self.cube[self.faces['F']] = pre_rot_cube['R']

        self.cube[self.faces['L']] = pre_rot_cube['F']

        self.cube[self.faces['B']][0] = pre_rot_cube['R'][2, ::-1]
        self.cube[self.faces['B']][1] = pre_rot_cube['R'][1, ::-1]
        self.cube[self.faces['B']][2] = pre_rot_cube['R'][0, ::-1]

        self.cube[self.faces['L']][0] = pre_rot_cube['B'][2, ::-1]
        self.cube[self.faces['L']][1] = pre_rot_cube['B'][1, ::-1]
        self.cube[self.faces['L']][2] = pre_rot_cube['B'][0, ::-1]

    def x_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['L']] = np.rot90(self.cube[self.faces['L']], 1)
        self.cube[self.faces['R']] = np.rot90(self.cube[self.faces['R']], -1)  # 90 deg rot of the right face

        self.cube[self.faces['F']] = pre_rot_cube[self.faces['D']]
        self.cube[self.faces['D']] = pre_rot_cube[self.faces['B']]
        self.cube[self.faces['B']] = pre_rot_cube[self.faces['U']]
        self.cube[self.faces['U']] = pre_rot_cube[self.faces['F']]

    def x_tag_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['L']] = np.rot90(self.cube[self.faces['L']], -1)
        self.cube[self.faces['R']] = np.rot90(self.cube[self.faces['R']], 1)

        self.cube[self.faces['D']] = pre_rot_cube[self.faces['F']]
        self.cube[self.faces['B']] = pre_rot_cube[self.faces['D']]
        self.cube[self.faces['U']] = pre_rot_cube[self.faces['B']]
        self.cube[self.faces['F']] = pre_rot_cube[self.faces['U']]

    def z_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['F']] = np.rot90(self.cube[self.faces['F']], -1)
        self.cube[self.faces['B']] = np.rot90(self.cube[self.faces['B']], 1)

        self.cube[self.faces['R']] = np.rot90(pre_rot_cube[self.faces['U']], -1)
        self.cube[self.faces['U']] = np.rot90(pre_rot_cube[self.faces['L']], -1)
        self.cube[self.faces['L']] = np.rot90(pre_rot_cube[self.faces['D']], -1)
        self.cube[self.faces['D']] = np.rot90(pre_rot_cube[self.faces['R']], -1)

    def z_tag_rot(self):
        pre_rot_cube = self.cube.copy()
        self.cube[self.faces['F']] = np.rot90(self.cube[self.faces['F']], 1)
        self.cube[self.faces['B']] = np.rot90(self.cube[self.faces['B']], -1)

        self.cube[self.faces['U']] = np.rot90(pre_rot_cube[self.faces['R']], 1)
        self.cube[self.faces['L']] = np.rot90(pre_rot_cube[self.faces['U']], 1)
        self.cube[self.faces['D']] = np.rot90(pre_rot_cube[self.faces['L']], 1)
        self.cube[self.faces['R']] = np.rot90(pre_rot_cube[self.faces['D']], 1)
