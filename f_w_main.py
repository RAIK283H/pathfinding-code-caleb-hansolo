import global_game_data
import graph_data
import f_w

if __name__ == '__main__':
    # edi graph index to test different graphs
    global_game_data.current_graph_index = 10
    # curr_graph = graph_data.graph_data[global_game_data.current_graph_index]

    # run floyd warshall on current graph
    paths = f_w.floyd_warshall()

    # display results    
    print(paths)