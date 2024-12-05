import math
import unittest
import pathing
import graph_data
import global_game_data
import permutation
import f_w


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
    
    # writing test to make sure path from start to end is correct and not empty on dfs
    def test_get_dfs_path(self):
        # set up
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [1, 2]
        expected_path = [1, 2]
        # test
        path = pathing.get_dfs_path()
        # assert
        self.assertEqual(expected_path, path)

    # writing test to make sure path from start to end is correct and not empty on bfs
    def test_get_bfs_path(self):
        # set up
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [1, 2]
        expected_path = [1, 2]
        # test
        path = pathing.get_bfs_path()
        # assert
        self.assertEqual(expected_path, path)


    # SJT AND HAMILTONIAN CYCLE TESTS
    def test_get_hamiltonian_cycles_with_no_cycle(self):
        # set up
        graph = graph_data.graph_data[11]
        global_game_data.current_graph_index = 11
        global_game_data.target_node = [1, 2]
        expected_cycles = False
        # test
        cycles = permutation.get_hamiltonian_cycles(graph)
        # assert
        self.assertEqual(expected_cycles, cycles)

    def test_get_hamiltonian_cycles_with_cycles(self):
        # set up
        graph = graph_data.graph_data[10]
        global_game_data.current_graph_index = 10
        global_game_data.target_node = [1, 2]
        expected_cycles = [[1, 2, 3, 4],
                            [4, 1, 2, 3],
                            [1, 4, 3, 2],
                            [3, 4, 1, 2],
                            [4, 3, 2, 1],
                            [3, 2, 1, 4],
                            [2, 3, 4, 1],
                            [2, 1, 4, 3]]
        # test
        cycles = permutation.get_hamiltonian_cycles(graph)
        # assert
        self.assertEqual(expected_cycles, cycles)

    def test_get_hamiltonian_cycles_contains_a_single_cycle(self):
        # set up
        graph = graph_data.graph_data[9]
        global_game_data.current_graph_index = 9
        global_game_data.target_node = [1, 2]
        expected_cycle = [6, 7, 3, 2, 1, 5, 4]
        # test
        cycles = permutation.get_hamiltonian_cycles(graph)
        # assert
        contains_cycle = cycles.__contains__(expected_cycle)
        self.assertTrue(contains_cycle)

    
    def test_sjt(self):
        # set up
        set = [i for i in range(1, 4)]
        expected_perms = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
        # test
        perms = permutation.sjt(set)
        # assert
        self.assertEqual(expected_perms, perms)

    def test_is_hamiltonian_cycle(self):
        # set up
        perm = [1, 2, 3, 4]
        graph = graph_data.graph_data[10]
        expected_result = True
        # test
        result = permutation.is_hamiltonian_cycle(perm, graph)
        # assert
        self.assertEqual(expected_result, result)

    def test_get_mobile_int_ordered_permutation(self):
        # set up
        perm = [1, 2, 3, 4, 5]
        directions = [True, True, False, False, True]
        expected_result = 5
        # test
        result = permutation.get_mobile_int(perm, directions, len(perm))
        # assert
        self.assertEqual(expected_result, result)

    
    def test_get_mobile_int_unordered_permutation(self):
        # set up
        perm = [5, 4, 3, 2, 1]
        directions = [True, True, False, False, True]
        expected_result = 4
        # test
        result = permutation.get_mobile_int(perm, directions, len(perm))
        # assert
        self.assertEqual(expected_result, result)

    def test_get_mobile_int_with_no_mobile_int(self):
        # set up
        perm = [2, 1, 3, 4, 5]
        directions = [True, True, False, False, False]
        expected_result = 0
        # test
        result = permutation.get_mobile_int(perm, directions, len(perm))
        # assert
        self.assertEqual(expected_result, result)
        

    # DJIKSTRA'S TESTS
    def test_get_simple_dijkstra_path(self):
        # set up
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [1, 2]
        expected_path = [1, 2]
        # test
        path = pathing.get_dijkstra_path()
        # assert
        self.assertEqual(expected_path, path)

    def test_get_more_complex_dijkstra_path(self):
        # set up 
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [21, 21, 21]
        expected_path = [21, 23]
        # test
        path = pathing.get_dijkstra_path()
        # assert
        self.assertEqual(expected_path, path)

    def test_get_even_more_complex_dijkstra_path(self):
        # set up 
        global_game_data.current_graph_index = 7
        global_game_data.target_node = [6, 6, 6, 6, 6, 6, 6, 6]
        expected_path = [1, 3, 5, 6, 5, 9]
        # test
        path = pathing.get_dijkstra_path()
        # assert
        self.assertEqual(expected_path, path)

    def test_get_dijkstra_path_with_confusing_path(self):
        # set up 
        global_game_data.current_graph_index = 12
        global_game_data.target_node = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        expected_path = [1, 4, 5, 1, 4, 6]
        # test
        path = pathing.get_dijkstra_path()
        # assert
        self.assertEqual(expected_path, path)

    
    # FLOYD WARSHALL UNIT TESTS
    def test_get_floyd_warshall_simple_path(self):
        # set up
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [1, 2]
        expected_path = [1, 2]
        # test
        path = f_w.floyd_warshall()
        # assert
        self.assertEqual(expected_path, path)

    def test_get_floyd_warshall_complex_path(self):
        # set up
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [21, 21, 21]
        expected_path = [17, 18, 23]
        # test
        path = f_w.floyd_warshall()
        # assert
        self.assertEqual(expected_path, path)

    def test_get_floyd_warshall_complex_path_2(self):
        # set up
        global_game_data.current_graph_index = 5
        global_game_data.target_node = [6, 6, 6, 6, 6, 6]
        expected_path = [1, 2, 3, 6, 9, 15]
        # test
        path = f_w.floyd_warshall()
        # assert
        self.assertEqual(expected_path, path)

if __name__ == '__main__':
    unittest.main()
