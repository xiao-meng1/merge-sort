# my implementation of merge sort


arr = [9, 7, 1, 5, 10, 17, 7, 16]


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        left_array = array[0:int(len(array) / 2)]
        right_array = array[int(len(array) / 2):]
        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)
        sorted_array = merge(left_array, right_array)
        return sorted_array


def merge(left_array, right_array):
    left_pointer = 0
    right_pointer = 0
    sorted_array = []
    for i in range(0, len(left_array) + len(right_array)):
        if left_pointer == len(left_array):
            sorted_array.extend(right_array[right_pointer:])
            break
        elif right_pointer == len(right_array):
            sorted_array.extend(left_array[left_pointer:])
            break
        else:
            if left_array[left_pointer] >= right_array[right_pointer]:
                sorted_array.extend([right_array[right_pointer]])
                right_pointer += 1
            else:
                sorted_array.extend([left_array[left_pointer]])
                left_pointer += 1
    return sorted_array


print(merge_sort(arr))
