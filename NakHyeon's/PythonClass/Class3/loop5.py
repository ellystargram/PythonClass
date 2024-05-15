animals = []
user_input = ""

print("make a list of animals")
print("one by one")
print("type blank to stop")

while True:
    user_input = input("Enter the animal: ").lower().strip()
    if user_input == "":
        break
    if user_input in animals:
        print("This animal is already in the list")
        continue
    animals.append(user_input)

animals.sort()

print("List of animals: ")

for animal in animals:
    print(animal)
