class Student:
    def _init_(self, name, regno, mark1, mark2, mark3):
        self.name = name
        self.regno = regno
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.total = mark1 + mark2 + mark3  # Calculate total marks

    def _str_(self):
        return f"{self.regno}\t{self.name}\t{self.total}"



num_students = int(input("Enter the number of students: "))
students_list = []


for i in range(num_students):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Name: ")
    regno = input("Register Number: ")
    mark1 = int(input("Mark 1: "))
    mark2 = int(input("Mark 2: "))
    mark3 = int(input("Mark 3: "))

    student = Student(name, regno, mark1, mark2, mark3)
 
students_list.sort(key=lambda x: x.total, reverse=True)


print("\nRank\tRegNo\tName\tTotal Marks")
print("-" * 40)
for rank, student in enumerate(students_list, start=1):
    print(f"{rank}\t{student}")
