import graph_data
import global_game_data
from numpy import random

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

        print("current: " + str(current) + "\n")
        print("  current_ind: " + str(current_ind) + "\n")

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

    print("path: " + str(path) + "\n")
    assert path is not None
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
