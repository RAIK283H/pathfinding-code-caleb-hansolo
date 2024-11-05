import graph_data
import permutation

if __name__ == '__main__':
    # run code to calculate cycles
    graph_index = 9
    curr_graph = graph_data.graph_data[graph_index]
    cycles = permutation.get_hamiltonian_cycles(curr_graph)
    
    # display results
    print()
    if cycles == False:
        print("No cycles found")
    else:
        print("Found " + str(len(cycles)) + " valid cycles: ")
        for cycle in cycles:
            print("   " + str(cycle))
