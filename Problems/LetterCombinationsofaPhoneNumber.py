# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    mapping = {
        "2": [
            "a", "b", "c"
        ],
        "3": [
            "d", "e", "f"
        ],
        "4": [
            "g", "h", "i"
        ],
        "5": [
            "j", "k", "l"
        ],
        "6": [
            "m", "n", "o"
        ],
        "7": [
            "p", "q", "r", "s"
        ],
        "8": [
            "t", "u", "v"
        ],
        "9": [
            "w", "x", "y", "z"
        ]
    }
    
    def letterCombinations(self, digits):
        length = len(digits)
        digits = list(digits)
        combinations = []
    
        if (length == 1):
            for letter in self.mapping[digits[0]]:
                combinations.append(letter)
        elif (length == 2):
            for letter1 in self.mapping[digits[0]]:
                for letter2 in self.mapping[digits[1]]:
                    combinations.append(letter1 + letter2)
        elif (length == 3):
            for letter1 in self.mapping[digits[0]]:
                for letter2 in self.mapping[digits[1]]:
                    for letter3 in self.mapping[digits[2]]:
                        combinations.append(letter1 + letter2 + letter3)
        elif (length == 4):
            for letter1 in self.mapping[digits[0]]:
                for letter2 in self.mapping[digits[1]]:
                    for letter3 in self.mapping[digits[2]]:
                        for letter4 in self.mapping[digits[3]]:
                            combinations.append(letter1 + letter2 + letter3 + letter4)

        return combinations