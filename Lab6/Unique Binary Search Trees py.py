class Solution:
    def numTrees(self, n):
    
    
        dp = [0] * (n + 1)

       
        dp[0] = 1  # Empty tree
        dp[1] = 1  # Single node

        
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
             
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]


import unittest

class TestUniqueBST(unittest.TestCase):
    def test_numTrees(self):
        sol = Solution()
        self.assertEqual(sol.numTrees(3), 5)  # Example 1
        self.assertEqual(sol.numTrees(1), 1)  # Example 2
        self.assertEqual(sol.numTrees(4), 14)
        self.assertEqual(sol.numTrees(5), 42)

if __name__ == "__main__":
    unittest.main()
