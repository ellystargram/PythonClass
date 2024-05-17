print(r"Hello\nWorld")
python = "Python"
print(python[0])
print(python[1])
print(python[-1])
print(python[-2])
print(python[0:3])
print(python[2:5])

L = ["python", 1, 2, 3, 4, "last"]
print(L[0])
print(L[2:6])

L = [1, 2, 3]
L.append(4)
L.append(5)
print(len(L))

L.insert(0, -1)
L.insert(2, 0)
print(L)

L = [1, 2, 3]
L.extend([4, 5])
print(L)

L = ["a", "b", "c", "d", "e"]
print(L.pop(1))
print(L)

L = ["a", "b", "c", "d", "e", "b"]
print(L.remove("b"))
print(L)

L = ["a", "b", "c", "d", "e"]
L.clear()
print(L)

L = ["a", "b", "c", "d", "e"]
L.reverse()
print(L)
L.sort()
print(L)
L.sort(reverse=True)
print(L)

# tuple
t = ("a", "b", "c", "d", "e")
print(t[0])
print(t[1:3])

score = {"name": "최지훈", "math": 90, "english": 95}
print(score["name"])
score["history"] = 85
print(score)
del score["math"]
print(score)

add = 4 + 2
sub = 4 - 2
mul = 4 * 2
div = 4 / 2
rest = 4 % 2
print(add, sub, mul, div)
print(rest)
print(2 ** 10)

i = 0
sum = 0
while i <= 10:
    sum += i
    print(i)
    i += 2
    if False:
        continue

print(sum)

for i in range(0, 5):
    print(i, end=" ")

for i in range(0, 4):
    print(i, end=",")
for i in range(0, 5):
    print(i, end="\n")

print("math = {0}, english = {1}".format(90, 95))
print("math = {math}, english = {english}".format(math=90, english=95))

score = [80, 90, 100, 70]


def summer(*scores):
    sum = 0
    for i in scores:
        sum += i
    return (sum)


print("sum=", summer(*score))

print("sum=", summer(80, 90, 100, 70))
