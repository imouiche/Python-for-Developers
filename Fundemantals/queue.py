
from collections import deque
from array import array
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

print(queue)

if not queue:
    print("queue is empty")

# Arrays
numbers = array("i", [1, 2, 3])
numbers.insert(0, 4)

# Sets
numbers = [1, 1, 2, 3, 4]
first = set(numbers)  # remove duplicates
second = {1, 5}

print(first | second)  # get the union

print(first & second)  # intersection

print(first - second)  # difference
print(first ^ second)  # symetric difference
