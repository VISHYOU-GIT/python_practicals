# Implement a binary search algorithm in Python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = []
n = int(input("Enter number of elements in the array: "))
print("Enter the elements of the array:")
for i in range(n):
    num = int(input())
    arr.append(num)
   
target = int(input("Enter the number to search for: "))
result = binary_search(arr, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")

"""
ALGORITHM:
1. Initialize low pointer to 0 and high pointer to last index
2. While low <= high:
   a. Calculate mid = (low + high) // 2
   b. If arr[mid] == target, return mid (found)
   c. If arr[mid] < target, search right half (low = mid + 1)
   d. If arr[mid] > target, search left half (high = mid - 1)
3. Return -1 if element not found

EXAMPLE OUTPUT:
Enter number of elements in the array: 5
Enter the elements of the array:
10
20
30
40
50
Enter the number to search for: 30
Element found at index: 2

Time Complexity: O(log n)
Space Complexity: O(1)
Note: Array must be sorted for binary search to work correctly
"""
