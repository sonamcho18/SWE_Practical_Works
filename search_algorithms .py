def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()

# Exercise 1
def linear_search_all_indices(arr, target):
    indices = []
    for i, value in enumerate(arr):
        if value == target:
            indices.append(i)
    return indices

# Example usage
arr = [1, 2, 3, 2, 4, 2, 5]
target = 2
result = linear_search_all_indices(arr, target)
print(f"All indices where {target} appears: {result}")

# Exercise 2
def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

# Example usage
sorted_list = [1, 3, 5, 7, 9]
target = 6
insertion_point = binary_search_insertion_point(sorted_list, target)
print(f"Insertion point for {target} is at index {insertion_point}")

# Exercise 3
def linear_search_with_count(arr, target):
    comparisons = 0
    indices = []
    for i, value in enumerate(arr):
        comparisons += 1
        if value == target:
            indices.append(i)
    return indices, comparisons

# Example usage
arr = [1, 2, 3, 2, 4, 2, 5]
target = 2
result, comparison_count = linear_search_with_count(arr, target)
print(f"All indices where {target} appears: {result}")
print(f"Number of comparisons made: {comparison_count}")

# Exercise 4
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Finding the block where the target is present (if it is present)
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Doing a linear search for target in the block beginning with prev
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    # If the element is found
    if arr[prev] == target:
        return prev
    
    return -1

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 15
result = jump_search(sorted_list, target)
print(f"Index of {target} using jump search: {result}")

def linear_search_with_count(arr, target):
    comparisons = 0
    for i, value in enumerate(arr):
        comparisons