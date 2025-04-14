def merge_sort_by_length(strings):
    """Sorts a list of strings by length from longest to shortest using merge sort."""
    if len(strings) <= 1:
        return strings

    mid = len(strings) // 2
    left = merge_sort_by_length(strings[:mid])
    right = merge_sort_by_length(strings[mid:])

    return merge(left, right)

def merge(left, right):
    """Merges two lists sorted by string length (longest to shortest)."""
    result = []
    while left and right:
        if len(left[0]) >= len(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left + right
    return result

# List 1
list1 = ["apple", "banana", "cherry", "fig", "grapefruit", "date", "kiwi", "lemon", "mango", "nectarine"]
# List 2
list2 = ["sunshine", "rain", "thunderstorm", "cloud", "mist", "hail", "snowflake", "fog", "breeze", "cyclone"]
# List 3
list3 = ["table", "chair", "wardrobe", "lamp", "bookshelf", "mirror", "couch", "rug", "desk", "stool"]

# Sort and print each list
print("Sorted list1:", merge_sort_by_length(list1))
print("Sorted list2:", merge_sort_by_length(list2))
print("Sorted list3:", merge_sort_by_length(list3))

