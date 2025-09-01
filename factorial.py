#Write a Python program to compute the factorial of a number using both recursive and iterative methods.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
 
num = int(input("Enter a number to compute its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial (recursive):", factorial(num))
    print("Factorial (iterative):", factorial_iterative(num))

"""
ALGORITHM:
Recursive Method:
1. Base case: if n == 0, return 1
2. Recursive case: return n * factorial(n-1)

Iterative Method:
1. Initialize result = 1
2. Loop from 2 to n (inclusive)
3. Multiply result by each number in the range

EXAMPLE OUTPUT:
Enter a number to compute its factorial: 5
Factorial (recursive): 120
Factorial (iterative): 120

Mathematical Formula: n! = n × (n-1) × (n-2) × ... × 2 × 1
Time Complexity: O(n) for both methods
Space Complexity: O(n) for recursive (due to call stack), O(1) for iterative
"""