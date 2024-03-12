mark = float(input("Enter your mark"))
if mark <1 or mark >100:
    print("Error: Marks must be between 1 and 100")

level = int(input("What level is the student? 1 or 2?"))

if level == 1:
    if mark <=50:
        print("Fail")
    elif mark >50 and mark <= 60:
        print("Pass")
    elif mark >=60 and mark < 70:
        print("Merit")
    elif mark >=70 and mark <= 100:
        print("Distinction")

if level == 2:
    if mark <=40:
        print("Fail")
    elif mark >40 and mark <= 50:
        print("Pass")
    elif mark >=50 and mark < 65:
        print("Merit")
    elif mark >=65 and mark <= 100:
        print("Distinction")