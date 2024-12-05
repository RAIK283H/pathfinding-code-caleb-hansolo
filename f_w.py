import graph_data
import global_game_data
import math



def convert_to_adj_matrix(graph):
    # initialize adj matrix with all 0's
    n = len(graph)
    adj = [[math.inf] * n for _ in range(n)]

    # fill in adj matrix
    for node in range(n):
        # for each neighbor of the ith node
        adj[node][node] = 0
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


def get_path(prev, start, end):
    if prev[start][end] == None:
        return []
    path = [end]
    while start != end:
        end = prev[start][end]
        path.insert(0, end)
    path.pop(0)
    return path

def floyd_warshall():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    # initialize distance matrix
    dist = convert_to_adj_matrix(graph)
    n = len(graph)

    # initialize and fill prev matrix
    prev = [[None] * n for _ in range(n)]

    # fill in prev matrix
    for node in range(n):
        for neighbor in range(n):
            prev[node][neighbor] = node
    
    for node in range(n):
        prev[node][node] = node
        dist[node][node] = 0

    # floyd warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]

    # get path
    path = get_path(prev, 0, n - 1)

    print("Path: " + str(path))

    return path

