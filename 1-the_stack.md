# The Stack
The stack is a very important aspect to programming. Aspects of it are found in many other data structures, and its use can be found everywhere. In this section, we will explore what the stack is, how it is used, and why it is important.

## Purpose of The Stack
The Stack data structure that is able to store data in a linear format. This is commonly related to a stack of pancakes, as you stack them starting from the bottom, and usually remove them starting from the top. The stack works very similarly, creating a list of data, and using the `pop()` function to remove the last piece of data added. There are ways to remove from other places, and otherwise manipulate the stack, but we will get to those later.

Since the stack is a very basic form of linear data management, it has a wide variety of uses. Pretty much any list of things can use a stack.

## Stack Functions
Functions that can be used with the stack are as follows:
* `append()` - adds a given value tot he front of the stack
* `push()` - adds a given value to the back of the stack
* `pop()` - removes and returns the value at a given index, or the last value if no index is given
* `del()` - removes a value at a given index
* `size()` - returns the size of the stack
* `empty()` - returns true if the stack is empty, or false if it is not

There are some other functions that can be used to manipulate the stack, but these are the basic ones that can be used in most circumstances.

## Example
Here is an example of the stack at work.

If we wanted to create a stack and add some values to it, we would create the variable and append values onto it.
```python
stack = []

stack.append(3)
stack.append(2)
stack.append(1)

print(stack)
```