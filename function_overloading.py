#program to demonstrate function overloading
def add(a, b, c=0):
    if c is None:
        return a + b
    return a + b + c

print(add(5, 10))
print(add(5, 10, 15))

"""
ALGORITHM:
1. Define function with optional parameter (default value)
2. Check if optional parameter is provided
3. Return sum of two numbers if third parameter not given
4. Return sum of three numbers if third parameter is given

EXAMPLE OUTPUT:
15
30

Note: Python doesn't have true function overloading like Java/C++
Instead, it uses default parameters to simulate function overloading
Time Complexity: O(1)
Space Complexity: O(1)
"""