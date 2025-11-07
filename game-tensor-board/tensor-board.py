import numpy as np 

#This is an example tensor representing this map: https://overcooked.fandom.com/wiki/1-2_%28Overcooked!_2%29

# Each type of tile can be mapped to an ASCII character for human readability
location_legend = {'.':0, '=':1, '#':2, '*':3, '$':4, '+':5, '-':6, '0': 7, '1':8}

#The "locations" on the board can be represented as a 2-D tensor of size W*H - this map is represented below
location_map = [['=','=','#','#','#','=','=','+','$','$','='],
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
C1 = len(location_legend)

# With this, a tensor can be created that converts the ASCII to an attribute vector
location_tensor = np.zeros((C1,H,W), dtype=np.int8) # this makes an all-0 tensor of the prescribed 3 dimensions
for r in range(H):
    for c in range(W):
        cls = location_legend[location_map[r][c]]
        location_tensor[cls, r, c] = 1

print('Location Tensor')
print(location_tensor,'\n')

# Next, dynamic attributes "resources" can be added as attribute vectors to the 3d dimension
"""
plate = O = 1
fire extinguisher = & = 2
pot = U = 3
rice pot = u = 4
fish = F = 5
chopped fish = f = 6
shrimp = S = 7
chopped shrimp = s = 8
rice = R = 9
cooked rice = r = 10
"""

resource_legend = {'':0, 'O':1, '&':2, 'U':3, 'u':4, 'F':5, 'f':6, 'S':7, 'R':8, 'r':9}
C2 = len(resource_legend)

# The human friendly resource map would be this
resource_map = [['&','' ,'' ,'' ,'F','' ,'' ,'O','' ,'' ,'' ],
                ['' ,'' ,'' ,'' ,'' ,'' ,'' ,'O','' ,'' ,'' ],
                ['' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ],
                ['' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ],
                ['' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ],
                ['' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ],
                ['' ,'' ,'f','' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ],
                ['f','f','' ,'' ,'' ,'u','' ,'U','u','' ,'' ]]

resource_tensor = np.zeros((C2,H,W), dtype=np.int8) # this makes an all-0 tensor of the prescribed 3 dimensions
for r in range(H):
    for c in range(W):
        cls = resource_legend[resource_map[r][c]]
        resource_tensor[cls, r, c] = 1

print('Resource Tensor')
print(resource_tensor,'\n')

# Next, concatenate the two tensors to combine them in the channels axis
state_tensor = np.concatenate((location_tensor,resource_tensor),axis = 0)

# Temporarily show all elements
np.set_printoptions(threshold=np.inf)

print('Combined State Tensor')
print(state_tensor,'\n')

# Temporarily show all elements
np.set_printoptions(threshold=1000)