import graph_data
import global_game_data
import math

def convert_to_adj_matrix(graph):
    n = len(graph)
    adj = [[0] * n] * n
    print(adj)

    return adj

def floyd_warshall():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    adjacency_matrix = convert_to_adj_matrix(graph)
    return