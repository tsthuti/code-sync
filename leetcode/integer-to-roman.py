class Solution:
    def intToRoman(self, num: int) -> str:
        # use arr here instead of a dict for 'on the lfy' mapping
        symbols = [
            ("I", "V", "X"),   # ones
            ("X", "L", "C"),   # tens
            ("C", "D", "M"),   # hundreds
            ("M", "", "")      # thousands
        ]
        
        string = str(num) # cast to a str so i can iterate over each number
        rom = ""

        i = 0
        while i < len(string):
            digit = int(string[i]) # first digit, cast to an int
            place = len(string) - i - 1 # finding out the face value of the number
            one, five, ten = symbols[place] # assigning symbols based on fv of number

            # all these cases handle the subtractive cases manually
            if digit <= 3:
                rom += one * digit
            elif digit == 4:
                rom += one + five
            elif digit <= 8:
                rom += five + (one * (digit - 5))
            elif digit == 9:
                rom += one + ten

            i += 1 # keep going for rest of numbers 

        return rom