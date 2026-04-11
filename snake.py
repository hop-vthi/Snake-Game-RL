import numpy as np
import random
import math as m


# action, 0 = Forward, 1 = Left, 2 = Right
class Snake(object):
    directions = [0,1,2,3] #0= Up, 1= DOWN, 2 = LEFT, 3 = RIGHT
    def __init__(self,length: int = 3):
        self.length = length
    # reset snake random
    def reset(self):
        self.i_pos =  np.array([15][15])/2 # Không thì để [2][2] đi
        self.body_position = [np.array([ self.i_pos[0] - x, self.i_pos[1] ], dtype=int) for x in range(self.length)]


    def movement(self, action):
        if action == 0 :
            return self.move_forward(action) # Tự tạo hàm khi nó forward với từng direction thì tiếp theo nó sẽ ntn nhé

        elif action == 1:
            return self.move_left(action)
        elif action == 2:
            return self.move_right(action)

    def is_colliding(self, position):
      pass

