import numpy as np 

#This is an example tensor representing this map: https://overcooked.fandom.com/wiki/1-2_%28Overcooked!_2%29

# Each type of tile can be mapped to an ASCII character for human readability
tile_legend = {'.':0, '=':1, '#':2, '*':3, '$':4, '+':5, '-':6, '0': 7, '1':8}

#The "locations" on the board can be represented as a 2-D tensor of size W*H - this map is represented below
state_map = [['=','=','#','#','#','=','=','+','$','$','='],
         ['.','.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','=','1','=','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.','.'],
         ['=','=','=','=','-','=','*','*','*','=','=']]

H = 8
W = 11

# Next, each tile type is converted to a one-hot encoded vector of its tile-legend value
# The number of channels is equivalent to the number of distinct attributes for tile type
C = len(tile_legend)

# With this, a tensor can be created that converts the ASCII to an attribute vector
state_tensor = np.zeros((C,H,W), dtype=np.int8) # this makes an all-0 tensor of the prescribed 3 dimensions
for r in range(H):
    for c in range(W):
        cls = tile_legend[state_map[r][c]]
        state_tensor[cls, r, c] = 1


print(state_tensor)