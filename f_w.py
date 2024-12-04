import graph_data
import global_game_data
import math



def convert_to_adj_matrix(graph):
    # initialize adj matrix with all 0's
    n = len(graph)
    adj = [[0] * n for _ in range(n)]

    # fill in adj matrix
    for node in range(n):
        # for each neighbor of the ith node
        for neighbor in graph[node][1]:
            # print ("node: " + str(node) + " neighbor: " + str(neighbor))
            # set adj[i][j] to euclidean distance between the two nodes
            current_x = graph[node][0][0]
            current_y = graph[node][0][1]
            current_coords = [current_x, current_y]
            neighbor_x = graph[neighbor][0][0]
            neighbor_y = graph[neighbor][0][1]
            neighbor_coords = [neighbor_x, neighbor_y]
            distance = math.dist(current_coords, neighbor_coords)
            # add distance to adj
            adj[node][neighbor] = distance

    return adj

def floyd_warshall():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    adjacency_matrix = convert_to_adj_matrix(graph)
    

    return adjacency_matrix