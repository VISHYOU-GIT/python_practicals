# Selection sort algorithm
def selection_sort(arr):
    print("Initial array:", arr)
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: Swapped {arr[min_index]} with {arr[i]} -> {arr}")
    print("Array length:", len(arr))
    return arr

def print_sorted_array(arr):
    print("Sorted array:", arr)

print("Enter the number of elements in the array:")
n = int(input())
print("Enter the elements of the array:")
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
sorted_arr = selection_sort(arr)
print_sorted_array(sorted_arr)

"""
ALGORITHM:
1. For each position i from 0 to n-1:
   a. Find the minimum element in the remaining unsorted array
   b. Swap the minimum element with element at position i
2. After each iteration, the sorted portion grows by one element

EXAMPLE OUTPUT:
Enter the number of elements in the array:
5
Enter the elements of the array:
64
25
12
22
11
Initial array: [64, 25, 12, 22, 11]
Step 1: Swapped 25 with 11 -> [11, 25, 12, 22, 64]
Step 2: Swapped 25 with 12 -> [11, 12, 25, 22, 64]
Step 3: Swapped 25 with 22 -> [11, 12, 22, 25, 64]
Step 4: Swapped 25 with 25 -> [11, 12, 22, 25, 64]
Step 5: Swapped 64 with 64 -> [11, 12, 22, 25, 64]
Array length: 5
Sorted array: [11, 12, 22, 25, 64]

Time Complexity: O(n²) - always makes n(n-1)/2 comparisons
Space Complexity: O(1) - sorts in place
Characteristics: Not stable, but makes minimum number of swaps
"""