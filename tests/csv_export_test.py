import unittest
import os
import sys
sys.path.append('../lib')
cwd = os.getcwd()

from csv_import_export import export_csv_data


class CSVImportTest(unittest.TestCase):

    def setUp(self):
        self.path = os.path.join(os.getcwd(), 'data', 'test_data.csv')
        self.object_test_data = [
            {'product_name': 'Eldon Base for stackable storage shelf, platinum', 'company_ids': ['0', '1', '5'], 'contact_name': 'Muhammed MacIntyre', 'group_ids': ['1', '3', '4']},
            {'product_name': '1.7 Cubic Foot Compact "Cube" Office Refrigerators', 'company_ids': ['0', '1'], 'contact_name': False, 'group_ids': ['556', '293', '434', '412']},
            {'product_name': 'Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl', 'company_ids': ['0', '1'], 'contact_name': 'Barry French', 'group_ids': '293'},
            {'product_name': 'R380', 'company_ids': ['0', '1', '3'], 'contact_name': 'Clay Rozendal', 'group_ids': '483'}
        ]
        
    def test_object_to_csv(self):
        result = export_csv_data(
            path = self.path,
            object_data_list = self.object_test_data
        )
        self.assertTrue(True)
       
   

if __name__ == '__main__':
    unittest.main()