import math
import Ra


def add(a, b):
	return a + b


def sub(a, b):
	return a - b


def mul(a, b):
	return a * b


def div(a, b):
	return a / b


def power(a, b):
	return math.pow(a, b)


def sqrt(a):
	return math.sqrt(a)


print(add(1, 2))
print(sub(1, 2))
print(mul(1, 2))
print(div(1, 2))
print(random.randint(1, 100))
print(power(2, 3))
print(sqrt(4))

print(power(2, 2.5))

print("Fu", "ck")

name = "John Doe"
print(name)
print(name.find("Doe"))

myName = "techno.sexking"
print("hello, my name is", myName, "and I am a programmer")

asdf = input("Enter your name: ")
print("Hello", asdf)

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
print("Hello", firstName, lastName)
