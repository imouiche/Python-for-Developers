
chars = list("Hello World")
print(chars)

items = [
    ("prduct1", 10),
    ("prduct2", 9),
    ("prduct3", 12)
]


""" def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
 """
# Using lambda expression
items.sort(key=lambda item: item[1])
print(items)

prices = [item[1] for item in items]
print(prices)

x = map(lambda item: item[1], items)
print(list(x))

# Filter
filtered = filter(lambda item: item[1] >= 10, items)
print(list(filtered))
filtered = [item for item in items if item[1] >= 10]

# Zip fucntion
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2, "abc")))
