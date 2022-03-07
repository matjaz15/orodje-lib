import unittest
import os
import sys
sys.path.append('../lib')
cwd = os.getcwd()

from csv_import_export import import_csv_data


class CSVTest(unittest.TestCase):

    def setUp(self):
        self.path_with_header = os.path.join(os.getcwd(), 'data', 'SampleCSVFileWithHeader.csv')
        self.path_without_header = os.path.join(os.getcwd(), 'data', 'SampleCSVFileWithoutHeader.csv')
        self.csv_encoding = 'utf-8'
        self.csv_delimiter = ','
        self.new_line_key = 'ID'
        self.header_list = ['ID','Product Name','Contact Name','Group ids']
        self.search_data_list = ['Product Name','Contact Name','Group ids']
        self.target_data_list = ['product_name','contact_name','group_ids']

        self.expected_data = [
            {'Product Name': 'Eldon Base for stackable storage shelf, platinum', 'Contact Name': 'Muhammed MacIntyre', 'Group ids': ['1', '3', '4']},
            {'Product Name': '1.7 Cubic Foot Compact "Cube" Office Refrigerators', 'Contact Name': False, 'Group ids': ['556', '293', '434', '412']},
            {'Product Name': 'Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl', 'Contact Name': 'Barry French', 'Group ids': '293'},
            {'Product Name': 'R380', 'Contact Name': 'Clay Rozendal', 'Group ids': '483'}
        ]
        self.expected_with_target_data_list = [
            {'product_name': 'Eldon Base for stackable storage shelf, platinum', 'contact_name': 'Muhammed MacIntyre', 'group_ids': ['1', '3', '4']},
            {'product_name': '1.7 Cubic Foot Compact "Cube" Office Refrigerators', 'contact_name': False, 'group_ids': ['556', '293', '434', '412']},
            {'product_name': 'Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl', 'contact_name': 'Barry French', 'group_ids': '293'},
            {'product_name': 'R380', 'contact_name': 'Clay Rozendal', 'group_ids': '483'}
        ]

    def test_import_csv_data_with_header(self):
        result = import_csv_data(
            path=self.path_with_header,
            new_line_key=self.new_line_key,
            search_data_list=self.search_data_list,
            encoding=self.csv_encoding,
            delimiter=self.csv_delimiter
        )
        self.assertListEqual(self.expected_data, result)

    def test_import_csv_data_with_header_and_with_target_data_list(self):
        result = import_csv_data(
            path=self.path_with_header,
            new_line_key=self.new_line_key,
            search_data_list=self.search_data_list,
            target_data_list=self.target_data_list,
            encoding=self.csv_encoding,
            delimiter=self.csv_delimiter
        )
        self.assertListEqual(self.expected_with_target_data_list, result)
    
    def test_import_csv_data_without_header(self):
        result = import_csv_data(
            path=self.path_without_header,
            new_line_key=self.new_line_key,
            search_data_list=self.search_data_list,
            header_list=self.header_list,
            encoding=self.csv_encoding,
            delimiter=self.csv_delimiter
        )
        self.assertListEqual(self.expected_data, result)

    def test_import_csv_data_without_header_and_with_target_data_list(self):
        result = import_csv_data(
            path=self.path_without_header,
            new_line_key=self.new_line_key,
            search_data_list=self.search_data_list,
            target_data_list=self.target_data_list,
            header_list=self.header_list,
            encoding=self.csv_encoding,
            delimiter=self.csv_delimiter
        )
        self.assertListEqual(self.expected_with_target_data_list, result)



if __name__ == '__main__':
    unittest.main()