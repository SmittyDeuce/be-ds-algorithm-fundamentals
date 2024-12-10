'''Problem Statement: Consider a sorting algorithm that arranges an
array of integers in ascending order. The challenge is to analyze
the Big O complexity of the algorithm and assess its efficiency in
various scenarios.'''
arr = [5, 2, 9, 1, 5, 6]

def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 2, 9, 1, 5, 6]
simple_sort(arr)
print("Sorted array:", arr)

# Task 1: Identifying Key Operations
# Analyze the provided algorithm and identify the key operations it performs.

'''It Iterates through the array twice. the outer loop iterates n times
while the inner iterates over and over again until the array is sorted getting
smaller each time it iterates. with 
if arr[j] > arr[j+1]:
    arr[j], arr[j+1] = arr[j+1], arr[j]

it compares if the current element arr[j] > the next arr[j+1]
then it swaps them with arr[j], arr[j+1] = arr[j+1], arr[j]
'''





# Task 2: Calculating Big O Complexity

# Apply the principles of Big O notation
# to express how the algorithm's runtime
# grows concerning the size of the input

'''The growth is quadratic because the total number of comparisons
grows proportionally to O(n^2) as the size of the input n increases.
'''


# Task 3: Efficiency Analysis:

# Propose potential improvements or alternative
# algorithms that might offer better performance

'''
**Heap Sort** builds a binary heap from the input data.
It repeatedly extracts the maximum (or minimum) element from
the heap and reconstructs the heap until the array is sorted.

- **Time Complexity**: **O(n log n)** in both the average and worst case.
- **Space Complexity**: **O(1)**, as it sorts in-place without needing extra space for merging (unlike Merge Sort).
- **Why It's Better**: Heap Sort has a guaranteed **O(n log n)** time complexity, unlike Bubble Sort's **O(n^2)**.

It also doesn't require extra space for merging, making it more efficient
in space-constrained environments.'''