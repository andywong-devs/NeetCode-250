# # brute force
# class NumMatrix:
#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         total_sum = 0
#         # Iterate from row1 to row2 (inclusive)
#         for r in range(row1, row2 + 1):
#             # Iterate from col1 to col2 (inclusive)
#             for c in range(col1, col2 + 1):
#                 total_sum += self.matrix[r][c]
#         return total_sum

## all combos hashmap
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0
        self.combos = {}
        for r in range(self.rows):
            for start in range(self.cols):
                current_sum = 0
                for end in range(start, self.cols):
                    current_sum += matrix[r][end]
                    # Key is (row, col_start, col_end)
                    self.combos[(r, start, end)] = current_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        # Still must loop through the rows to add the segments
        for r in range(row1, row2 + 1):
            total += self.combos[(r, col1, col2)]
        return total

## 1D prefix sum
# class NumMatrix:
#     def __init__(self, matrix: List[List[int]]):
#         rows = len(matrix)
#         cols = len(matrix[0]) if rows > 0 else 0
#         # row_pref[r][c] stores sum of row r from index 0 to c-1
#         self.row_pref = [[0] * (cols + 1) for _ in range(rows)]
#         for r in range(rows):
#             for c in range(cols):
#                 self.row_pref[r][c + 1] = self.row_pref[r][c] + matrix[r][c]

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         total = 0
#         for r in range(row1, row2 + 1):
#             # Calculate segment sum: RightTotal - LeftTotal
#             total += self.row_pref[r][col2 + 1] - self.row_pref[r][col1]
#         return total