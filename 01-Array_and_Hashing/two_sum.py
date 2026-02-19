class Solution:
# brute force
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]


# hash map 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}  # val -> index
        for i, n in enumerate(nums):
            dic[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic and dic[diff] != i:
                return [i, dic[diff]]
        return []
                