def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    left_index = right_index = 0

    # Compare elements from both arrays and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Concatenate any remaining elements from both arrays (if any)
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
