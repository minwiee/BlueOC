def most_frequent_string_lengths(arr):
    length_frequency = {}
    
    # Calculate frequency of string lengths
    for string in arr:
        length = len(string)
        length_frequency[length] = length_frequency.get(length, 0) + 1

    # Find the most frequent length
    max_frequency = 0
    most_frequent_lengths = []
    for length, frequency in length_frequency.items():
        # print(length, frequency)
        if frequency > max_frequency:
            max_frequency = frequency
            most_frequent_lengths = [length]
            # print(most_frequent_lengths)
        elif frequency == max_frequency:
            most_frequent_lengths.append(length)
        

    # Collect strings of the most frequent length(s)
    result = [string for string in arr if len(string) in most_frequent_lengths]
    return result

# Test Cases
test_cases = [
    (['a', 'ab', 'abc', 'cd', 'def', 'gh'], ['ab', 'cd', 'gh']),
    (['hello', 'world', 'hi', 'test', 'js', 'code'], ['hello', 'world', 'hi', 'test', 'js', 'code']),
    (['one', 'two', 'three', 'four', 'five', 'six'], ['one', 'two', 'six']),
    (['a', 'bb', 'ccc', 'dd', 'ee', 'ffff'], ['bb', 'dd', 'ee']),
    (['short', 'longer', 'longest'], ['short', 'longer', 'longest'])
]

# Unit Test Function

def run_tests():
    for index, (input_data, expected) in enumerate(test_cases):
        result = most_frequent_string_lengths(input_data)
        print(input_data, " -> ", result)
        assert result == expected, f"Test Case {index + 1} failed: expected {expected}, got {result}"
    print("All test cases passed.")

# Run the tests

run_tests()
