stack = [0] * 10
top = -1

top += 1 
stack[top] = 1  # push(1)
top += 1 
stack[top] = 2  # push(2)
top += 1 
stack[top] = 3  # push(3)

print(stack[top])  # pop()
top -= 1
top -= 1
print(stack[top+1])  # pop()

