#implement a python program to find the largest number from a list of numbers
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

num_list=[10, 20, 30, 40, 50]
print("The largest number in the list is:", find_largest(num_list))
print("The largest number in the list using max is:", max(num_list))  # Using built-in max for comparison

"""
ALGORITHM:
1. Initialize largest with first element of the list
2. Iterate through each element in the list
3. If current element is greater than largest, update largest
4. Return the largest element found

EXAMPLE OUTPUT:
The largest number in the list is: 50
The largest number in the list using max is: 50

Time Complexity: O(n) where n is the number of elements
Space Complexity: O(1)
Alternative: Python's built-in max() function provides the same functionality
"""