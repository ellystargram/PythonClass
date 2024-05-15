import toolkit


candidate = ["rock", "scissor", "paper"]
cheat = False
antiCheat = False
while True:
	cheat = False
	antiCheat = False
	userSelection = input("원하는걸 영어로 입력하시오: ").strip().lower()
	if userSelection.startswith("sudo"):
		cheat = True
		userSelection = userSelection[4:].strip()
	elif userSelection.startswith("dosu"):
		antiCheat = True
		userSelection = userSelection[4:].strip()
	if len(userSelection) == 0:
		print("입력이 없어서 랜덤으로 선택되어 들어갑니다.")
		userSelection = toolkit.random.choice(candidate)

	userSelection = userSelection.lower()
	userSelection = toolkit.stringSuggestion(userSelection, candidate)
	if userSelection is None:
		print("잘못된 입력입니다.")
	else:
		break

if cheat:
	comSelection = candidate[(candidate.index(userSelection) + 1) % 3]
elif antiCheat:
	comSelection = candidate[(candidate.index(userSelection) + 2) % 3]
else:
	comSelection = toolkit.random.choice(candidate)

print("당신은", userSelection, "를 선택했고, 컴퓨터는", comSelection, "를 선택했습니다.")

userIndex = candidate.index(userSelection)
comIndex = candidate.index(comSelection)

if userIndex == comIndex:
	print("비겼습니다.")
elif (userIndex + 1) % 3 == comIndex:
	print("당신이 이겼습니다.")
else:
	print("당신이 졌습니다.")
