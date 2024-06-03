"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:

        if(len(numbers)==0):
            return "list can not blank"

        max_value = numbers[0]
        max_index = 0

        for index, value in enumerate(numbers):
            if value > max_value:
                max_value = value
                max_index = index

        return max_index
    

        
        
