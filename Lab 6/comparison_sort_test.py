"""CPE202
John Wright
Lab 5
"""
import unittest
import random
from comparison_sort import insertion_sort, merge_sort, merge_sort_helper
import time

class MyTest(unittest.TestCase):

   def test_insertion_sort(self):
      random.seed(1)
      list = random.sample(range(1000),1000)
      listsorted = []
      list2sorted = []
      for i in range(1000):
         listsorted.append(i)
      for i in range(100000):
         list2sorted.append(i)
      self.assertEqual(insertion_sort([5,4,3,2,1]), (15))
      self.assertEqual(insertion_sort(list), (251393))
      self.assertEqual(insertion_sort(listsorted), 1000)
      self.assertEqual(insertion_sort(list2sorted), 100000)

   def test_merge_sort(self):
      random.seed(1)
      list = random.sample(range(1000), 1000)
      list2 = random.sample(range(8000), 8000)
      listsorted = []
      list2sorted = []
      for i in range(1000):
         listsorted.append(i)
      for i in range(100000):
         list2sorted.append(i)
      testsort = merge_sort_helper(list)
      self.assertEqual(testsort[0], (listsorted))
      self.assertEqual(merge_sort(list), 9976)
      self.assertEqual(merge_sort(list2), 103808)
      self.assertEqual(merge_sort(list2sorted), 1668928)


if __name__ == '__main__':
   unittest.main()
