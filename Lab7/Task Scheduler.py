from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
     
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())  
        max_count = list(task_counts.values()).count(max_freq)  

       
        part_count = max_freq - 1  
        part_length = n - (max_count - 1)  
        empty_slots = part_count * part_length  
        available_tasks = len(tasks) - (max_freq * max_count)  
        idles = max(0, empty_slots - available_tasks)  

        return len(tasks) + idles 

import unittest

class TestTaskScheduler(unittest.TestCase):
    def test_leastInterval(self):
        sol = Solution()
        self.assertEqual(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2), 8)  # Example 1
        self.assertEqual(sol.leastInterval(["A", "C", "A", "B", "D", "B"], 1), 6)  # Example 2
        self.assertEqual(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 3), 10)  # Example 3

if __name__ == "__main__":
    unittest.main()
