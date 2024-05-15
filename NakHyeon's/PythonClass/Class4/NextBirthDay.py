import datetime

target_date = input("Enter your birthdate (yyyy-mm-dd): ")
target_date = datetime.datetime.strptime(target_date, "%Y-%m-%d")

today = datetime.datetime.now()
next_birthday = datetime.datetime(today.year, target_date.month, target_date.day)
if today > next_birthday:
    next_birthday = datetime.datetime(today.year + 1, target_date.month, target_date.day)

days_left = (next_birthday - today).days + 1

print("Days left for your next birthday:", days_left)
