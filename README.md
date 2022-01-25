# Leetcode


## 1. Two Sum

[![Solve](https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/24/Actions-document-edit-icon.png)](https://leetcode.com/problems/two-sum/)

Topic prerequisites

- Dictionary

### Method to solve

- Given an array of numbers and target, at each element check if the required amount to add to the present element is present in the dictionary or not.
- If the difference is not present, add the present element and the index of the present element as a key value pair to the dictionary.
- If the difference is found, return the value of the key of the difference and the present element's index as a list of two indices.


## 2. Add Two Numbers

[![Solve](https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/24/Actions-document-edit-icon.png)](https://leetcode.com/problems/add-two-numbers/)

Topic prerequisites

- LinkedList

### Method to solve

- Get the size of each linked list
- Assign the number1 to the longer linked list and number2 to the shoter linked list.
- Traverse through the linked list till the smaller number is completely traversed.
- Keep adding the digits to the larger number and find carry by finding the remainder with 10 and find the digit with quotient with 10.
- Continue to do this with the extra digits, the larger number has.
- Finally, if carry has a non zero value, add the node in the end.
- Return the head of the longer linked list.


## 3. Longest Substring Without Repeating Characters

[![Solve](https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/24/Actions-document-edit-icon.png)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Topic prerequisites

- Sliding Window

### Method to solve

- Intialize an empty set, left pointer and result as 0.
- Start iterating using a right pointer.
- Using right pointer, find if the element at right pointer is in set.
- If the element at right pointer is in set, remove the left pointer element from the set as it is the cause of repetition.
- Keep removing until, no element is repeated.
- Add the right pointer element in the set.
- Maximize result as difference of left and right pointer including both the extreme elements.
- Return the result.


## 4. Median of Two Sorted Arrays

[![Solve](https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/24/Actions-document-edit-icon.png)](https://leetcode.com/problems/median-of-two-sorted-arrays/)

Topic prerequisites

- Binary Search

### Method to solve

- The number of elements on the left side and right side will be equal even after merging
- While iterating run only through the smaller list and that will give the remaining elements required to complete the array in the left half of the merged list
- Iterate till the leftmost element in array 2 (right half) is greter than rightmost element in array 1 (left half)
- Iterate till the leftmost element in array 1 (right half) is greter than rightmost element in array 2 (left half)
- If the element index reaches zero, assign the leftmax to be -infinity
- If the element index reaches maximum length, assign the rightmax to be infinity


## 6. Zigzag Conversion

[![Solve](https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/24/Actions-document-edit-icon.png)](https://leetcode.com/problems/zigzag-conversion/)

Topic prerequisites

- Matrix

### Method to solve

- Iterate through the string and keep increasing the column count till length of the string.
- For row count, increase till the extremes are reached. Reverse the directions at extremes.


## 7. Reverse Integer

[![Solve](https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/24/Actions-document-edit-icon.png)](https://leetcode.com/problems/reverse-integer/)

Topic prerequisites

- String conversion

### Method to solve

- Find the sign
- Convert integer to its absolute value
- Convert the integer to string and reverse it
- Convert it back to the integer and multiply the sign
- Convert it to integer
- Check for boundary cases
