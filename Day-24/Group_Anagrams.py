from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        
        groups = defaultdict(list)

        for word in strs:
            
            # Sort the word to create a key
            key = ''.join(sorted(word))

            # Add original word to its group
            groups[key].append(word)

        # Return grouped anagrams
        return list(groups.values())
solution s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))