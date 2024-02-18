from faker import Faker
import random


fake = Faker()
print(fake.name())

students = []
first_names = []

for _ in range(10):
    student = {
        "name": fake.name(),
        "age": random.randint(18, 25),
        "major": random.choice(["Computer Science", "Mathematics", "Physics"]),
        "gpa": round(random.uniform(2.0, 4.0), 2),
        "is_international": random.choice([True, False])
    }
    students.append(student)

for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    first_names.append(first_name)
    last_name = full_name.split()[1]
    print(first_name, last_name)
    print("Age:", student["age"])

def checkForDuplicates():
    duplicates = []
    duplicate = False
    for firstNameString in first_names:
        count = 0
        for firstName in first_names:
            if firstName == firstNameString:
                count +=1
        if count > 1:
                duplicate = True
                duplicates.append(firstNameString)
        print(f"Count for {firstNameString}: {count}" )
    if duplicate:
         print(f"There is a name that appears more than once: {set(duplicates)}")
        
checkForDuplicates()