""" x = 1
print(id(x)) """
message = " Python Programming"

""" fisrt = "Inoussa"
last = "Mouiche"
full = f"{fisrt} {last}"
full1 = f"{len(fisrt)} { 2 + 4}" """

""" print(message.upper())
print(message.rstrip())
print(message.title())
print(message.find("Pro"))

print(message.replace("P", "-")) """

# x = input("x ")
# y = x + 1

""" names = ["QJhon", "Mary"]
for name in names:
    if name.startswith("J"):
        print("found")
        break

else:
    print("Not found") """

""" guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))

"""


""" def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2))
 """


def save_user(**user):
    print(user)


save_user(id=1, name="Admin")
