import unittest
import sys
sys.path.append('../')
import list


class TestList(unittest.TestCase):

    def setUp(self):
        self.array = list.List()
        self.array.append(3)
        self.array.append(22)
        self.array.append(143)
        self.array.append(2)
        self.array.append(90)
        self.array.append(11)
        self.array.append(8)
        self.array.append(2)

    def test_is_empty_non_empty_array(self):
        self.assertFalse(self.array.is_empty())

    def test_is_empty_empty_array(self):
        array = list.List()
        self.assertTrue(array.is_empty())

    def test_get_elem_wrong_idx(self):

        with self.assertRaises(KeyError) as context:
            self.array.get_elem(100)

        self.assertTrue('The index is invalid!' in str(context.exception))

    def test_get_elem(self):
        self.assertEqual(self.array.get_elem(2), 143)

    def test_append(self):
        previous_size = self.array.size
        number = 18
        self.array.append(number)
        self.assertEqual(str(self.array), '[3, 22, 143, 2, 90, 11, 8, 2, 18]')
        self.assertEqual(self.array.get_elem(self.array.size - 1), number)
        self.assertTrue(self.array.size == (previous_size + 1))

    def test_prepend_empty_array(self):
        array = list.List()
        previous_size = array.size
        array.prepend(18)
        self.assertEqual(str(array), '[18]')
        self.assertTrue(array.size == (previous_size + 1))

    def test_prepend(self):
        previous_size = self.array.size
        self.array.prepend(18)
        self.assertEqual(str(self.array), '[18, 3, 22, 143, 2, 90, 11, 8, 2]')
        self.assertEqual(self.array.get_elem(0), 18)
        self.assertTrue(self.array.size == (previous_size + 1))

    def test_insert_wrong_index(self):

        with self.assertRaises(IndexError) as context:
            self.array.insert(100, 18)

            self.assertEqual('Invalid index!', str(context.exception))

    def test_insert(self):
        previous_size = self.array.size
        self.array.insert(5, 18)
        self.assertEqual(str(self.array), '[3, 22, 143, 2, 90, 18, 11, 8, 2]')
        self.assertEqual(self.array.get_elem(5), 18)
        self.assertTrue(self.array.size == (previous_size + 1))

    def test_pop_empty_array(self):
        array = list.List()

        with self.assertRaises(Exception) as context:
            array.pop()

        self.assertEqual('Empty array', str(context.exception))

    def test_pop(self):
        previous_size = self.array.size
        self.assertEqual(2, self.array.pop())
        self.assertEqual(str(self.array), '[3, 22, 143, 2, 90, 11, 8]')
        self.assertTrue(self.array.size == (previous_size - 1))

    def test_remove_empty_array(self):
        array = list.List()

        with self.assertRaises(Exception) as context:
            array.remove(18)

        self.assertEqual('Empty array', str(context.exception))

    def test_remove(self):
        previous_size = self.array.size
        self.array.remove(2)
        self.assertEqual(str(self.array), '[3, 22, 143, 90, 11, 8]')
        self.assertEqual(self.array.get_elem(3), 90)
        self.assertTrue(self.array.size == (previous_size - 2))

    def test_find_unique_element(self):
        self.assertEqual(self.array.find(11), [5])

    def test_find_missing_element(self):
        self.assertEqual(self.array.find(18), [])

    def test_find_duplicate_element(self):
        self.assertEqual(self.array.find(2), [3, 7])


if __name__ == '__main__':
    unittest.main()
