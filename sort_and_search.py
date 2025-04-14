numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

def linear_search(lst, target):
    """Searches for target using linear search."""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

print("Using Linear Search on unsorted list:")
index = linear_search(numbers, 9)
print("Number 9 found at index:", index)

def insertion_sort(lst):
    """Sorts a list using insertion sort."""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

sorted_numbers = insertion_sort(numbers.copy())
print("\nSorted list with Insertion Sort:")
print(sorted_numbers)

def binary_search(lst, target):
    """Searches for target using binary search (on sorted list)."""
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print("\nUsing Binary Search on sorted list:")
index = binary_search(sorted_numbers, 9)
print("Number 9 found at index:", index)
