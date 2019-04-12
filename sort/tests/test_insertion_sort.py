import unittest
import sys
sys.path.append('../')
import insertion_sort


class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        array = []
        self.assertEqual(insertion_sort.insertion_sort(array), [])

    def test_sorted_list(self):
        array = [1, 3, 6, 10, 12, 28]
        self.assertEqual(insertion_sort.insertion_sort(array), [1, 3, 6, 10, 12, 28])

    def test_descending_sorted_list(self):
        array = [28, 12, 10, 6, 3, 1]
        self.assertEqual(insertion_sort.insertion_sort(array), [1, 3, 6, 10, 12, 28])

    def test_unordered_list(self):
        array = [12, 28, 3, 6, 10, 1]
        self.assertEqual(insertion_sort.insertion_sort(array), [1, 3, 6, 10, 12, 28])


if __name__ == '__main__':
    unittest.main()
