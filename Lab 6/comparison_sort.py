"""
Lab6
John Wright
"""
import time
import random

def merge_sort(alist):
    """Takes alist and sorts it in ascending order using merge sort and returns the number of comparisons
        Author:
            John Wright
        Args:
            alist (list): list of unsorted integers
        Returns:
            (int): number of comparisons
        """
    temp = merge_sort_helper(alist)
    return temp[1]

def merge_sort_helper(alist):
    """Helper function for merge_sort
    Author:
        John Wright
    Args:
        alist (list): list of unsorted integers
    Returns:
        (int): number of comparisons
    """
    comparisons = 0
    newlist = []
    if len(alist) <= 1:
        return alist, comparisons
    left_index = 0
    right_index = 0
    midpoint = len(alist) // 2
    left = merge_sort_helper(alist[:int(midpoint)])
    right = merge_sort_helper(alist[int(midpoint):])
    comparisons = left[1] + right[1]
    left = left[0]
    right = right[0]

    while left_index < len(left) and right_index < len(right):
        comparisons += 1
        if left[left_index] <= right[right_index]:
            newlist.append(left[left_index])
            left_index += 1
        else:
            newlist.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        comparisons += 1
        newlist.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        comparisons += 1
        newlist.append(right[right_index])
        right_index += 1
    return newlist , comparisons

def insertion_sort(alist):
    """Takes alist and sorts it in ascending order using insertion sort and returns the number of comparisons
        Author:
            John Wright
        Args:
            alist (list): list of unsorted integers
        Returns:
            (int): number of comparisons
        """
    comparisons = 1
    length = len(alist)
    for i in range(1,length):
        while i > 0 and alist[i-1] > alist[i]:
            comparisons += 1
            alist[i-1], alist[i] = alist[i], alist[i-1]
            i -= 1
        comparisons += 1
    return comparisons


# leftover code from data collection for charts
"""
random.seed(1)
list = random.sample(range(1000), 1000)
start_time = time.time()
print('Comparisons = {}'.format(insertion_sort(list)))
end_time = time.time()
total_time = end_time-start_time
print('TotalTime = {}'.format(total_time))
"""