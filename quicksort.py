import random


NUMBERS = (1,2,4,4,5,6,7,8,8,9,34,56,89, 74,3,21,33,3,2,1,1,0,-87)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    base_element = random.choice(arr)
    left = [n for n in arr if n < base_element]
    middle = [n for n in arr if n == base_element]
    right = [n for n in arr if n > base_element]
    
    return quicksort(left) + middle + quicksort(right)
  
if __name__ == "__main__":
  unsorted_arr = random.sample(NUMBERS, len(NUMBERS))
  print(unsorted_arr)
  sorted_arr = quicksort(unsorted_arr)
  print(sorted_arr)
    
