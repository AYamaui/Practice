import unittest
import sys
sys.path.append('../')
import binary_search_iterative
import binary_search_recursive


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.number = 9

    def test_element_in_even_list(self):
        array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
        self.assertEqual(binary_search_iterative.binary_search(array, 16), 8)
        self.assertEqual(binary_search_recursive.binary_search(0, len(array) - 1, array, 16), 8)

    def test_element_in_odd_list(self):
        array = [0, 2, 4, 6, 8, 10, 12, 14, 16]
        self.assertEqual(binary_search_iterative.binary_search(array, 4), 2)
        self.assertEqual(binary_search_recursive.binary_search(0, len(array) - 1, array, 4), 2)

    def test_element_not_in_list(self):
        array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
        self.assertEqual(binary_search_iterative.binary_search(array, self.number), -1)
        self.assertEqual(binary_search_recursive.binary_search(0, len(array) - 1, array, self.number), -1)

    def test_single_element_list(self):
        array = [0]
        self.assertEqual(binary_search_iterative.binary_search(array, self.number), -1)
        self.assertEqual(binary_search_recursive.binary_search(0, len(array) - 1, array, self.number), -1)

    def test_element_in_first_position(self):
        array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
        self.assertEqual(binary_search_iterative.binary_search(array, 0), 0)
        self.assertEqual(binary_search_recursive.binary_search(0, len(array) - 1, array, 0), 0)

    def test_element_in_last_position(self):
        array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
        self.assertEqual(binary_search_iterative.binary_search(array, 18), 9)
        self.assertEqual(binary_search_recursive.binary_search(0, len(array) - 1, array, 18), 9)

    def test_empty_list(self):
        array = []
        self.assertEqual(binary_search_iterative.binary_search(array, self.number), -1)
        self.assertEqual(binary_search_recursive.binary_search(0, len(array) - 1, array, self.number), -1)


if __name__ == '__main__':
    unittest.main()
