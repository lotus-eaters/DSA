def get_marks():
	marks={}
	num = int(input("Enter number of subjects"))
	for i in range(num):
		subject = input(f"Enter subject {i+1}")
		score = int(input("Enter score of the subject"))
		marks[subject] = score
	return marks

def compute_math(marks):
	total = sum(marks.values())
	average = total/len(marks)
	highest_scoring_subject = max(marks, key=marks.get)
	lowest_scoring_subject = min(marks, key=marks.get)
	print("\n----- Report Card -----")
	print(f"Total Marks: {total}")
	print(f"Average Marks: {average:.2f}")
	print(f"Highest Scoring Subject: {highest_scoring_subject} ({marks[highest_scoring_subject]}")
	print(f"Lowest Scoring Subject: {lowest_scoring_subject} ({marks[lowest_scoring_subject]})")


marks_data = get_marks()
compute_math(marks_data)

