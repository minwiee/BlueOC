def sum_of_top_two(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two integers")
    
    # Initialize two variables to hold the two largest values
    first_max = float('-inf')
    second_max = float('-inf')
    
    # Iterate through the array
    for num in arr:
        if num > first_max:
            second_max = first_max  # Update second largest before updating the largest
            first_max = num
        elif num > second_max:
            second_max = num  # Update the second largest if current number is less than the largest

    return first_max + second_max

big_integers = [9223372036854775807, 9223372036854775806]  

# Test cases
print(sum_of_top_two(big_integers))
print(sum_of_top_two([1, 4, 2, 3, 5]))  
print(sum_of_top_two([10, 1, 8, 3, 6]))  # Output: 18
print(sum_of_top_two([-10, -1, -8, -3, -6]))  # Output: -4
print(sum_of_top_two([0, 0, 0, 1, 0]))  # Output: 1
