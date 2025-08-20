import sys
import sysconfig
import re

# Check if given String is a Palindrome or NOT:

# Algorithm is ::

# 1. Define a function that takes String as an Input Parameter and returns None
# 2. The function should ignore spaces, punctuation, and case differences from the Input String.
# 3. Reverse the regex applied String
# 4. Compare both the strings and verify if same or not.
# 5. If both are same then print message saying Palindrome else Not a Palindrome!

def is_palindrome(input_str: str) -> bool:

    cleaned_str = re.sub(r'[^A-Za-z0-9]', '', input_str).lower()

    # String Reverse
    reversed_str = cleaned_str[::-1]

    # Compare both the strings

    if cleaned_str == reversed_str:
        print("Given String is a Palindrome!!!")
        return True
    else:
        print("Given String is a NOT a Palindrome!!!")
        return False

    # return bool

def main():
   
   user_input = input("Enter a String: ")
   print(is_palindrome(user_input))

   print(is_palindrome("A man, a plan, a canal: Panama"))
   print(is_palindrome("Hello, World!"))          

if __name__ == '__main__':
    main()