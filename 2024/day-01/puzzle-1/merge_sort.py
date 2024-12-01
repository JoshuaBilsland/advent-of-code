def merge(left, right):
    merged = []  # the merged items
    left_index = 0
    right_index = 0

    # while there are still items to merge
    while left_index < len(left) and right_index < len(right):
        # add the smallest number
        left_value = left[left_index]
        right_value = right[right_index]
        if left_value < right_value:
            merged.append(left_value)
            left_index += 1
        else:
            merged.append(right_value)
            right_index += 1

    # Append any remaining items
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def merge_sort(items):
    # recursion will stop when list has been divided into single item lists
    if len(items) <= 1:
        return items
    else:
        midpoint = len(items)//2
        left_half = items[:midpoint]
        right_half = items[midpoint:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        merged_items = merge(left_half, right_half)

        return merged_items
