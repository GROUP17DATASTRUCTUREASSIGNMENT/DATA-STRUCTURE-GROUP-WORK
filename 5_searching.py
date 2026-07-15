# Task 5: Searching (Linear Search vs. Binary Search)
# Time Complexities:
# - Linear Search: O(N) worst/average case
# - Binary Search: O(log N) worst/average case (assumes pre-sorted array)

def linear_search(arr, target):
    """Perform Linear Search and return (index, comparison_count)."""
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search(arr, target):
    """Perform Binary Search on a sorted array and return (index, comparison_count)."""
    comparisons = 0
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons


# --- Demonstration ---
if __name__ == "__main__":
    print("--- 5. Searching Demonstration ---")
    # Sorted list of exactly 20 items
    sorted_list = [5, 12, 17, 23, 29, 35, 41, 47, 53, 59, 64, 70, 75, 81, 88, 92, 95, 99, 104, 110]
    print(f"Target Array: {sorted_list} (Length: {len(sorted_list)})")
    
    target_value = 81
    print(f"Searching for target value: {target_value}\n")
    
    # Linear Search execution
    idx_linear, comp_linear = linear_search(sorted_list, target_value)
    print(f"Linear Search: Found at index {idx_linear} with {comp_linear} comparisons.")
    
    # Binary Search execution
    idx_binary, comp_binary = binary_search(sorted_list, target_value)
    print(f"Binary Search: Found at index {idx_binary} with {comp_binary} comparisons.")