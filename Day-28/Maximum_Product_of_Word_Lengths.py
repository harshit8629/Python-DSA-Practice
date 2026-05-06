words = ["abcw","baz","foo","bar","xtfn","abcdef"]
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):

                # Convert words into sets
                set1 = set(words[i])
                set2 = set(words[j])

                # Check if common letters exist
                if set1.isdisjoint(set2):

                    product = len(words[i]) * len(words[j])

                    max_product = max(max_product, product)

        return max_product
solution = Solution()
print(solution.maxProduct(words))