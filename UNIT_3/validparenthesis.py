""" 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets. (}
Open brackets must be closed in the correct order. ([)]
Every close bracket has a corresponding open bracket of the same type. 
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}' 

Understand: 
Edge cases: 
 - empty string
 - "(([])))"

Match step:
 - Stack
 - Dictionary (hashmap)

Plan:
 - stack to store opening brackets
 - dictionary: {
            ):(, ]:[, }:{
        }
 - Loop through the string:
 - if opening bracket ; ({[:
    append to stack
 - if closing bracket: )}]:
    -compare with recent open bracket, return false if mismatch
    


"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {")": "(",
                      "}":"{",
                      "]":"["}
        
        for par in s:
            if par in "({[":
                stack.append(par)
            else:
                if stack and stack[-1] == dictionary[par]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
    
#TC: O(n) , n = len(s)
#SC: O(n), n = len(s)




