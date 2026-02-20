import random
class Solution:

# insertion sort
    # def insertion_sort(self, nums: List[int]) -> List[int]:         # [4, 3, 1, 3, 2]
    #     for i in range(1, len(nums)): #     1, 2, 3, 4
    #         current = nums[i]
    #         j = i - 1                 #  0, 1, 2, 3
    #         while j >= 0 and nums[j] > current:
    #             nums[j + 1] = nums[j]
    #             j -= 1
    #         nums[j + 1] = current
    #     return nums

# bubble sort
        # n = len(nums)
        # for i in range(n):
        #     for j in range(0, n-i-1):
        #         if nums[j] > nums[j+1]:
        #             temp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+1] = temp
        # print(nums)

# merge sort
    # def _merge(self, left: List[int], right: List[int]) -> List[int]: #(conquer)
    #     result = []
    #     i, j = 0, 0
    #     while i < len(left) and j < len(right):
    #         if left[i] <= right[j]:
    #             result.append(left[i])
    #             i += 1;
    #         else:
    #             result.append(right[j])
    #             j += 1;
    #     result += left[i:];
    #     result += right[j:];
    #     return result;

    # def sortArray(self, nums: List[int]) -> List[int]: #(divide)
    #     if len(nums) <= 1:
    #         return nums;
    #     mid = len(nums) // 2
    #     sorted_left = self.sortArray(nums[:mid])
    #     sorted_right = self.sortArray(nums[mid:])
    #     return self._merge(sorted_left, sorted_right)

# quick sort
    # def sortArray(self, nums: List[int]) -> List[int]: 
    #     self.quick_sort(nums, 0, len(nums) - 1)
    #     return nums
    # def quick_sort(self, nums: List[int], low: int, high: int):
    #     if low < high:
    #         pivot_index = self._partition(nums, low, high)
    #         self.quick_sort(nums, low, pivot_index - 1)
    #         self.quick_sort(nums, pivot_index + 1, high)

    def _partition(self, nums: List[int], low: int, high: int) -> int:
        # avoid: worst-case scenario
        rand_idx = random.randint(low, high)
        nums[rand_idx], nums[high] = nums[high], nums[rand_idx]
        pivot = nums[high] 
        i = low
        for j in range(low, high):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i

# heap sort
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)


        for i in range(n // 2 - 1, -1, -1):
            self._heapify(nums, n, i)


        for i in range(n - 1, 0, -1):

            nums[i], nums[0] = nums[0], nums[i]

            self._heapify(nums, i, 0)
            
        return nums

    def _heapify(self, nums: List[int], n: int, i: int):
        
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2


            if left < n and nums[left] > nums[largest]:
                largest = left

           
            if right < n and nums[right] > nums[largest]:
                largest = right


            if largest == i:
                break


            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest

