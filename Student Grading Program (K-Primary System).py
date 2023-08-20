student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#  Don't change the code above 

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.
for name in student_scores:
  score = student_scores[name]
  if score <= 70:
    student_grades[name] = "Fail"
  elif score >= 71 and score <= 80:
    student_grades[name] = "Acceptable"
  elif score >= 81 and score <= 90:
    student_grades[name] = "Exceeds Expectations"
  else:
    student_grades[name] = "Outstanding"

# #  Don't change the code below 
  print(f"{name}: {student_grades[name]}\n")
