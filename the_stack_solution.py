stack = []

def sortedStack(number):
    last = len(stack) - 1

    if len(stack) != 0:
        if number > stack[last]:
            stack.append(number)
            return
        else:
            index = 0
            for value in stack:
                if number < value:
                    stack.insert(index, number)
                    return
                index += 1
    else:
        stack.append(number)
        return

print("Test 1:")
sortedStack(5)
sortedStack(4)
sortedStack(3)
sortedStack(8)
sortedStack(6)
sortedStack(9)
sortedStack(1)
sortedStack(7)
sortedStack(2)
print(stack) # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
stack = []

print("Test 2:")
sortedStack(34)
sortedStack(7)
sortedStack(12)
sortedStack(56)
sortedStack(44)
sortedStack(45)
sortedStack(90)
sortedStack(25)
sortedStack(1)
print(stack) # Expected: [1, 7, 12, 25, 34, 44, 45, 56, 90]
stack = []

print("Test 3:")
sortedStack(0.1)
sortedStack(0.7)
sortedStack(0.3)
sortedStack(0.4)
sortedStack(0.8)
sortedStack(0.2)
sortedStack(0.5)
sortedStack(0.9)
sortedStack(0.6)
print(stack) # Expected: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
stack = []