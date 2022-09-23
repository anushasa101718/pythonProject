student1 = input("Enter name:")
marks = int(input("Enter marks:"))
if marks >= 75 :
    print(student1,"Distinction",marks)
elif marks >= 65 and marks < 75:
    print(student1, "First class", marks)
elif marks >= 45 and marks < 60:
    print(student1, "second class", marks)
else:
    print(student1, "you are champ", marks)
