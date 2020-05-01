
from timeit import timeit

""" try:
    with open("dictionary.py") as file:
        print("File opened. ")

    #file = open("dictionary.py")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("not a valid age")
    # print(ex)
    # print(type(ex))
# except ZeroDivisionError:
#     print("Age cannot be zero")
else:
    print("No exception were thrown")
# finally:
#     print("No exceptions ")
#     file.close()
print("Execution continues") """


code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age canot be 0 or less")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
   pass
"""

print("First code", timeit(code1, number=10000))


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("Seconde code", timeit(code2, number=10000))
