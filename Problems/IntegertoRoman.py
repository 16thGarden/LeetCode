# https://leetcode.com/problems/integer-to-roman/

class Solution:
    conversion = [
        [
            "",
            "I",
            "II",
            "III",
            "IV",
            "V",
            "VI",
            "VII",
            "VIII",
            "IX"
        ],

        [
            "",
            "X",
            "XX",
            "XXX",
            "XL",
            "L",
            "LX",
            "LXX",
            "LXXX",
            "XC"
        ],

        [
            "",
            "C",
            "CC",
            "CCC",
            "CD",
            "D",
            "DC",
            "DCC",
            "DCCC",
            "CM"
        ],

        [   
            "",
            "M",
            "MM",
            "MMM"
        ]
    ]

    def divide(self, num):
        result = []
        while(num > 0):
            result.append(num % 10)
            num //= 10

        return result

    def intToRoman(self, num):
        num = self.divide(num)
        
        place = 0
        roman = ""
        for d in num:
            roman = self.conversion[place][d] + roman
            place += 1
        
        return roman

s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(58))
print(s.intToRoman(1994))
print(s.intToRoman(10))
print(s.intToRoman(50))
print(s.intToRoman(100))
print(s.intToRoman(500))
print(s.intToRoman(1000))