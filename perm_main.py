import graph_data
import permutation

if __name__ == '__main__':
    graph_index = 2
    curr_graph = graph_data.graph_data[graph_index]
    cycles = permutation.get_hamiltonian_cycles(curr_graph)
    print(cycles)
