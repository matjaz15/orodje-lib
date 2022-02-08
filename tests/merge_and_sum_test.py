import unittest
import os
import sys
sys.path.append('../lib')
cwd = os.getcwd()

from src.lists import merge_and_sum_by_id


class ListsTest(unittest.TestCase):

    def setUp(self):
        self.unique_id_name = 'my_id'
        self.sum_key_names = ['num1', 'num2']

    def test_merge_and_sum_data_by_id(self):
        test_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 5, 'num2': 10},
            {'my_id': 1, 'name': 'test2', 'num1': 2, 'num2': 3},
            {'my_id': 1, 'name': 'test3', 'num1': 1, 'num2': 2},
            {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
        ]
        expected_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 8, 'num2': 15},
            {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
        ]
        result = merge_and_sum_by_id(
            data=test_data,
            unique_id_name=self.unique_id_name,
            sum_key_names=self.sum_key_names
        )
        self.assertListEqual(expected_data, result)

    def test_merge_and_sum_with_different_data(self):
        test_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 5, 'num2': 10},
            {'my_id': 1, 'name': 'test2', 'num1': 2, 'num2': 3, 'fk_company': 5},
            {'my_id': 1, 'name': 'test3', 'num1': 1, 'num2': 2, 'fk_user': 1},
            {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
        ]
        expected_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 8, 'num2': 15},
            {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
        ]
        result = merge_and_sum_by_id(
            data=test_data,
            unique_id_name=self.unique_id_name,
            sum_key_names=self.sum_key_names
        )
        self.assertListEqual(expected_data, result)

    def test_merge_and_sum_with_decimals(self):
        test_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 5.33, 'num2': 10.77},
            {'my_id': 1, 'name': 'test2', 'num1': 2.12, 'num2': 3.55},
            {'my_id': 1, 'name': 'test3', 'num1': 1.55, 'num2': 2.66},
            {'my_id': 6, 'name': 'test4', 'num1': 4.99, 'num2': 5.33}
        ]
        expected_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 9, 'num2': 16.98},
            {'my_id': 6, 'name': 'test4', 'num1': 4.99, 'num2': 5.33}
        ]
        result = merge_and_sum_by_id(
            data=test_data,
            unique_id_name=self.unique_id_name,
            sum_key_names=self.sum_key_names
        )
        self.assertListEqual(expected_data, result)
    
    def test_merge_no_sum(self):
        test_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 5, 'num2': 10},
            {'my_id': 1, 'name': 'test2', 'num1': 2, 'num2': 3},
            {'my_id': 1, 'name': 'test3', 'num1': 1, 'num2': 2},
            {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
        ]
        expected_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 5, 'num2': 10},
            {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
        ]
        result = merge_and_sum_by_id(
            data=test_data,
            unique_id_name=self.unique_id_name
        )
        self.assertListEqual(expected_data, result)

    def test_merge_with_different_data_no_sum(self):
        test_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 5, 'num2': 10},
            {'my_id': 1, 'name': 'test2', 'num1': 2, 'num2': 3, 'fk_company': 5},
            {'my_id': 1, 'name': 'test3', 'num1': 1, 'num2': 2, 'fk_user': 1},
            {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
        ]
        expected_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 5, 'num2': 10},
            {'my_id': 6, 'name': 'test4', 'num1': 4, 'num2': 5}
        ]
        result = merge_and_sum_by_id(
            data=test_data,
            unique_id_name=self.unique_id_name
        )
        self.assertListEqual(expected_data, result)

    def test_merge_with_decimals_no_sum(self):
        test_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 5.33, 'num2': 10.77},
            {'my_id': 1, 'name': 'test2', 'num1': 2.12, 'num2': 3.55},
            {'my_id': 1, 'name': 'test3', 'num1': 1.55, 'num2': 2.66},
            {'my_id': 6, 'name': 'test4', 'num1': 4.99, 'num2': 5.33}
        ]
        expected_data = [
            {'my_id': 1, 'name': 'test1', 'num1': 5.33, 'num2': 10.77},
            {'my_id': 6, 'name': 'test4', 'num1': 4.99, 'num2': 5.33}
        ]
        result = merge_and_sum_by_id(
            data=test_data,
            unique_id_name=self.unique_id_name
        )
        self.assertListEqual(expected_data, result)


if __name__ == '__main__':
    unittest.main()