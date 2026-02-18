# Problem: [Problem Name, e.g., Merge Sort]
# LeetCode Link: [URL]
# Difficulty: [Easy/Medium/Hard]

"""
UMPIRE Process:

U - Understand: 
    - Input: An unsorted array of integers.
    - Output: A sorted array (ascending).
    - Constraints: O(n log n) time required. 

M - Match: 
    - Divide and Conquer pattern. Uses recursion and a merge helper function.

P - Plan:
    1. Base case: If len <= 1, return.
    2. Find middle, split into left/right halves.
    3. Recursively call sort on both halves.
    4. Merge sorted halves using two pointers.

I - Implement: (Code below)
"""

def sortArray(nums):
    # Your code goes here...
    pass

"""
R - Review/Refine:
    - Tested with empty list, single element, and duplicates.
    - Added slicing logic for clarity.

E - Evaluate:
    - Time Complexity: O(n log n)
    - Space Complexity: O(n) due to temporary arrays during merge.
"""