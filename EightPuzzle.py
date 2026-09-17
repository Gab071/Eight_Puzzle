import copy
import heapq as hp

class Puzzle:
    def __init__(self):

        self.desiredState = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

    
    def print_state(self, currentState):
        for row in currentState:
            print(row)

    
    def exchange(self, pos1, pos2, currentState):
        p1 = [-1, -1]
        p2 = [-1, -1]
        for i in range(len(currentState)):
            for j in range(len(currentState)):
                if currentState[i][j] == pos1:
                    p1 = [i, j]
                
                elif currentState[i][j] == pos2:
                    p2 = [i, j]

        currentState[p2[0]][p2[1]], currentState[p1[0]][p1[1]] = currentState[p1[0]][p1[1]], currentState[p2[0]][p2[1]]
                    
    
    def state_desired(self, currentState):
        return self.desiredState == currentState


    def neighbouring_states(self, state1, state2):
        states = self.move_state(state1)
        states = {self.convert_to_tuple(s) for s in states}
        state2 = self.convert_to_tuple(state2)

        return state2 in states
            

    def move_state(self, state):
        states = []
        r, c = self.find_field(state, 0)
        
        kierunki = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for dr, dc in kierunki:
            nowy_r, nowy_c = r + dr, c + dc
            
            if 0 <= nowy_r < len(state) and 0 <= nowy_c < len(state):
                # I made here deep copy because python is not creating a new matrix
                stateCopy = copy.deepcopy(state)
                stateCopy[r][c], stateCopy[nowy_r][nowy_c] = stateCopy[nowy_r][nowy_c], stateCopy[r][c]
            
                states.append(stateCopy)  
        
        return states


    def convert_to_tuple(self, state):
        return tuple(tuple(row) for row in state)
    

    def count_legal_states(self, state1):
        p0 = self.find_field(state1, 0)
        legalStates = 0
        row, col = p0[0], p0[1]

        if row < len(state1):
            legalStates += 1

        if col < len(state1):
            legalStates += 1

        if row >= 0:
            legalStates += 1

        if col >= 0:
            legalStates += 1
        
        return legalStates


    def find_field(self, state1, field):
        for r in range(len(state1)):
            for c in range(len(state1)):
                if state1[r][c] == field:
                    return [r, c]


    def Manhattan_distance(self, currentState):
        index = 1
        sum = 0
        for row in range(len(currentState)):
            for col in range(len(currentState)):
                pos = self.find_field(currentState, index)
                sum += abs(pos[0] - row) + abs(pos[1] - col)
                index += 1
                if index == 9:
                    return sum
        
        return sum


    def find_path(self, initialState):
        queue = []
        # There is f, because g = 0
        f = self.Manhattan_distance(initialState)
        g = 0
        # Just to not get an error, because the state in heapq is compared and we need that variable to distinguish between "same states"
        count = 0
        hp.heappush(queue, (f, count, g, initialState))
        visited = set()
        initialStateT = self.convert_to_tuple(initialState)
        parents = {}
        while len(queue) > 0:
            f, count, g, currentState = hp.heappop(queue)
            currentStateT = self.convert_to_tuple(currentState)

            if self.state_desired(currentState):
                path = []
                val = currentStateT
                path.append(currentStateT)
                while val != initialStateT:
                    newVal = parents[val]
                    newVal = self.convert_to_tuple(newVal)
                    val = newVal
                    path.append(val)

                return path 
                    
            
            if currentStateT not in visited:
                states = self.move_state(currentState)
                for state in states:
                    stateTuple = self.convert_to_tuple(state)
                    if stateTuple not in visited: # and stateTuple not in parents:
                        parents[stateTuple] = currentStateT
                        count += 1
                        h = self.Manhattan_distance(state)
                        hp.heappush(queue, (h+g, count, g+1, state))
                
                visited.add(currentStateT)

        return False



state1 = [
    [1, 3, 8],
    [0, 5, 4],
    [2, 7, 6]
]


uk = Puzzle()

print()
path = uk.find_path(state1)

for element in path:
    uk.print_state(element)
    
    print()