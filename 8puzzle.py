from collections import deque
def states():
    intial = (input("Enter the initail state rowwiswe(list):"))
    final = (input("Enter the initail state rowwiswe(list):"))
    for i in range(len(intial)):
        for j in range(len(intial[i])):
            if intial[i][j] not in [1,2,3,4,5,6,7,8]:
                intial[i][j]='#'
            if final[i][j] not in [1,2,3,4,5,7,8]:
                final[i][j]='#'
    return intial,final
def possible_move(current):
    move=[]
    hash_index,i=find_hash_index(current)
    if current[i]!=0:
        move.append(up(current))
    elif current[i]!=2:
        move.append(down(current))
    elif hash_index!=2:
        move.append(left(current))
    elif hash_index!=0:
        move.append(right(current))
def find_hash_index(current):
        for i in range(len(current)):
            hash_index=current[i].index('#')
        return hash_index,i
def up(current):
    hash_index,i=find_hash_index(current)
    current[i-1][hash_index],current[i][hash_index]= current[i][hash_index],current[i-1][hash_index]
    return current,True
def down(current):
    hash_index,i=find_hash_index(current)
    current[i+1][hash_index],current[i][hash_index]= current[i][hash_index],current[i+1][hash_index]
    return current,True
def left(current):
    hash_index,i=find_hash_index(current)
    current[i][hash_index+1],current[i][hash_index]= current[i][hash_index],current[i][hash_index+1]
    return current,True
def right(current):
    hash_index,i=find_hash_index(current)
    current[i][hash_index-1],current[i][hash_index]= current[i][hash_index],current[i][hash_index-1]
    return current,True
def are_2d_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    for sublist1, sublist2 in zip(list1, list2):
        if len(sublist1) != len(sublist2):
            return False
        for item1, item2 in zip(sublist1, sublist2):
            if item1 != item2:
                return False
    return True

def BFS():
    initial,final=states()
    visited = set()        
    queue = deque(initial)  
    result = []            
    while queue:
        node = queue.popleft()  
        if node not in visited:
            moves=possible_move(node)
            
            visited.add(node)    # Mark the node as visited
            result.append(node)  # Add the node to the result list
            # Add all unvisited adjacent nodes to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result
states()