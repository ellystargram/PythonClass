import random

# print(random.randint(1, 6))

idols = ["칸나", "유니", "리제", "타비", "마시로", "히나", "릴파", "징버거", "아이네", "비챤", "고세구", "주르르"]
status = ["귀여운", "섹시한", "멋진", "예쁜", "아름다운", "똑똑한", "바보같은", "핫한"]
print("I have a", random.choice(status), random.choice(idols), "in my house.")

jusawi1 = random.randint(1, 12)
jusawi2 = random.randint(1, 12)
print("jusawi1:", jusawi1, "jusawi2:", jusawi2, "sum:", jusawi1 + jusawi2)

a = int(input("Enter a number: "))