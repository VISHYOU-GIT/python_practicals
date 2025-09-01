#write a program for checking whether a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

"""
ALGORITHM:
1. If number <= 1, return False (not prime)
2. Check divisibility from 2 to √n:
   - If any number divides n evenly, return False (not prime)
3. If no divisors found, return True (prime)

EXAMPLE OUTPUT:
Enter a number to check if it's prime: 17
17 is a prime number.

Enter a number to check if it's prime: 15
15 is not a prime number.

Mathematical Principle: A prime number has exactly two factors: 1 and itself
Optimization: Only check up to √n as larger factors would have been found earlier
Time Complexity: O(√n)
Space Complexity: O(1)
"""