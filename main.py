#Author : Nicole Giron nqg5259@psu.edu
grade = 0
def gradePoint(course):
  if course == "A":
    grade = 4.0
    return grade
  elif course == "A-":
    grade = 3.67
    return grade
  elif course == "B+":
    grade = 3.33
    return grade
  elif course == "B":
    grade = 3.0
    return grade
  elif course == "B-":
    grade = 2.67
    return grade
  elif course == "C+":
    grade = 2.33
    return grade
  elif course == "C":
    grade = 2.0
    return grade
  elif course == "D":
    grade = 1.0
    return grade
  else :
    grade = 0.0
    return grade

course1 = input("Enter your course 1 letter grade: ")
course1Credit = float(input("Enter your course 1 credit: "))
print("Grade point for course 1 is: " + str(gradePoint(course1)))


course2 = input("Enter your course 2 letter grade: ")
course2Credit = float(input("Enter your course 2 credit: "))
print("Grade point for course 2 is: " + str(gradePoint(course2)))

course3 = input("Enter your course 3 letter grade: ")
course3Credit = float(input("Enter your course 3 credit: "))
print("Grade point for course 3 is: " + str(gradePoint(course3)))

GPA = (gradePoint(course1) * course1Credit + gradePoint(course2) * course2Credit + gradePoint(course3) * course3Credit) / (course1Credit + course2Credit + course3Credit) 

print("Your GPA is: " + str(GPA))