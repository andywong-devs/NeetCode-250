class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # first: remove all existing of val in nums
        # second: return the number of reminaing elements (k)
        
        nums[:] = [x for x in nums if x != val]
        return len(nums)