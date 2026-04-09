
MAX_STUDENTS = 100


def get_menu_choice():
    while True:
        print("\nStudent Menu")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Grade")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice

        print("Invalid choice. Please enter a number from 1 to 6.")


def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def get_student_age():
    while True:
        age_text = input("Enter student age: ").strip()
        if not age_text.isdigit():
            print("Invalid input. Age must be a whole number.")
            continue

        age = int(age_text)
        if 1 <= age <= 120:
            return age

        print("Age must be between 1 and 120.")


def get_student_grade():
    while True:
        grade_text = input("Enter student grade (0-100): ").strip()
        try:
            grade = float(grade_text)
            if 0 <= grade <= 100:
                return grade
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Grade must be a number.")


def find_student_index(student_ids, target_id):
    for index in range(len(student_ids)):
        if student_ids[index].lower() == target_id.lower():
            return index
    return -1


def add_student(student_ids, student_names, student_ages, student_grades):
    if len(student_ids) >= MAX_STUDENTS:
        print("Student list is full.")
        return

    student_id = get_non_empty_text("Enter student ID: ")
    if find_student_index(student_ids, student_id) != -1:
        print("Student ID already exists.")
        return

    name = get_non_empty_text("Enter student name: ")
    age = get_student_age()
    grade = get_student_grade()

    student_ids.append(student_id)
    student_names.append(name)
    student_ages.append(age)
    student_grades.append(grade)

    print("Student added successfully.")


def view_students(student_ids, student_names, student_ages, student_grades):
    if len(student_ids) == 0:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 55)
    print(f"{'ID':<12}{'Name':<20}{'Age':<10}{'Grade':<10}")
    print("-" * 55)

    for index in range(len(student_ids)):
        print(
            f"{student_ids[index]:<12}"
            f"{student_names[index]:<20}"
            f"{student_ages[index]:<10}"
            f"{student_grades[index]:<10.2f}"
        )


def search_student(student_ids, student_names, student_ages, student_grades):
    if len(student_ids) == 0:
        print("No student records found.")
        return

    student_id = get_non_empty_text("Enter student ID to search: ")
    index = find_student_index(student_ids, student_id)

    if index == -1:
        print("Student not found.")
        return

    print("\nStudent Found")
    print(f"ID: {student_ids[index]}")
    print(f"Name: {student_names[index]}")
    print(f"Age: {student_ages[index]}")
    print(f"Grade: {student_grades[index]:.2f}")


def update_student_grade(student_ids, student_names, student_grades):
    if len(student_ids) == 0:
        print("No student records found.")
        return

    student_id = get_non_empty_text("Enter student ID to update: ")
    index = find_student_index(student_ids, student_id)

    if index == -1:
        print("Student not found.")
        return

    print(f"Current grade of {student_names[index]}: {student_grades[index]:.2f}")
    student_grades[index] = get_student_grade()
    print("Student grade updated successfully.")


def delete_student(student_ids, student_names, student_ages, student_grades):
    if len(student_ids) == 0:
        print("No student records found.")
        return

    student_id = get_non_empty_text("Enter student ID to delete: ")
    index = find_student_index(student_ids, student_id)

    if index == -1:
        print("Student not found.")
        return

    del student_ids[index]
    del student_names[index]
    del student_ages[index]
    del student_grades[index]
    print("Student deleted successfully.")


def main():
    student_ids = []
    student_names = []
    student_ages = []
    student_grades = []

    while True:
        choice = get_menu_choice()

        if choice == "1":
            add_student(student_ids, student_names, student_ages, student_grades)
        elif choice == "2":
            view_students(student_ids, student_names, student_ages, student_grades)
        elif choice == "3":
            search_student(student_ids, student_names, student_ages, student_grades)
        elif choice == "4":
            update_student_grade(student_ids, student_names, student_grades)
        elif choice == "5":
            delete_student(student_ids, student_names, student_ages, student_grades)
        else:
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()
