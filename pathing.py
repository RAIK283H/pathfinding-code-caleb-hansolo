import graph_data
import global_game_data
from numpy import random
import node
import heapq as heap
import math

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    assert graph_data is not None
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    # start at start node (index 0)
    start = graph[0]
    start_ind = 0
    # end node is last node (index len - 1)
    end = graph[len(graph) - 1]
    end_ind = len(graph) - 1
    # target is target_node
    target = global_game_data.target_node[global_game_data.current_graph_index]
    assert target is not None

    # path and current variables
    current = start
    current_ind = 0
    past = start
    past_ind = 0
    path = []
    path.append(start_ind)
    
    # while path hasn't been found
    targetFound = False
    pathFound = False
    while not pathFound:
        # start from start, make random moves until at end, then check if target has been reached. If not, repeat process

        # # look at current's adjacency list, pick random node, then make that current node
        # random_index = random.randint(0, len(current[1]))
        # # make a past variable so that current doesnt become the one it was just previously at
        # real_past_ind = past_ind
        # past = current
        # past_ind = current_ind 
        # current = graph[current[1][random_index]]
        # current_ind = random_index
        # print("current BEFORE alteration: " + str(current) + "\n")
        # # make sure current isnt backtracking by one IF it has enough space to do so
        # while current_ind != real_past_ind and len(current[1]) > 1:
        #     # re-reandomize
        #     print("   RANDOMIZING current: " + str(current) + "\n")
        #     random_index = random.randint(0, len(past[1]))
        #     current = graph[current[1][random_index]]
        #     current_ind = random_index
        # print("current AFTER alteration: " + str(current) + "\n")
        random_index = random.randint(0, len(current[1]))
        current_ind = int(current[1][random_index])
        current = graph[current_ind]

        # print("current: " + str(current) + "\n")
        # print("  current_ind: " + str(current_ind) + "\n")

        # append current node to path
        assert current is not None
        assert current_ind is not None
        path.append(current_ind)

        # if target node found
        if current_ind == target:
            targetFound = True

        # if reached end and target has been found
        if current_ind == end_ind and targetFound:
            pathFound = True

    # print("path: " + str(path) + "\n")
    assert path is not None
    return path


def get_dfs_path():
    assert graph_data is not None
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    # start at start node (index 0)
    start_ind = 0
    # end node is last node (index len - 1)
    end_ind = len(graph) - 1
    # target is target_node (gives target node's index)
    target = global_game_data.target_node[global_game_data.current_graph_index]
    assert target is not None

    # path and current variables
    path = [] # final path
    parents = {} # dictionary of nodes as keys and their parent as values
    parents[start_ind] = -1
    visited = [] # list of nodes that have been visited
    stack = []
    stack.append(start_ind)
    current_ind = 0

    # while stack isn't empty and target has not been found
    while len(stack) != 0:
        current_ind = stack.pop()
        assert current_ind is not None
        if current_ind == target:
            break
        # if current node not yet visited
        if not current_ind in visited:
            # add current node to visited
            visited.append(current_ind)
            # add current node's neighbors to stack
            for neighbor in graph[current_ind][1]:
                # add node to stack if unvisited
                if not neighbor in visited:
                    stack.append(neighbor)
                    # add neighbor node to parents, and make current node's index its parent
                    parents[neighbor] = current_ind
                    print(parents)


    # for assertion making sure each consecutive node is connected by an edge
    edge_parents = parents.copy()

    # add the path from start to target to the path array
    path = get_path_from_parents(start_ind, target, parents)

    stack = [target]
    visited = [target]
    parents = {}
    parents[target] = -1

    # DFS from target to the end
    while len(stack) != 0:
        current_ind = stack.pop()
        assert current_ind is not None
        if current_ind == end_ind:
            break
        for neighbor in graph[current_ind][1]:
            if not neighbor in visited:
                visited.append(neighbor)
                stack.append(neighbor)
                parents[neighbor] = current_ind
                edge_parents[neighbor] = current_ind
                print(parents)

    # add the path from target to end to the path array
    path = path + get_path_from_parents(target, end_ind, parents)

    # ASSERTIONS:

    # Postcondition: Result path includes the target node
    assert target in path
    # Postcondition: Result path ends at the exit node
    assert path[len(path) - 1] == end_ind
    # Postcondition: Every pair of sequential vertices in the path are connected by an edge
    # just check that every node in path has a parent, meaning they are connected
    for i in range(len(path) - 1):
        assert path[i] in edge_parents


    return path


