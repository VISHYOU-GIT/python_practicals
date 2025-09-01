# Implement a linear search algorithm in Python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr =[]
n = int(input("Enter number of elements in the array: "))
print("Enter the elements of the array:")
for i in range(n):
    num = int(input())
    arr.append(num)
target = int(input("Enter the number to search for: "))
result = linear_search(arr, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")

"""
ALGORITHM:
1. Start from first element (index 0)
2. Compare each element with target value
3. If match found, return the index
4. If end of array reached without finding target, return -1

EXAMPLE OUTPUT:
Enter number of elements in the array: 5
Enter the elements of the array:
10
25
30
15
40
Enter the number to search for: 30
Element found at index: 2

Time Complexity: O(n) where n is the number of elements
Space Complexity: O(1)
Note: Linear search works on both sorted and unsorted arrays
"""
