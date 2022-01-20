import unittest
import os
import sys
sys.path.append('../../python')
cwd = os.getcwd()
import files


class FilesTest(unittest.TestCase):

    def setUp(self):
        self.path_with_header = os.path.join(os.getcwd(), 'data', 'SampleCSVFileWithHeader.csv')
        self.path_without_header = os.path.join(os.getcwd(), 'data', 'SampleCSVFileWithoutHeader.csv')
        self.csv_encoding = 'utf-8'
        self.csv_delimiter = ','
        self.line_key = 'ID'
        self.search_data_structure = ['Product Name','Contact Name','Group ids']
        self.target_data_structure = ['product_name','contact_name','group_ids']

        self.expected_without_target_data_struture = [
            {'Product Name': 'Eldon Base for stackable storage shelf, platinum', 'Contact Name': 'Muhammed MacIntyre', 'Group ids': ['1', '3', '4']},
            {'Product Name': '1.7 Cubic Foot Compact "Cube" Office Refrigerators', 'Contact Name': False, 'Group ids': ['556', '293', '434', '412']},
            {'Product Name': 'Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl', 'Contact Name': 'Barry French', 'Group ids': '293'},
            {'Product Name': 'R380', 'Contact Name': 'Clay Rozendal', 'Group ids': '483'}
        ]
        self.expected_with_target_data_structure = [
            {'product_name': 'Eldon Base for stackable storage shelf, platinum', 'contact_name': 'Muhammed MacIntyre', 'group_ids': ['1', '3', '4']},
            {'product_name': '1.7 Cubic Foot Compact "Cube" Office Refrigerators', 'contact_name': False, 'group_ids': ['556', '293', '434', '412']},
            {'product_name': 'Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl', 'contact_name': 'Barry French', 'group_ids': '293'},
            {'product_name': 'R380', 'contact_name': 'Clay Rozendal', 'group_ids': '483'}
        ]

    def test_grab_csv_data_with_header(self):
        result = files.grab_csv_data(
            path=self.path_with_header,
            line_key=self.line_key,
            search_data_structure=self.search_data_structure,
            encoding=self.csv_encoding,
            delimiter=self.csv_delimiter
        )
        self.assertListEqual(self.expected_without_target_data_struture, result)

    def test_grab_csv_data_with_header_and_with_target_data_structure(self):
        result = files.grab_csv_data(
            path=self.path_with_header,
            line_key=self.line_key,
            search_data_structure=self.search_data_structure,
            target_data_structure=self.target_data_structure,
            encoding=self.csv_encoding,
            delimiter=self.csv_delimiter
        )
        self.assertListEqual(self.expected_with_target_data_structure, result)
    
    def test_grab_csv_data_without_header(self):
        result = files.grab_csv_data(
            path=self.path_without_header,
            line_key=self.line_key,
            search_data_structure=self.search_data_structure,
            encoding=self.csv_encoding,
            delimiter=self.csv_delimiter,
            has_headers=False
        )
        self.assertListEqual(self.expected_without_target_data_struture, result)

    def test_grab_csv_data_without_header_and_with_target_data_structure(self):
        result = files.grab_csv_data(
            path=self.path_without_header,
            line_key=self.line_key,
            search_data_structure=self.search_data_structure,
            target_data_structure=self.target_data_structure,
            encoding=self.csv_encoding,
            delimiter=self.csv_delimiter,
            has_headers=False
        )
        self.assertListEqual(self.expected_with_target_data_structure, result)



if __name__ == '__main__':
    unittest.main()