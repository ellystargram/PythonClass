import datetime
import random





def stringSuggestionV2(search, candidates, caseSensitive=True):
	possibility = [0].copy() * len(candidates)
	for i in range(len(candidates)):
		for j in range(len(search)):
			if len(candidates[i]) <= j:
				break
			if not caseSensitive:
				searchAlphabetLowerfy = search[j].lower()
				candidateAlphabetLowerfy = candidates[i][j].lower()
				if searchAlphabetLowerfy == candidateAlphabetLowerfy:
					possibility[i] += 2
				elif candidateAlphabetLowerfy.__contains__(searchAlphabetLowerfy):
					possibility[i] += 1
			else:
				if search[j] == candidates[i][j]:
					possibility[i] += 4
				elif candidates[i].__contains__(search[j]):
					possibility[i] += 2
				elif search[j].lower() == candidates[i][j].lower():
					possibility[i] += 2
				elif candidates[i].__contains__(search[j].lower()):
					possibility[i] += 1

	maxPossibility = 0
	maxPossibilityCount = 0
	maxPossibilityList = []

	for i in range(len(possibility)):
		if possibility[i] > maxPossibility:
			maxPossibility = possibility[i]
			maxPossibilityCount = 1
			maxPossibilityList = [candidates[i]]
		elif possibility[i] == maxPossibility:
			maxPossibilityCount += 1
			maxPossibilityList.append(candidates[i])

	if maxPossibilityCount > 1:
		return maxPossibilityList
	else:
		maxPossibilityIndex = possibility.index(maxPossibility)

	return candidates[maxPossibilityIndex]


def stringSuggestionV3(search, candidates, caseSensitive=True, wildcardChar='*'):
	possibility = [0].copy() * len(candidates)
	maxCandidateLength = 0
	for i in range(len(candidates)):
		if len(candidates[i]) > maxCandidateLength:
			maxCandidateLength = len(candidates[i])

	for i in range(len(candidates)):
		import math
		if len(candidates[i]) < len(search):
			possibility[i] += maxCandidateLength - (len(candidates[i] - len(search)))

	for i in range(len(candidates)):
		for j in range(len(search)):
			if search[j] == wildcardChar:
				possibility[i] += 1
				continue
			if len(candidates[i]) <= j:
				break
			if not caseSensitive:
				searchAlphabetLowerfy = search[j].lower()
				candidateAlphabetLowerfy = candidates[i][j].lower()
				if searchAlphabetLowerfy == candidateAlphabetLowerfy:
					possibility[i] += 2
				elif candidateAlphabetLowerfy.__contains__(searchAlphabetLowerfy):
					possibility[i] += 1
			else:
				if search[j] == candidates[i][j]:
					possibility[i] += 4
				elif candidates[i].__contains__(search[j]):
					possibility[i] += 2
				elif search[j].lower() == candidates[i][j].lower():
					possibility[i] += 2
				elif candidates[i].__contains__(search[j].lower()):
					possibility[i] += 1

	maxPossibility = 0
	maxPossibilityCount = 0
	maxPossibilityList = []

	for i in range(len(possibility)):
		if possibility[i] > maxPossibility:
			maxPossibility = possibility[i]
			maxPossibilityCount = 1
			maxPossibilityList = [candidates[i]]
		elif possibility[i] == maxPossibility:
			maxPossibilityCount += 1
			maxPossibilityList.append(candidates[i])

	if maxPossibilityCount > 1:
		return maxPossibilityList
	else:
		maxPossibilityIndex = possibility.index(maxPossibility)

	return candidates[maxPossibilityIndex]


def quantomize(origin):
	dateSecond = datetime.datetime.now().second * 1000000 + datetime.datetime.now().microsecond

	destination = ""
	temp = str(dateSecond)
	for i in range(len(temp)):
		destination += chr(ord(temp[i]) + i)
	destination += "!@"
	random.seed(dateSecond)

	for i in range(len(origin)):
		quantomizeKeyMin = random.randint(0, 50)
		quantomizeKeyMax = random.randint(50, 100)
		destination += chr(ord(origin[i]) + random.randint(quantomizeKeyMin, quantomizeKeyMax))
	return destination


def dequantomize(origin):
	if origin.find("!@") == -1:
		return "잘못된 입력입니다."
	temp = origin.split("!@")[0]
	origin = origin.split("!@")[1]
	destination = ""
	dateSecond = ""

	for i in range(len(temp)):
		dateSecond += chr(ord(temp[i]) - i)

	random.seed(int(dateSecond))

	for i in range(len(origin)):
		quantomizeKeyMin = random.randint(0, 50)
		quantomizeKeyMax = random.randint(50, 100)
		destination += chr(ord(origin[i]) - random.randint(quantomizeKeyMin, quantomizeKeyMax))

	return destination


def keyedQuantomize(origin, key):
	keySave = key
	destination = ""
	for i in range(len(origin)):
		destination += chr(ord(origin[i]) + key % 10)
		key = key // 10
		if key == 0:
			key = keySave
	return destination


def keyedDequantomize(origin, key):
	keySave = key
	destination = ""
	for i in range(len(origin)):
		destination += chr(ord(origin[i]) - key % 10)
		key = key // 10
		if key == 0:
			key = keySave
	return destination


def combinedQuantomize(origin, key, itteration):
	temp = keyedQuantomize(origin, key)
	temp = quantomize(list(temp))
	for i in range(itteration - 1):
		temp = keyedQuantomize(temp, key)
		temp = quantomize(list(temp))
	return temp


def combinedDequantomize(origin, key, itteration):
	temp = dequantomize(origin)
	temp = keyedDequantomize(temp, key)
	for i in range(itteration - 1):
		temp = dequantomize(temp)
		temp = keyedDequantomize(temp, key)
	return temp
