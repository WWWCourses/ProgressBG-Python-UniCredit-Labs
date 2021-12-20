# TASK: user enters student name-score pairs. While the user enters empty string for 'user_name', read values and put them into dictinary

students_score = {}


while True:
	user_name = input('enter a name: ')

	if user_name == '':
		break
	user_score = input('enter a score: ')

	students_score[user_name] = user_score;



print(students_score)


best_students_scores = {}
for k,v in students_score.items():
	if(v>4.5):
		best_students_scores[k] = v