def get_bfs_path():
    assert graph_data is not None
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    # start at start node (index 0)
    start_ind = 0
    # end node is last node (index len - 1)
    end_ind = len(graph) - 1
    # target is target_node (gives target node's index)
    target = global_game_data.target_node[global_game_data.current_graph_index]
    assert target is not None

    # path and current variables
    path = [] # final path
    parents = {} # dictionary of nodes as keys and their parent as values
    parents[start_ind] = -1
    visited = [] # list of nodes that have been visited
    queue = []
    queue.append(start_ind)
    visited.append(start_ind)
    current_ind = 0

    while len(queue) != 0:
        current_ind = queue.pop(0)
        assert current_ind is not None
        if current_ind == target:
            break
        # go through current node's neighbors
        for neighbor in graph[current_ind][1]:
            # add neighbor node to queue if unvisited
            if not neighbor in visited:
                # add node to visited
                visited.append(neighbor)
                queue.append(neighbor)
                # add neighbor node to parents, and make current node's index its parent
                parents[neighbor] = current_ind
                print(parents)

    # for assertion making sure each consecutive node is connected by an edge
    edge_parents = parents.copy()

    # add the path from start to target to the path array
    path = get_path_from_parents(start_ind, target, parents)

    queue = [target]
    visited = [target]
    parents = {}
    parents[target] = -1

    # BFS from target to the end
    while len(queue) != 0:
        current_ind = queue.pop(0)
        assert current_ind is not None
        # if end is reached, break
        if current_ind == end_ind:
            break
        for neighbor in graph[current_ind][1]:
            if not neighbor in visited:
                queue.append(neighbor)
                visited.append(current_ind)
                parents[neighbor] = current_ind
                edge_parents[neighbor] = current_ind
                print(parents)

    # add the path from target to end to the path array
    path = path + get_path_from_parents(target, end_ind, parents)

    # ASSERTIONS:

    # Postcondition: Result path includes the target node
    assert target in path
    # Postcondition: Result path ends at the exit node
    assert path[len(path) - 1] == end_ind
    # Postcondition: Every pair of sequential vertices in the path are connected by an edge
    # just check that every node in path has a parent, meaning they are connected
    for i in range(len(path) - 1):
        assert path[i] in edge_parents

    return path


def get_dijkstra_path():
    # BFS, but use a priority queue
    assert graph_data is not None
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    # start at start node (index 0)
    start_ind = 0
    # end node is last node (index len - 1)
    end_ind = len(graph) - 1
    # target is target_node (gives target node's index)
    target = global_game_data.target_node[global_game_data.current_graph_index]
    assert target is not None

    # path and current variables
    path = [] # final path
    parents = {} # dictionary of nodes as keys and their parent as values
    parents[start_ind] = -1
    visited = [] # list of nodes that have been visited
    frontier = [(0, start_ind)]
    heap.heapify(frontier)
    visited.append(start_ind)
    current_ind = 0

    while frontier:
        # get index of next element in the queue
        current_ind = heap.heappop(frontier)[1]
        # print(" goo goo gaga ",current_ind)
        # make sure current index exists
        assert current_ind is not None

        # if current index is target, break
        if current_ind == target:
            break
        
        # go through current node's neighbors
        for neighbor in graph[current_ind][1]:
            # add neighbor node to queue if unvisited
            if not neighbor in visited:
                # add cost to neighbor (distance from current node)
                current_x = graph[current_ind][0][0]
                current_y = graph[current_ind][0][1]
                current_coords = [current_x, current_y]
                print(" rah",current_coords)
                neighbor_x = graph[neighbor][0][0]
                neighbor_y = graph[neighbor][0][1]
                neighbor_coords = [neighbor_x, neighbor_y]
                print(neighbor_coords)
                cost = math.dist(current_coords, neighbor_coords)
                # add node to visited
                visited.append(neighbor)
                heap.heappush(frontier, (cost, neighbor))
                # add neighbor node to parents, and make current node's index its parent
                parents[neighbor] = current_ind
                print(parents)

    # for assertion making sure each consecutive node is connected by an edge
    edge_parents = parents.copy()

    # add the path from start to target to the path array
    path = get_path_from_parents(start_ind, target, parents)

    frontier = [(0, target)]
    heap.heapify(frontier)
    visited = [target]
    parents = {}
    parents[target] = -1

    # BFS from target to the end
    while frontier:
        # get index of next element in the queue
        current_ind = heap.heappop(frontier)[1]
        # make sure current index exists
        assert current_ind is not None

        # if end is reached, break
        if current_ind == end_ind:
            break

        for neighbor in graph[current_ind][1]:
            if not neighbor in visited:
                # add cost to neighbor (distance from current node)
                current_x = graph[current_ind][0][1]
                current_y = graph[current_ind][0][0]
                current_coords = [current_x, current_y]
                neighbor_x = graph[neighbor][0][1]
                neighbor_y = graph[neighbor][0][0]
                neighbor_coords = [neighbor_x, neighbor_y]
                cost = math.dist(current_coords, neighbor_coords)
                # add node to visited
                heap.heappush(frontier, (cost, neighbor))
                visited.append(current_ind)
                # add neighbor node to parents
                parents[neighbor] = current_ind
                edge_parents[neighbor] = current_ind
                print(parents)

    # add the path from target to end to the path array
    path = path + get_path_from_parents(target, end_ind, parents)

    # ASSERTIONS:

    # Postcondition: Result path includes the target node
    assert target in path
    # Postcondition: Result path ends at the exit node
    assert path[len(path) - 1] == end_ind
    # Postcondition: Every pair of sequential vertices in the path are connected by an edge
    # just check that every node in path has a parent, meaning they are connected
    for i in range(len(path) - 1):
        assert path[i] in edge_parents

    return path


def get_path_from_parents(start, end, parents):
    # creates path from start to end using dictionary of parent nodes
    path = []
    current = end

    print("start: " + str(start))
    print("end: " + str(end))
    # while current node has a parent and isn't the start, put the parents down in path (this is in reverse order)
    while current in parents and current >= 0:
        path.append(current)
        current = parents[current]

    # get rid of last (start) node, it is a repeat
    path.pop()
    # reverse path
    path.reverse()

    print(path)

    return path
