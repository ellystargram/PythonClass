import datetime

# bornYear = int(input("태어난 년도를 입력하세요: "))

today = datetime.date.today()
print(today, "기준")

# print("당신의 나이는 세는 나이로", today.year - bornYear + 1, "세 입니다.")

bornDate = input("태어난 날짜를 입력하세요(yyyy-mm-dd): ")
bornDate = datetime.datetime.strptime(bornDate, "%Y-%m-%d")

trueAge = today.year - bornDate.year
if today.month < bornDate.month or (today.month == bornDate.month and today.day < bornDate.day):
	trueAge -= 1
print("당신의 나이는 윤석열 나이로", trueAge, "세 입니다.")
print("당신의 태어난 요일은", bornDate.strftime("%A"), "입니다.")
