class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        rom=0
        i=0

        while i < len(s):
            # safely check next char
            # if next char bigger than current char, we know its subtractive
            if i + 1 < len(s) and dict[s[i]] < dict[s[i + 1]]:
                rom += dict[s[i + 1]] - dict[s[i]]
                i += 2  # skip both characters that we handled subtraction for
            else:
                rom += dict[s[i]]
                i += 1

        return rom