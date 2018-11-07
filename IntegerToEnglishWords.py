"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

"""
思路：将数字以千为单位分组（3位数）。使用除法和取模运算将数字以千为单位拆分成数组，然后将其转化为单词。
题目中限定了输入数字范围为0到2^31 - 1之间，最高只能到billion位，3个一组也只需处理四组即可.
注意边界条件的处理，不需要考虑添加单词And。
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        list1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                "Forteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        list2 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        def words(n):
            if n < 20:
                return list1[n-1:n]
            if n < 100:
                return [list2[n/10 - 2]] + words(n%10)               #cannot concatenate list object and 'str'
            if n < 1000:
                return [list1[n/100-1]] + ["Hundred"] + words(n%100)
            for idx, value in enumerate(["Thousand", "Million", "Billion"], 1):   #enumerate(iterable, start = 1) 表示enumerate从1开始counting, 否则默认是0
                if n < 1000 ** (idx+1):
                    return words(n/1000**idx) +  [value] + words(n%1000**idx)

        return " ".join(words(num)) or "Zero"     #注意：这里是用or!!
