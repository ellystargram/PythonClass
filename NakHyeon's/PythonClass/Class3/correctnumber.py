import toolkit

min_num = 50
max_num = 200

random_number = toolkit.random.randint(min_num, max_num)

user_input = ""
count_tries = 0

sudo = False

while user_input != "exit":
    if sudo:
        user_input = input("SUDO: Enter the number: ").lower().strip()
    else:
        user_input = input("Enter the number: ").lower().strip()
    if user_input == "exit":
        break
    elif user_input.startswith("sudo"):
        print("you are super user now!")
        sudo = True
        continue
    elif user_input.startswith("dosu"):
        sudo = False
        print("you are normal user now!")
        continue
    elif sudo and user_input.startswith("set"):
        user_input = user_input.replace("set", "").strip()
        if user_input == "":
            print("random number is changed")
            random_number = toolkit.random.randint(min_num, max_num)
        else:
            random_number = int(user_input)
            print("random number is changed to ", random_number)
        continue
    elif sudo and user_input.startswith("get"):
        print("random number is ", random_number)
        continue
    if not user_input.isdigit():
        print("Please enter a number")
        continue
    if user_input == str(random_number):
        print("Correct number!")
        print(count_tries + 1)
        break
    elif int(user_input)<min_num or int(user_input)>max_num:
        print("The number is out of range")
        print("The number should be between ", min_num, " and ", max_num)
    else:
        print("Wrong number!")
        count_tries += 1
        if int(user_input) < random_number:
            print("The number is higher")
        else:
            print("The number is lower")
