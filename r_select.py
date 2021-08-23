import random


NUMBERS = (9,8,7,6,5,4,3,2,1,0)


def r_select(arr, i):
    """ find i-lowest element in arr"""
    if len(arr) == 1:
        return arr[0]
    
    base_element = random.choice(arr)
    
    print(f"Base element: {base_element}")
    
    left = [n for n in arr if n < base_element]
    right = [n for n in arr if n > base_element]
    
    divided_arr = left + [base_element] + right
    
    print(f'Divided arr: {divided_arr}')
    
    base_element_position = divided_arr.index(base_element) + 1
    
    if i < base_element_position:
        return r_select(left, i)
    elif i > base_element_position:
        return r_select(right, i - base_element_position)
    else:
        return base_element

      
if __name__ == "__main__":
  print(r_select(NUMBERS, 10))  # 9
  print(r_select(NUMBERS, 3))   # 2


    
