# Write a program to check whether a number is odd or even
num = int(input("Enter a number to check if it is odd or even: "))
print(f"The number {num} is {'Even' if num % 2 == 0 else 'Odd'}.")

"""
ALGORITHM:
1. Take input number from user
2. Use modulo operator (%) to find remainder when divided by 2
3. If remainder is 0, number is even
4. If remainder is 1, number is odd
5. Display result using conditional expression

EXAMPLE OUTPUT:
Enter a number to check if it is odd or even: 42
The number 42 is Even.

Enter a number to check if it is odd or even: 17
The number 17 is Odd.

Mathematical Principle: Even numbers are divisible by 2 (remainder = 0)
Time Complexity: O(1)
Space Complexity: O(1)
"""