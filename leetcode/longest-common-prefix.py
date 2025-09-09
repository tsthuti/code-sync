class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0] # make the first str the entire prefix
        for s in strs[1:]: # compare next str in arr to the set prefix
            while not s.startswith(prefix): # if next str ≠ same as prefix, trim off last letter until match
                prefix = prefix[:-1]  # shrink the prefix
                if not prefix:
                    return "" # if all char chopped off, return empty str
        return prefix