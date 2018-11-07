"""
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument,
please click the reload button to reset your code definition.
"""

"""
time: O(n) Space: O(1)
"""

class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        numberSeen = False
        pointSeen = False
        eSeen = False
        numberAfterE = True
        for i in range(len(s)):
            if s[i].isdigit():                  #如果出现数字
                numberSeen = True
                numberAfterE = True
            elif s[i] == ".":
                if eSeen or pointSeen:         #如果e后面出现点，或者已经出现过点，都是false
                    return False
                pointSeen = True
            elif s[i] == "e":
                if eSeen or not numberSeen:    #如果已经出现过e, 或者e后面没有number, 都是false
                    return False
                eSeen = True
                numberAfterE = False           #注意：这里numberAfterE是false
            elif s[i] == "+" or s[i] == "-":
                if i != 0 and s[i-1] != "e":     #如果正负号不出现在第一位并且也没出现在e之后，那么都是false
                    return False
            else:
                return False
        return numberSeen and numberAfterE      #最后要保证numberSeen和numberAfterE都是true
