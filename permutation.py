import graph_data
import global_game_data
from numpy import random

def get_hamiltonian_cycles(graph):
    assert graph is not None
    # in hamiltonian cycles, the first node in the cycle must be adjacent to the last
    # use input set of numbers (besides start and end nodes)
    set = [i for i in range(1, len(graph) - 1)]

    # use sjt to find all permutations of set
    perms = sjt(set)

    # make list of valid cycles
    cycles = []

    # test each permutation to see if it is a valid hamiltonian cycle
    for perm in perms:
        if is_hamiltonian_cycle(perm):
            global_game_data.graph_paths.append(perm)
            cycles.append(perm)
    
    return cycles


def sjt(set):
    assert set is not None
    # returns all permutations of set
    perms = []

    # length of set is n
    n = len(set)

    # True is pointing left, False is pointing right
    point_left = True
    point_right = False
    directions = [point_left for i in range(n)]


    # implement Steinhaus–Johnson–Trotter algorithm
    

    return perms


def is_hamiltonian_cycle(perms, graph):
    assert perms is not None

    # ensure that the first and last elements in the permutation are adjacent
    if (perms[0] not in graph[perms[len(perms) - 1]][1]):
        return False

    # ensure that all adjacent elements in the permutation are adjacent in the graph
    for i in range(len(perms) - 1):
        if (perms[i + 1] not in graph[perms[i]][1]):
            return False

    return True

