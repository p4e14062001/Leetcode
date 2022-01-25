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
