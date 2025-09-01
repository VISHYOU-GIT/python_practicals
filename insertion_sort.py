#insertion sort algorithm
def insertion_sort(arr):
    print("Initial array:", arr)
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        print(f"Step {i}: Inserting {key} into the sorted portion {arr[:i]}")
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
        print(f"     After insertion: {arr[:i+1]}")

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
sorted_arr = insertion_sort(arr)
print_sorted_array(sorted_arr)

"""
ALGORITHM:
1. Start from second element (index 1)
2. For each element (key), compare with elements in sorted portion
3. Shift larger elements one position to the right
4. Insert key at correct position
5. Repeat until all elements are processed

EXAMPLE OUTPUT:
Enter the number of elements in the array:
5
Enter the elements of the array:
64
34
25
12
22
Initial array: [64, 34, 25, 12, 22]
Step 1: Inserting 34 into the sorted portion [64]
     After insertion: [34, 64]
Step 2: Inserting 25 into the sorted portion [34, 64]
     After insertion: [25, 34, 64]
Step 3: Inserting 12 into the sorted portion [25, 34, 64]
     After insertion: [12, 25, 34, 64]
Step 4: Inserting 22 into the sorted portion [12, 25, 34, 64]
     After insertion: [12, 22, 25, 34, 64]
Array length: 5
Sorted array: [12, 22, 25, 34, 64]

Time Complexity: O(n²) worst case, O(n) best case
Space Complexity: O(1)
"""