class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len = len(word1)
        w2_len = len(word2)

        min_len = min(w1_len, w2_len)

        new_str = []

        for i in range(min_len):
            new_str.append(word1[i])
            new_str.append(word2[i])

        new_str.append(word1[min_len:])
        new_str.append(word2[min_len:])

        return("".join(new_str))