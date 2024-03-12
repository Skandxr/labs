mark = float(input("Enter your mark"))

if mark <1 or mark >100:
    print("Error: Marks must be between 1 and 100")
elif mark <=50:
    print("Fail")
elif mark >50 and mark <= 60:
    print("Pass")
elif mark >=60 and mark < 70:
    print("Merit")
elif mark >=70 and mark <= 100:
    print("Distinction")
