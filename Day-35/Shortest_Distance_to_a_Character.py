class Solution:
    def shortestToChar(self, s: str, c: str):
        result = []
        positions = []

        for i in range(len(s)):
            if s[i] == c:
                positions.append(i)
        for i in range(len(s)):
            minimum = float('inf')

            for pos in positions:
                minimum = min(minimum, abs(i - pos))

            result.append(minimum)
        return result
solution = Solution()
print(solution.shortestToChar("loveleetcode", "e"))