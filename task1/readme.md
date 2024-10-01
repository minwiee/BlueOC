# Task 1: String Length Frequency

## Objective
Write a function that identifies the most frequent string lengths in an array of strings.

## Requirements
- Provide multiple test cases.
- Use any language you prefer; **JavaScript** or **Python** is recommended.
- [Optional] Include a unit test function.

## Example
**Input:**  
['a', 'ab', 'abc', 'cd', 'def', 'gh']

**Explanation:**  

The task requires identifying the most frequent string length in an array of strings and returning all strings that match this length.

**Step-by-Step Breakdown:**
1. **Input Analysis**:  
   For an input array `['a', 'ab', 'abc', 'cd', 'def', 'gh']`, we calculate the length of each string:
   - `'a'` has 1 character.
   - `'ab'`, `'cd'`, and `'gh'` have 2 characters.
   - `'abc'` and `'def'` have 3 characters.

2. **Frequency Calculation**:  
   We then determine how often each string length occurs in the array:
   - 1 character → occurs 1 time (`'a'`).
   - 2 characters → occurs 3 times (`'ab'`, `'cd'`, `'gh'`).
   - 3 characters → occurs 2 times (`'abc'`, `'def'`).

3. **Find the Most Frequent Length**:  
   In this example, the most frequent string length is **2 characters**, occurring 3 times.

4. **Result**:  
   Once we identify the most frequent string length (2), we collect all strings with that length. In this case, the strings `'ab'`, `'cd'`, and `'gh'` all have 2 characters, so they are returned in the output.

**Output:**  
['ab', 'cd', 'gh']
