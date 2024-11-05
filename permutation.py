import graph_data
import global_game_data
from numpy import random
import math

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
        if (is_hamiltonian_cycle(perm, graph)):
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

    # initialize current permutation
    current = set
    perms.append(current)

    # implement Steinhaus–Johnson–Trotter algorithm

    # will repreat n! times since thats how many perms there are
    for i in range(1, math.factorial(n)):
        # find next permutation

        # first find largest mobile integer
        mobile_int = get_mobile_int(current, directions, n)
        # find position of mobile integer in the per
        position = current.index(mobile_int)

        # if mobile int points left, swap mobile and the int to the left of it
        if (directions[current[position] - 1] == point_left):
            temp = current[position]
            current[position] = current[position - 1]
            current[position - 1] = temp

        # if mobile int points right, swap mobile and the int to the right of it
        else:
            temp = current[position]
            current[position] = current[position + 1]
            current[position + 1] = temp

        # update direction of mobile integer
        for i in range(n):
            if (current[i] > mobile_int):
                directions[current[i] - 1] = not directions[current[i] - 1]

        for i in range(n):  
            print(current[i], end = " ")

        print("")

        # add current permutation to perms
        new_perm = []
        for i in range(n):
            new_perm.append(current[i])
        perms.append(new_perm)


    return perms


def get_mobile_int(perm, directions, n):
    # returns the next mobile integer in the permutation
    # perm is a list of ints
    assert perm is not None

    prev = 0
    curr = 0

    for i in range(n):
        # if the direction is True and i isnt first element, go left
        if (directions[perm[i] - 1] == True and i != 0):
            if (perm[i] > perm[i - 1] and perm[i] > prev):
                curr = perm[i]
                prev = curr
        # if the direction is False and i isnt last element, go right
        elif (directions[perm[i] - 1] == False and i != n - 1):
            if (perm[i] > perm[i + 1] and perm[i] > prev):
                curr = perm[i]
                prev = curr
    
    return curr


def is_hamiltonian_cycle(perm, graph):
    assert perm is not None

    # ensure that the first and last elements in the permutation are adjacent
    if (perm[0] not in graph[perm[len(perm) - 1]][1]):
        print("FIRST AND LAST NOT NEIGHBORS: " + str(perm))
        return False

    # ensure that all adjacent elements in the permutation are adjacent in the graph
    for i in range(len(perm) - 1):
        if (perm[i + 1] not in graph[perm[i]][1]):
            print("   NOT NEIGHBORS: " + str(perm))
            return False

    return True

