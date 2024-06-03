"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""
from num_thai.thainumbers import NumThai

class Solution:

    def number_to_thai(self, number: int) -> str:
        num = NumThai()
        

        if number == 0:
            return "ศูนย์"
        elif number < 0:
            return "number can not less than 0"
        else:
            text = num.NumberToTextThai(number)
            ans = ""
            for word in text:
                ans +=word
            return ans
        

        
   
