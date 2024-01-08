class Solution:
      def twoSum(self, nums, target):
        dict={}

        for i, a in enumerate (nums):
            b=target-a
            if b in dict:
                return i, dict [b]
            dict [a] = i
