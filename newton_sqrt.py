#implement a python program to caculate the square root of a number by using Newton's method
def newton_sqrt(N, tolerance=1e-6):
    x = N
    while True:
        root = 0.5 * (x + N / x)
        if abs(root - x) < tolerance:
            return root
        x = root

num = float(input("Enter a number to calculate its square root: "))
if num < 0:
    print("Square root is not defined for negative numbers.")
else:
    sqrt_result = newton_sqrt(num)
    print(f"The square root of {num} is approximately {sqrt_result}.")

"""
ALGORITHM (Newton-Raphson Method):
1. Start with initial guess x = N (the number itself)
2. Repeat until convergence:
   - Calculate new approximation: root = 0.5 * (x + N/x)
   - If |root - x| < tolerance, return root (converged)
   - Otherwise, set x = root and continue
3. Return the final approximation

EXAMPLE OUTPUT:
Enter a number to calculate its square root: 25
The square root of 25.0 is approximately 5.0.

Enter a number to calculate its square root: 10
The square root of 10.0 is approximately 3.1622776601683795.

Mathematical Formula: x_new = (x_old + N/x_old) / 2
Time Complexity: O(log log n) - very fast convergence
Space Complexity: O(1)
Tolerance: 1e-6 (adjustable for required precision)
"""