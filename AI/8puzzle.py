from collections import deque

def states():
    initial_str = input("Enter the initial state row-wise (space-separated): ")
    final_str = input("Enter the final state row-wise (space-separated): ")

    initial = [list(map(int, initial_str.split()[i:i + 3])) for i in range(0, 9, 3)]
    final = [list(map(int, final_str.split()[i:i + 3])) for i in range(0, 9, 3)]

    return initial, final

def possible_move(current):
    moves = []
    hash_index, i = find_hash_index(current)
    if i > 0:  # Can move up
        moves.append(up(current))
    if i < len(current) - 1:  # Can move down
        moves.append(down(current))
    if hash_index > 0:  # Can move left
        moves.append(left(current))
    if hash_index < len(current[i]) - 1:  # Can move right
        moves.append(right(current))
    return moves

def find_hash_index(current):
    for i in range(len(current)):
        if 0 in current[i]:  # Assuming 0 represents the empty space
            hash_index = current[i].index(0)
            return hash_index, i

def up(current):
    new_state = [row[:] for row in current]
    hash_index, i = find_hash_index(new_state)
    new_state[i][hash_index], new_state[i-1][hash_index] = new_state[i-1][hash_index], new_state[i][hash_index]
    return new_state

def down(current):
    new_state = [row[:] for row in current]
    hash_index, i = find_hash_index(new_state)
    new_state[i][hash_index], new_state[i+1][hash_index] = new_state[i+1][hash_index], new_state[i][hash_index]
    return new_state

def left(current):
    new_state = [row[:] for row in current]
    hash_index, i = find_hash_index(new_state)
    new_state[i][hash_index], new_state[i][hash_index-1] = new_state[i][hash_index-1], new_state[i][hash_index]
    return new_state

def right(current):
    new_state = [row[:] for row in current]
    hash_index, i = find_hash_index(new_state)
    new_state[i][hash_index], new_state[i][hash_index+1] = new_state[i][hash_index+1], new_state[i][hash_index]
    return new_state

def are_2d_lists_equal(list1, list2):
    return list1 == list2

def BFS():
    initial, final = states()
    initial = tuple(map(tuple, initial))
    final = tuple(map(tuple, final))

    visited = set()
    queue = deque([(initial, [])])

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue
        
        visited.add(current)

        if current == final:
            return path + [current]

        for move in possible_move(list(map(list, current))):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                queue.append((move_tuple, path + [current]))

    return None

solution = BFS()
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
