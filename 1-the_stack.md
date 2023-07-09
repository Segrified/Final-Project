# The Stack
The stack is a very important aspect to programming. Aspects of it are found in many other data structures, and its use can be found everywhere. In this section, we will explore what the stack is, how it is used, and why it is important.

## Purpose of The Stack
The Stack data structure that is able to store data in a linear format. This is commonly related to a stack of pancakes, as you stack them starting from the bottom, and usually remove them starting from the top. The stack works very similarly, creating a list of data, and using the `pop()` function to remove the last piece of data added. There are ways to remove from other places, and otherwise manipulate the stack, but we will get to those later.

Since the stack is a very basic form of linear data management, it has a wide variety of uses. Pretty much any list of things can use a stack.

## Stack Functions
Functions that can be used with the stack are as follows:
* `append()` - adds a given value to the front of the stack
* `pop()` - removes and returns the value at a given index, or the last value if no index is given
* `del()` - removes a value at a given index
* `len()` - returns the amount of values in the stack

There are some other functions that can be used to manipulate the stack, but these are the basic ones that can be used in most circumstances.

### Usage
If we wanted to create a stack and add some values to it, we would create the variable and append values onto it.
```python
stack = []

stack.append(3)
stack.append(2)
stack.append(1)

print(stack)
```

Would return
> [3, 2, 1]

And if we wanted to remove values from it, we could use the `pop()` function, which removes starting from the last value if no index is given.
```python
stack = [3, 2, 1]

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
```

Would return
> 1
> 2
> 3
> []

## Example
Here is an example of the stack at work.

Say we had a lot of tasks to do in a day, but could only complete 5 of them. Assuming we feed the tasks into the stack in order of importance, let's make sure we get the most important ones done first.

The following example shows adding tasks to the stack, and removing the ones we don't have time for.
```python
tasks = []

tasks.append("Finish Homework")
tasks.append("Feed the dog")
tasks.append("Take out the trash")
tasks.append("Do the dishes")
tasks.append("Do Laundry")
tasks.append("Get more cereal")
tasks.append("Surf the internet")

while len(tasks) > 5:
    tasks.pop()

print(tasks)
```

## Problem to Solve
Write a program that is able to organize a list of numbers as they are fed to it. It should be able to search the list and find a place for each value. For this problem, you can assume there will be no repeating numbers.

Test your program against the following number strings:
* 6, 5, 8, 3, 2, 9, 1
* 5, 20, 4, 33, 62, 3
* 