sentences = ["macbook pro", "macbook air", "macbook", "galaxy book", "galaxy s22", "galaxy s24", "iphone 12 mini", "iphone 12 pro", "iphone 12", "iphone 12 pro max"]


def searchString(input, candidates, case_match_enable=False):
	score_table = []
	candidates_count = len(candidates)
	for i in range(candidates_count):
		score_table.append(0)
	for i in range(len(input)):
		for j in range(len(candidates)):
			comp_candiate=""
			comp_input=""
			if case_match_enable:
				comp_input=input[i]
				comp_candidate=candidates[j]
			else:
				comp_input=input.lower()[i]
				comp_candidate=candidates[j].lower()
			for k in range(len(comp_candidate)):
				if comp_input == comp_candidate[k]:
					score_table[j] += 4
					continue
				elif comp_candidate.find(comp_input):
					score_table[j] +=2
				elif case_match_enable and comp_candidate.lower().find(comp_input.lower()):
					score_table[j] +=1
	
	maxs = []
	max_point = 0
	for i in range(candidates_count):
		if score_table[i] > max_point:
			max_point = score_table[i]
			maxs = [candidates[i]]
		elif score_table[i] == max_point:
			maxs.append(candidates[i])
	
	return maxs

try:
	search = input("geegle search engine beta: ")
	print(searchString(search, sentences, True))
except:
	print("something fucked")

print("exit...")
