# Eight Puzzle


## Overview

Eight Puzzle is a game where the goal is to move tiles to get desired order of tiles. Programmed in Python.

## How to use 

1. Change the order of the tiles on the lines 8-10:
```
self.desiredState = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
```

2. And also the order of the tiles on the lines 154-156:
```
state1 = [
    [1, 3, 8],
    [0, 5, 4],
    [2, 7, 6]
]
```

Point 1. is the state that computer will try to find and point 2. is the starting state. 

Note: There are states that is impossible to find from some starting states. For more info check more eloquent and reliable resources (for example [Wikipedia](https://www.wikipedia.org/)).

## How to Run 

1. Clone this repository:
```
git clone https://github.com/Gab071/Eight_Puzzle.git
cd Eight_Puzzle
```

2. Install python (if not installed):
```
sudo apt install python3 python3-pip
```

3. Run the code:
```
python3 Eight Puzzle 
```