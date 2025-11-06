# Kitchen Commander Tensor Board 

## Goal  
The goal is to develop a data structure that encodes the attributes of the game state for easy reference by the computer systems in the network. The Tensor Board will be a universal representation of the current game state shared between the Jetson and the 4 Raspberry Pis.
   
## Success Criteria  
- [ ] This data structure must fully encode all relevant information from the game state. This includes individual players, each individual type of tile, every resource on the map, and the state of resources.
- [ ] Each attribute in the state must be detectable by an object detection model (no metadata or intuition not visually represented.
- [ ] Must be small enough to be searched efficiently without noticeable latency.
      
## Plan of Action  
To accomplish this, I will be using a sparse 3-Dimensional Tensor with channels representing every unique tile type and every individual resource.

- Develop a data structure format
- Uniquely code each individual tile (location) and resource with an ASCII symbol
- Conform all attributes to a one-hot encoded vector
- Test structure by translating 2 sample maps to tensor-board format by hand
- Reverse design the object detection classes to differentiate each separate attribute
- Integrate with computervision

## Execution

### Log 05 November 2025  
I started researching "tensors" because I've seen them mentioned in AI decision making projects. My initial cursory understanding of them is that they are more complex matrices. A better understanding of how to use them to encode the attributes of the game map should clear up ambiguity about what my computervision sub-subsystem needs to detect and classify as an independent entity.  

What something should be **seen** as will be derived by what it needs to be **tracked** as.  

I found a very simple and informative reference [A Gentle Intro To Tensors With Examples](https://wandb.ai/vincenttu/intro-to-tensors/reports/A-Gentle-Intro-To-Tensors-With-Examples--VmlldzozMTQ2MjE5#what-are-tensors-in-machine-learning?)

This article elegantly explains the background concepts for conceptualizing tensors, their dimensions, and how they are used in machine learning.  
  
Starting from the simple shape of the map, it can be represented as a simple matrix (a 2-Dimensional tensor)  of ASCII symbols.
<img width="382" height="281" alt="image" src="https://github.com/user-attachments/assets/668ed2ed-477d-4b66-8a20-ea2611d9e9be" />  

```
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
```

Next, when each ASCII value is broken out as a one-hot encoded vector for its individual attribute it is intuitively a stack of matrices with each one showing a "1" for the presence of a tile type and a "0" for the absense.
  
```
# these are "walkable floor tiles"
[[[0 0 0 0 0 0 0 0 0 0 0]
  [1 1 1 1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1 1 1 1]
  [1 1 1 1 0 0 0 1 1 1 1]
  [1 1 1 1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1 1 1 1]
  [1 1 1 1 1 1 1 1 1 1 1]
  [0 0 0 0 0 0 0 0 0 0 0]]

# these are "counter tiles"
 [[1 1 0 0 0 1 1 0 0 0 1]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 1 0 1 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [1 1 1 1 0 1 0 0 0 1 1]]

# these are "cutting boards"
 [[0 0 1 1 1 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]]

# these are "burners"
 [[0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 1 1 1 0 0]]

# this is the "delivery window"
 [[0 0 0 0 0 0 0 0 1 1 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]]


# this is the "plate return"
 [[0 0 0 0 0 0 0 1 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]]

# this is the "trash"
 [[0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 1 0 0 0 0 0 0]]

# this is the "shrimp crate" (notice is is non existent in this map)
 [[0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]]

# this is the "fish crate" 
 [[0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 1 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]]]

```

This tensor stores the static tile locations and types for a single frame.
