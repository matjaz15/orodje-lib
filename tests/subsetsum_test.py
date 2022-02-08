from threading import Timer
import random
import unittest
import os
import sys
import time
sys.path.append('../lib')
cwd = os.getcwd()

from src.math import subsetsum

class SubsetsumTest(unittest.TestCase):
    def setUp(self):
        self.nums = [1,5,3,62,1,2,88,0,56]      
        self.tolerance = 6  

    # --1 step tests--
    def test_subsetsum_1_step_closest_to_50(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=1,
            include_rest=True            
        )
        self.assertTupleEqual((56,), result)

    def test_subsetsum_1_step_closest_to_50_using_tolerance(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=1,
            tolerance=self.tolerance
        )
        self.assertTupleEqual((56,), result)

    def test_subsetsum_1_step_closest_to_50_index(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=1,
            include_rest=True,
            return_only_indexees=True
        )
        self.assertTupleEqual((8,), result)

    def test_subsetsum_1_step_exactly_56(self):       
        result = subsetsum(
            nums=self.nums,
            target=56,
            steps=1,
            include_rest=True            
        )
        self.assertTupleEqual((56,), result)


    # --2 step tests--
    def test_subsetsum_2_step_closest_to_50(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=2,
            include_rest=True            
        )
        self.assertTupleEqual((0,56), result)

    def test_subsetsum_2_step_closest_to_50_using_tolerance(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=2,
            tolerance=self.tolerance
        )
        self.assertTupleEqual((0,56), result)

    def test_subsetsum_2_step_closest_to_50_index(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=2,
            include_rest=True,
            return_only_indexees=True      
        )
        self.assertTupleEqual((7,8), result)

    def test_subsetsum_1_step_exactly_64(self):       
        result = subsetsum(
            nums=self.nums,
            target=64,
            steps=2,
            include_rest=True            
        )
        self.assertTupleEqual((62,2), result)
    

class SubsetsumTestWithFloats(unittest.TestCase):
    def setUp(self):
        self.nums = [10.23, 66.12, 5.11, 48.44, 51.22, 1.1]
        self.tolerance = 6

    # --1 step tests--
    def test_subsetsum_1_step_closest_to_50(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=1,
            include_rest=True            
        )
        self.assertTupleEqual((51.22,), result)

    def test_subsetsum_1_step_closest_to_50_using_tolerance(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=1,
            tolerance=self.tolerance
        )
        self.assertTupleEqual((51.22,), result)

    def test_subsetsum_1_step_closest_to_50_index(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=1,
            include_rest=True,
            return_only_indexees=True
        )
        self.assertTupleEqual((4,), result)


    # --2 step tests--
    def test_subsetsum_2_step_closest_to_50(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=2,
            include_rest=True            
        )
        self.assertTupleEqual((48.44, 1.1), result)

    def test_subsetsum_2_step_closest_to_50_using_tolerance(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=2,
            tolerance=self.tolerance
        )
        self.assertTupleEqual((48.44, 1.1), result)

    def test_subsetsum_2_step_closest_to_50_index(self):       
        result = subsetsum(
            nums=self.nums,
            target=50,
            steps=2,
            include_rest=True,
            return_only_indexees=True      
        )
        self.assertTupleEqual((3,5), result)
    

class SubsetsumPerformanceTest(unittest.TestCase):
    def setUp(self):
        # test = [random.randrange(0,99) for i in range(0,150)] 
        self.time_limit = 0.0000001
        self.time_limit2 = 0.003
        self.time_limit3 = 0.03
        self.nums_10 = [31, 36, 93, 75, 48, 4, 79, 76, 1, 89]
        self.nums_50 = [50, 75, 97, 73, 83, 85, 87, 84, 33, 29, 7, 79, 
        43, 90, 29, 48, 59, 71, 91, 11, 60, 52, 14, 46, 93, 58,
        32, 6, 85, 59, 33, 17, 97, 78, 5, 82, 34, 40, 14, 90, 17, 
        52, 67, 45, 41, 72, 10, 66, 1, 21]
        self.nums_150 = [26, 16, 76, 12, 7, 82, 60, 24, 29, 14, 80, 79, 
        89, 25, 46, 5, 34, 83, 16, 68, 67, 16, 37, 72, 13, 13, 78, 38, 
        9, 60, 48, 63, 26, 46, 44, 79, 64, 7, 73, 59, 94, 40, 50, 80, 
        83, 7, 69, 13, 15, 23, 85, 3, 18, 95, 74, 44, 29, 28, 45, 76, 47, 
        73, 59, 51, 31, 11, 49, 54, 76, 75, 80, 91, 41, 3, 3, 65, 7, 81, 
        95, 98, 72, 15, 81, 44, 68, 33, 93, 67, 93, 94, 84, 36, 66, 22, 
        97, 43, 69, 65, 48, 66, 41, 43, 79, 97, 73, 66, 53, 6, 98, 30, 27, 
        79, 21, 33, 18, 42, 76, 74, 66, 90, 79, 42, 6, 40, 56, 23, 41, 
        67, 47, 57, 65, 20, 45, 37, 10, 61, 7, 35, 77, 77, 89, 75, 98, 31, 
        28, 40, 33, 45, 81, 89]

    def test_performance_10_numbers_1_step_under_0_0000001sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_10,
            target=90,
            tolerance=1,
            steps=1
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)
        self.assertLessEqual(end_time, self.time_limit)
    
    def test_performance_10_numbers_2_step_under_0_0000001sec(self):
        start_time = time.time()
        result = subsetsum(
            nums=self.nums_10,
            target=90,
            tolerance=1,
            steps=2
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)
        self.assertLessEqual(end_time, self.time_limit)

    def test_performance_10_numbers_5_step_under_0_0000001sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_10,
            target=380,
            tolerance=1,
            steps=5
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)
        self.assertLessEqual(end_time, self.time_limit)

    def test_performance_50_numbers_1_step_under_0_0000001sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_50,
            target=70,
            tolerance=1,
            steps=1
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)
        self.assertLessEqual(end_time, self.time_limit2)
    
    def test_performance_50_numbers_2_step_under_0_0000001sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_50,
            target=150,
            tolerance=1,
            steps=2
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)
        self.assertLessEqual(end_time, self.time_limit2)

    def test_performance_50_numbers_5_step_under_0_0000001sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_50,
            target=150,
            tolerance=1,
            steps=5
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)
        self.assertLessEqual(end_time, self.time_limit2)

    def test_performance_150_numbers_1_step_under_0_0000001sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_150,
            target=66,
            tolerance=1,
            steps=1
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)        
        self.assertLessEqual(end_time, self.time_limit2)
    
    def test_performance_150_numbers_2_step_under_0_0000001sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_150,
            target=66,
            tolerance=1,
            steps=2
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)        
        self.assertLessEqual(end_time, self.time_limit2)
    
    def test_performance_150_numbers_5_step_under_0_0000001sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_150,
            target=200,
            tolerance=1,
            steps=5
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)      
        self.assertLessEqual(end_time, self.time_limit2)

    def test_performance_150_numbers_7_step_under_0_0000001sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_150,
            target=200,
            tolerance=1,
            steps=7
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)      
        self.assertLessEqual(end_time, self.time_limit3)

    def test_performance_150_numbers_8_step_under_0_03sec(self):
        start_time = time.time()        
        result = subsetsum(
            nums=self.nums_150,
            target=200,
            tolerance=1,
            steps=8
        )
        end_time = time.time() - start_time
        self.assertNotEqual((),result)      
        self.assertLessEqual(end_time, self.time_limit3)

if __name__ == '__main__':
    unittest.main()