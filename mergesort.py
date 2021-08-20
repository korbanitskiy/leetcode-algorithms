import random
import itertools


NUMBERS = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

def merge(arr1, arr2):
    container = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            container.append(arr1[i])
            i += 1
        else:
            container.append(arr2[j])
            j += 1
    
    container.extend(arr1[i:])
    container.extend(arr2[j:])
    return container


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    sorted_left = mergesort(left)
    sorted_right = mergesort(right)
    return merge(sorted_left, sorted_right)


if __name__ == "__main__":
    unsorted_arr = random.sample(NUMBERS, len(NUMBERS))
    print(unsorted_arr)
    sorted_arr = mergesort(unsorted_arr)
    print(sorted_arr)
