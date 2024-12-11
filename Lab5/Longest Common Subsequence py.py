class Solution:
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

    
        cache = [0] * (n + 1)
        cache[1] = 1

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]

import unittest

class TestFibonacci(unittest.TestCase):
    def test_fib(self):
        sol = Solution()
        self.assertEqual(sol.fib(0), 0)
        self.assertEqual(sol.fib(1), 1)
        self.assertEqual(sol.fib(5), 5)
        self.assertEqual(sol.fib(10), 55)

if __name__ == "__main__":
    unittest.main()
