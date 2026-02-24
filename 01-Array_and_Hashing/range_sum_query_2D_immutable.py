# 1. brute force
# from typing import List
# class NumMatrix:
#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         total_sum = 0
#         for row in range(row1, row2 + 1):        # inclusive 
#             for col in range(col1, col2 + 1):    # inclusive
#                 total_sum += self.matrix[row][col]
#         return total_sum

# 2. all combos hashmap
# 2. col combos prefix
# from typing import List
# class NumMatrix:
#     def __init__(self, matrix: List[List[int]]):
#         self.row = len(matrix)
#         self.col = len(matrix[0]) if self.row > 0 else 0
#         self.lookup = {}
#         for r in range(self.row):
#             for start in range(self.col):           # start col index
#                 total_sum = 0
#                 for end in range(start, self.col):  # end col index
#                     total_sum += matrix[r][end]
#                     self.lookup[(r, start, end)] = total_sum
        
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         total_sum = 0
#         for row in range(row1, row2 + 1):
#             total_sum += self.lookup[(row, col1, col2)]
#         return total_sum
        
# 3. 1D prefix sum
# from typing import List
# class NumMatrix: 
#     def __init__(self, matrix: List[List[int]]):
#         # Ask: "Should I handle empty inputs?" 
#         # If yes, this is the 'Clean Code' way:
#         if not matrix or not matrix[0]:
#             self.rows = 0
#             self.cols = 0
#             self.row_pref = [] 
#             return
#         self.rows = len(matrix)
#         self.cols = len(matrix[0]) if self.rows > 0 else 0
#         self.row_pref = [[0] * (self.cols + 1) for _ in range(self.rows)]
#         for r in range(self.rows):
#             for c in range(self.cols):
#                 self.row_pref[r][c + 1] = self.row_pref[r][c] + matrix[r][c]
#         print(self.row_pref)
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         # Check if we have data before looping
#         if not self.row_pref:
#             return 0
#         total_sum = 0
#         for r in range(row1, row2 + 1):
#             total_sum += self.row_pref[r][col2 + 1] - self.row_pref[r][col1]
#         return total_sum

# 4. 2D prefix sum
from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.sum_pref = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        col_counter = 0
        row_counter = 0
        for r in range(self.rows):
            col_counter = 0
            for c in range(self.cols):
                col_counter += self.matrix[r][c] 
                self.sum_pref[r + 1][c + 1] += (col_counter + self.sum_pref[r][c + 1])
        print(self.sum_pref)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.sum_pref[row2 + 1][col2 + 1] # Bottom Right
        - self.sum_pref[row1][col2 + 1]   # Minus everything above
        - self.sum_pref[row2 + 1][col1]   # Minus everything to the left
        + self.sum_pref[row1][col1])      # Add back Top-Left corner (it was subtracted twice!)









