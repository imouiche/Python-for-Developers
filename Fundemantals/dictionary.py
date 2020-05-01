
from sys import getsizeof

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)  # better approach

print(point["x"])

point["x"] = 10
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])

print(point.get("a"), 0)  # 0 as default if key does not exist

del point["x"]
print(point)

for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)

# comprehension
values = {x: x*2 for x in range(5)}
print(values)

# genrator objects
values = (x*2 for x in range(1000))
print("gen", getsizeof(values))

# Umpack operator
values = list(range(5))
values = [*range(5), *"Hello"]  # like spread operator in js

print(values)

first = {"x": 1}
second = dict(x=10, y=2)

combined = {**first, **second, "z": 1}

print(combined)
