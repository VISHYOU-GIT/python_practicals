#wap to calculate greatest common divisor of two numbers
import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd_result = gcd(num1, num2)
built_in_gcd_result = math.gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd_result}.")
print(f"The GCD of {num1} and {num2} using built-in function is {built_in_gcd_result}.")

"""
ALGORITHM (Euclidean Algorithm):
1. While b is not zero:
   a. Store b in temporary variable
   b. Set b = a % b (remainder)
   c. Set a = temporary variable
2. Return a (GCD)

EXAMPLE OUTPUT:
Enter first number: 48
Enter second number: 18
The GCD of 48 and 18 is 6.
The GCD of 48 and 18 using built-in function is 6.

Mathematical Principle: GCD(a,b) = GCD(b, a mod b)
Time Complexity: O(log(min(a,b)))
Space Complexity: O(1)
"""

