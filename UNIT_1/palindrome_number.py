"""Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?"""


"""UMPIRE BREAKDOWN"""

"""Understand:
input: integer
palindrome: 121, 131, 11.
-121
edge cases, constraints: 0, 1 - 9, negative numbers

Matching:
two pointer approach, convert the input to a string
Reversing the string
Exploiting math (division by 10s)

Plan:
1. convert the input to a string
2. initiate the left and right pointer
3. loop the inwards: if they left and right are different, return False, else update left and right
4. return True


x = 12321 =  1 * 10^4
y = 


get the number of digits in the x by dividing by 10:
12321/ 10 = 1232, count = 1
1232/10 = 123, count = 2
123/ 10 = 12, count = 3
12/10 = 1, count = 4
1/10 = 0, count = 5

max divider = 10*4
last -> x%10
first -> x//divider
x = x % divider : converts from 12321 to x = 2321
x = x//10 : converts from 2321 to x = 232
divider = divider / 100, since we deleted two digits, divider = 10^2
continue the cycle of operations until x = 0

x 
if first != last:
return False

"""






def palindrome_number(x: int) --> bool:
  y = x
  count = 0

  #handle negative inputs
  if x < 0:
      return False

  while y > 0:
      y = y//10
      count += 1
      
  divider = 10**(count - 1)
  
      
  #alternatively instead of using extra variable y, we can find our divider using this approach below
  """"
      ANOTHER METHOD TO GET THE INITIAL DIVIDER
      divider = 1
      #build the divider, until you get to the highest power of 10 that is less than or equal to the input x
      while 10 * divider <= x:
        divider = 10 * divider
      """

  #implement the loop to repeatedly compare first and last digit and then delete them
  while x > 0 and divider > 0:
      first = x // divider
      last = x % 10

      if first != last:
          return False

      x = x % divider #deletes the first digit
      x = x // 10 #deletes the last digit
      divider = divider / 100 #because we deleted two digits, the divider reduces by two powers of 10, i.e 10^2
      #continue the loop

  return True



print(palindrome_number(input()))

