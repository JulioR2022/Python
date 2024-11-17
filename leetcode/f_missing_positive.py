"""Questão 41.First Missing Positive - Hard"""

class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums = sorted(nums)

       
        if 1 in nums:
            for i,value in enumerate(nums):
                if value <= 0:
                    continue
                if  nums[i-1] < 0:
                    continue
                if value > (nums[i - 1] + 1):
                    return nums[i-1] + 1           
        else:
            return 1  # 1 é o menor inteiro postivo

        return nums[-1] + 1 # nums possui os n menores inteiros positivos
        