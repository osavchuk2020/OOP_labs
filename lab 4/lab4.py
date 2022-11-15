import math

a = "lorem ipsum" #string
b = 1 # number
c = ["a", 1, 1.25, "text"] # List
d = {"a": "text", "b": 1} # Dict
e = ("a", ) # Tuple
f = {"ss", } # Set

print("string variable: ", a)
print("constant FALSE = ", False)
print("constant TRUE = ", True)
print("constant NONE = ", None)

print(abs(-12.5), f"equals {abs(12.5)}")
print(pow(13, 2), f"equals {13**2}")
print(round(10/3, 3))

letters = ["a", "b", "c"]
print("list of letters:")
for i in range(len(letters)):
    print(f"{i+1}. {letters[i]}")

i = 0
while letters[i] != "c":
    print(f"{i}. {letters[i]}")
    i += 1

print("b = 1" if b == 2 else f"b = {b}")
print(f"name = {name}" if "name" in locals() else "variable `name` doesnt exist")

negNum = -100
try: 
    print(f"square root of {negNum} equals", math.sqrt(negNum))
except Exception as e:
    print("ERROR:", e)
finally:
    print("(this math operation cannot be performed)")

with open("textFile.txt", 'w') as fileObject:
    fileObject.write("lorem ipsum")

compare = lambda a, b: f"{a} > {b}" if a > b else f"{a} < {b}" if a < b else f"{a} = {b}"
print(compare(3, 2))