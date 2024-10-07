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
    # graph = graph_data.graph_data[0]
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    # start at start node (index 0)
    start = graph[0]
    # end node is last node (index len - 1)
    end = graph[len(graph) - 1]
    # target is target_node
    target = global_game_data.target_node[global_game_data.current_graph_index]

    # path and current variables
    current = start
    past = start
    path = []
    path.append(start)
    
    # while path hasn't been found
    targetFound = False
    pathFound = False
    while not pathFound:
        # start from start, make random moves until at end, then check if target has been reached. If not, repeat process

        # look at current's adjacency list, pick random node, then make that current node
        random_index = random.randint(0, len(current[1]))
        # make a past variable so that current doesnt become the one it was just previously at
        real_past = past
        past = current 
        current = graph[current[1][random_index]]
        # make sure current isnt backtracking by one IF it has enough space to do so
        while current != real_past and len(current[1]) > 1:
            # re-reandomize
            random_index = random.randint(0, len(past[1]))
            current = graph[current[1][random_index]]

        # append current node to path
        path.append(current)

        # if target node found
        if current == target:
            targetFound = True

        if current == end and targetFound:
            pathFound = True

    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
