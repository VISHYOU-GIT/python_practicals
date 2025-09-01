#implement a python program to find the largest number from a list of numbers
numbers = list(map(int, input("Enter numbers separated by ,: ").split(",")))
largest = max(numbers) if numbers else None
print(f"The largest number in the list is: {largest}")

"""
ALGORITHM:
1. Take input as comma-separated numbers
2. Split the input string by commas
3. Convert each string element to integer
4. Use built-in max() function to find largest number
5. Handle empty list case

EXAMPLE OUTPUT:
Enter numbers separated by ,: 10,25,3,99,45,12
The largest number in the list is: 99

Time Complexity: O(n) where n is the number of elements
Space Complexity: O(n) for storing the list
Note: Uses Python's built-in max() function for efficiency
"""
