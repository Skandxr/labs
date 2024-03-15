#class Student: #part1
   # def __init__(self, name, age):
        #self.name = name
        #self.age = age

#student1 = Student("Alice", 20)
#student2 = Student("Bob", 22)

#print(f"The age of {student1.name} is {student1.age} years old.")



class Student: #part2
    def __init__(self, name, age, current_class=None):
        self.name = name
        self.age = age
        self.current_class = current_class
        self.num_tests = 0
        self.total_score = 0

    def add_test_score(self, score):
        self.num_tests += 1
        self.total_score += score

    def calculate_average_score(self):
        if self.num_tests == 0:
            return 0
        return self.total_score / self.num_tests

student = Student("Charlie", 18, "Class A")

# Adding test scores and calculating average
student.add_test_score(85)
student.add_test_score(90)
student.add_test_score(88)

average_score = student.calculate_average_score()
print(f"{student.name}'s average test score is {average_score:.2f}")



