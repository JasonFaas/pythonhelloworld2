# You have a game of snake - you trace a path of up, down, left, right according to user input. The edges of the play area is looping - exiting out the right edge will bring you back around to the left edge.  If you run into yourself, you lose. You start out at a max length of 3 and every 10 steps you take, you max length get longer by one unit.

# I'd like you to implement the take step/move function which will be called every frame of the game.
# It should take in a direction as it's argument and tell me if I have lost the game (run into myself)

# https://giphy.com/embed/4JmTg4bTuofUQ
# Width, height of board & start x and start y

import numpy as np
import collections

positions = None
step_counter = None
width = None
height = None
direction_mods = None
dll = None

print(-1 % 4)


def init(board_width=5, board_height=5, start_x=2, start_y=2):
    global positions, step_counter, width, height, direction_mods, dll
    positions = np.zeros((board_height, board_width), dtype=bool)
    dll = collections.deque()
    dll.append([start_x, start_y])
    dll.append([start_x - 1, start_y])
    dll.append([start_x - 2, start_y])
    positions[start_x, start_y] = True
    positions[start_x - 1, start_y] = True
    positions[start_x - 2, start_y] = True
    step_counter = 0
    width = board_width
    height = board_height
    direction_mods = {'N': [-1, 0],
                      'S': [1, 0],
                      'E': [0, 1],
                      'W': [0, -1]}


def step_move(direction):
    global step_counter, dll
    #increment step counter
    step_counter += 1

    #Get new position coordinates
    direction_modifier = direction_mods[direction]
    head_position = dll[-1]
    new_position = [(head_position[0] + direction_modifier[0]) % height,
                    (head_position[1] + direction_modifier[1]) % width]

    head_prev_position = dll[-2]
    if new_position[0] == head_prev_position[0] and new_position[1] == head_prev_position[1]:
        print('wrong direction')
        return False
    if positions[new_position[0], new_position[1]]:
        print('step on self')
        return False

    #set new position
    positions[new_position[0], new_position[1]] = True
    dll.append([new_position[0], new_position[1]])

    if step_counter % 10 != 0:
        tail_position = dll[0]
        positions[tail_position[0], tail_position[1]] = False
        dll.popleft()

    print(positions)
    print(dll)

    return True


init()

print(positions)
print(dll)

assert step_move('N')
assert step_move('W')
assert step_move('N')
assert step_move('N')
assert step_move('E')
assert step_move('S')
assert step_move('E')
assert step_move('E')
assert step_move('E')
for i in range(30):
    print(i)
    assert step_move('E')
# assert step_move('N')
# assert step_move('S')
# assert step_move('E')
