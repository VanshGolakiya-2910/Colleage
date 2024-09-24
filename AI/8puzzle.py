from collections import deque

# Get initial and final states from the user
def states():
    initial_str = input("Enter the initial state row-wise (space-separated): ")
    final_str = input("Enter the final state row-wise (space-separated): ")

    initial = [list(map(int, initial_str.split()[i:i + 3])) for i in range(0, 9, 3)]
    final = [list(map(int, final_str.split()[i:i + 3])) for i in range(0, 9, 3)]

    return initial, final

# Get index of the empty space (represented by 0)
def find_empty(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

# Swap positions of two tiles
def swap(state, row1, col1, row2, col2):
    new_state = [row[:] for row in state]
    new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
    return new_state

# Generate all possible moves from the current state
def possible_moves(state):
    row, col = find_empty(state)
    moves = []

    if row > 0:  # Move up
        moves.append(swap(state, row, col, row - 1, col))
    if row < 2:  # Move down
        moves.append(swap(state, row, col, row + 1, col))
    if col > 0:  # Move left
        moves.append(swap(state, row, col, row, col - 1))
    if col < 2:  # Move right
        moves.append(swap(state, row, col, row, col + 1))

    return moves

# BFS to find the solution
def BFS():
    initial, final = states()
    
    # Convert to tuple for immutability in sets
    initial = tuple(map(tuple, initial))
    final = tuple(map(tuple, final))

    # Queue holds (current_state, path_taken)
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        # If we've already visited this state, skip it
        if current in visited:
            continue
        
        visited.add(current)

        # Check if this is the solution
        if current == final:
            return path + [current]

        # Explore possible moves
        for move in possible_moves([list(row) for row in current]):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                queue.append((move_tuple, path + [current]))

    return None

# Print the solution
solution = BFS()
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
from collections import deque

# Get initial and final states from the user
def states():
    initial_str = input("Enter the initial state row-wise (space-separated): ")
    final_str = input("Enter the final state row-wise (space-separated): ")

    initial = [list(map(int, initial_str.split()[i:i + 3])) for i in range(0, 9, 3)]
    final = [list(map(int, final_str.split()[i:i + 3])) for i in range(0, 9, 3)]

    return initial, final

# Get index of the empty space (represented by 0)
def find_empty(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

# Swap positions of two tiles
def swap(state, row1, col1, row2, col2):
    new_state = [row[:] for row in state]
    new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
    return new_state

# Generate all possible moves from the current state
def possible_moves(state):
    row, col = find_empty(state)
    moves = []

    if row > 0:  # Move up
        moves.append(swap(state, row, col, row - 1, col))
    if row < 2:  # Move down
        moves.append(swap(state, row, col, row + 1, col))
    if col > 0:  # Move left
        moves.append(swap(state, row, col, row, col - 1))
    if col < 2:  # Move right
        moves.append(swap(state, row, col, row, col + 1))

    return moves

# BFS to find the solution
def BFS():
    initial, final = states()
    
    # Convert to tuple for immutability in sets
    initial = tuple(map(tuple, initial))
    final = tuple(map(tuple, final))

    # Queue holds (current_state, path_taken)
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        # If we've already visited this state, skip it
        if current in visited:
            continue
        
        visited.add(current)

        # Check if this is the solution
        if current == final:
            return path + [current]

        # Explore possible moves
        for move in possible_moves([list(row) for row in current]):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                queue.append((move_tuple, path + [current]))

    return None

# Print the solution
solution = BFS()
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
from collections import deque

# Get initial and final states from the user
def states():
    initial_str = input("Enter the initial state row-wise (space-separated): ")
    final_str = input("Enter the final state row-wise (space-separated): ")

    initial = [list(map(int, initial_str.split()[i:i + 3])) for i in range(0, 9, 3)]
    final = [list(map(int, final_str.split()[i:i + 3])) for i in range(0, 9, 3)]

    return initial, final

# Get index of the empty space (represented by 0)
def find_empty(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

# Swap positions of two tiles
def swap(state, row1, col1, row2, col2):
    new_state = [row[:] for row in state]
    new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
    return new_state

# Generate all possible moves from the current state
def possible_moves(state):
    row, col = find_empty(state)
    moves = []

    if row > 0:  # Move up
        moves.append(swap(state, row, col, row - 1, col))
    if row < 2:  # Move down
        moves.append(swap(state, row, col, row + 1, col))
    if col > 0:  # Move left
        moves.append(swap(state, row, col, row, col - 1))
    if col < 2:  # Move right
        moves.append(swap(state, row, col, row, col + 1))

    return moves

# BFS to find the solution
def BFS():
    initial, final = states()
    
    # Convert to tuple for immutability in sets
    initial = tuple(map(tuple, initial))
    final = tuple(map(tuple, final))

    # Queue holds (current_state, path_taken)
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        # If we've already visited this state, skip it
        if current in visited:
            continue
        
        visited.add(current)

        # Check if this is the solution
        if current == final:
            return path + [current]

        # Explore possible moves
        for move in possible_moves([list(row) for row in current]):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                queue.append((move_tuple, path + [current]))

    return None

# Print the solution
solution = BFS()
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
from collections import deque

# Get initial and final states from the user
def states():
    initial_str = input("Enter the initial state row-wise (space-separated): ")
    final_str = input("Enter the final state row-wise (space-separated): ")

    initial = [list(map(int, initial_str.split()[i:i + 3])) for i in range(0, 9, 3)]
    final = [list(map(int, final_str.split()[i:i + 3])) for i in range(0, 9, 3)]

    return initial, final

# Get index of the empty space (represented by 0)
def find_empty(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

# Swap positions of two tiles
def swap(state, row1, col1, row2, col2):
    new_state = [row[:] for row in state]
    new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
    return new_state

# Generate all possible moves from the current state
def possible_moves(state):
    row, col = find_empty(state)
    moves = []

    if row > 0:  # Move up
        moves.append(swap(state, row, col, row - 1, col))
    if row < 2:  # Move down
        moves.append(swap(state, row, col, row + 1, col))
    if col > 0:  # Move left
        moves.append(swap(state, row, col, row, col - 1))
    if col < 2:  # Move right
        moves.append(swap(state, row, col, row, col + 1))

    return moves

# BFS to find the solution
def BFS():
    initial, final = states()
    
    # Convert to tuple for immutability in sets
    initial = tuple(map(tuple, initial))
    final = tuple(map(tuple, final))

    # Queue holds (current_state, path_taken)
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        # If we've already visited this state, skip it
        if current in visited:
            continue
        
        visited.add(current)

        # Check if this is the solution
        if current == final:
            return path + [current]

        # Explore possible moves
        for move in possible_moves([list(row) for row in current]):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                queue.append((move_tuple, path + [current]))

    return None

# Print the solution
solution = BFS()
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
from collections import deque

# Get initial and final states from the user
def states():
    initial_str = input("Enter the initial state row-wise (space-separated): ")
    final_str = input("Enter the final state row-wise (space-separated): ")

    initial = [list(map(int, initial_str.split()[i:i + 3])) for i in range(0, 9, 3)]
    final = [list(map(int, final_str.split()[i:i + 3])) for i in range(0, 9, 3)]

    return initial, final

# Get index of the empty space (represented by 0)
def find_empty(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

# Swap positions of two tiles
def swap(state, row1, col1, row2, col2):
    new_state = [row[:] for row in state]
    new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
    return new_state

# Generate all possible moves from the current state
def possible_moves(state):
    row, col = find_empty(state)
    moves = []

    if row > 0:  # Move up
        moves.append(swap(state, row, col, row - 1, col))
    if row < 2:  # Move down
        moves.append(swap(state, row, col, row + 1, col))
    if col > 0:  # Move left
        moves.append(swap(state, row, col, row, col - 1))
    if col < 2:  # Move right
        moves.append(swap(state, row, col, row, col + 1))

    return moves

# BFS to find the solution
def BFS():
    initial, final = states()
    
    # Convert to tuple for immutability in sets
    initial = tuple(map(tuple, initial))
    final = tuple(map(tuple, final))

    # Queue holds (current_state, path_taken)
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        # If we've already visited this state, skip it
        if current in visited:
            continue
        
        visited.add(current)

        # Check if this is the solution
        if current == final:
            return path + [current]

        # Explore possible moves
        for move in possible_moves([list(row) for row in current]):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                queue.append((move_tuple, path + [current]))

    return None

# Print the solution
solution = BFS()
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
from collections import deque

# Get initial and final states from the user
def states():
    initial_str = input("Enter the initial state row-wise (space-separated): ")
    final_str = input("Enter the final state row-wise (space-separated): ")

    initial = [list(map(int, initial_str.split()[i:i + 3])) for i in range(0, 9, 3)]
    final = [list(map(int, final_str.split()[i:i + 3])) for i in range(0, 9, 3)]

    return initial, final

# Get index of the empty space (represented by 0)
def find_empty(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

# Swap positions of two tiles
def swap(state, row1, col1, row2, col2):
    new_state = [row[:] for row in state]
    new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
    return new_state

# Generate all possible moves from the current state
def possible_moves(state):
    row, col = find_empty(state)
    moves = []

    if row > 0:  # Move up
        moves.append(swap(state, row, col, row - 1, col))
    if row < 2:  # Move down
        moves.append(swap(state, row, col, row + 1, col))
    if col > 0:  # Move left
        moves.append(swap(state, row, col, row, col - 1))
    if col < 2:  # Move right
        moves.append(swap(state, row, col, row, col + 1))

    return moves

# BFS to find the solution
def BFS():
    initial, final = states()
    
    # Convert to tuple for immutability in sets
    initial = tuple(map(tuple, initial))
    final = tuple(map(tuple, final))

    # Queue holds (current_state, path_taken)
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        # If we've already visited this state, skip it
        if current in visited:
            continue
        
        visited.add(current)

        # Check if this is the solution
        if current == final:
            return path + [current]

        # Explore possible moves
        for move in possible_moves([list(row) for row in current]):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                queue.append((move_tuple, path + [current]))

    return None

# Print the solution
solution = BFS()
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
