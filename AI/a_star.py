import heapq

def a_star_search(initial_state, target_state, heuristic_func):
    frontier = []
    heapq.heappush(frontier, (0, initial_state))
    movement_cost = {initial_state: 0}
    trace_path = {initial_state: None}
    visited = set()

    while frontier:
        current_total_cost, current_state = heapq.heappop(frontier)

        if current_state in visited:
            continue
        
        visited.add(current_state)

        current_g_cost = movement_cost[current_state]
        current_h_cost = heuristic_func(current_state, target_state)
        print(f"Evaluating State with g(x) = {current_g_cost}, h(x) = {current_h_cost}, f(x) = {current_total_cost}:")
        display_state(current_state, current_g_cost, current_h_cost, current_total_cost)

        if current_state == target_state:
            print("Target reached!")
            return build_path(trace_path, target_state)

        for neighbor in generate_neighbors(current_state):
            tentative_g_cost = movement_cost[current_state] + 1

            if neighbor not in movement_cost or tentative_g_cost < movement_cost[neighbor]:
                movement_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic_func(neighbor, target_state)
                if neighbor not in visited:
                    heapq.heappush(frontier, (f_cost, neighbor))
                    trace_path[neighbor] = current_state

    print("No valid path to the target")
    return None

def misplaced_tiles_heuristic(current_state, target_state):
    return sum(1 for curr_tile, target_tile in zip(current_state, target_state) if curr_tile != target_tile and curr_tile != 0)

def manhattan_distance_heuristic(current_state, target_state):
    def compute_manhattan_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    current_positions = {value: (idx // 3, idx % 3) for idx, value in enumerate(current_state)}
    target_positions = {value: (idx // 3, idx % 3) for idx, value in enumerate(target_state)}

    return sum(compute_manhattan_distance(current_positions[val], target_positions[val]) for val in range(1, 9))

def generate_neighbors(current_state):
    neighbor_list = []
    empty_tile_idx = current_state.index(0)
    row, col = divmod(empty_tile_idx, 3)
    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in possible_moves:
        new_row, new_col = row + move[0], col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            new_state = list(current_state)
            new_state[empty_tile_idx], new_state[new_blank_idx] = new_state[new_blank_idx], new_state[empty_tile_idx]
            neighbor_list.append(tuple(new_state))

    return neighbor_list

def build_path(trace_path, target_state):
    path = []
    current_state = target_state
    while current_state:
        path.append(current_state)
        current_state = trace_path[current_state]
    path.reverse()
    return path

def display_state(state, g_cost, h_cost, f_cost):
    if g_cost is not None and h_cost is not None and f_cost is not None:
        print(f"g(x) = {g_cost}, h(x) = {h_cost}, f(x) = {f_cost}")
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()

initial_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)
target_state = (8, 1, 3, 0, 2, 4, 7, 6, 5)

print("Heuristic: Misplaced Tiles")
a_star_search(initial_state, target_state, misplaced_tiles_heuristic)

