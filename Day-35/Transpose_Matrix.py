import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return np.transpose(matrix).tolist()
solution = Solution()
print(solution.transpose([[1,2,3],[4,5,6],[7,8,9]]))