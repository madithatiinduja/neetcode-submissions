class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rev=matrix[::-1]
        matrix[:]=[list(rows) for rows in zip(*rev)]
      
        