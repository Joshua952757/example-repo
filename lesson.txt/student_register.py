num_students = int(input("Enter number of students: "))

with open("reg_form.txt", "w") as file:
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        file.write(student_id + "\n--------------------\n")

print("Registration complete. IDs saved in reg_form.txt.")
