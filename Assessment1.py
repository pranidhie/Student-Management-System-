# Constants for grade thresholds
HD_THRESHOLD = 85
D_THRESHOLD = 75
C_THRESHOLD = 65
P_THRESHOLD = 50

# Initialize an empty list to store student records as dictionaries
students = []

# Function to categorise the mark into a grade
def categorise_grade(mark):
    """Returns a grade string based on numeric mark."""
    if mark >= HD_THRESHOLD:
        return "HD (High Distinction)"
    elif mark >= D_THRESHOLD:
        return "D (Distinction)"
    elif mark >= C_THRESHOLD:
        return "C (Credit)"
    elif mark >= P_THRESHOLD:
        return "P (Pass)"
    else:
        return "F (Fail)"

# Function to add a student record
def add_student():
    """Adds a new student by prompting for name and mark."""
    name = input("Enter student name: ")
    mark_input = input("Enter student mark (0-100): ")
    if mark_input.isnumeric():
        mark = int(mark_input)
        if 0 <= mark <= 100:
            grade = categorise_grade(mark)
            students.append({"name": name, "mark": mark, "grade": grade})
            print(f"Student {name} added successfully with grade {grade}.")
        else:
            print("Mark must be between 0 and 100.")
    else:
        print("Invalid input. Please enter a valid number.")

# Function to remove a student by name
def remove_student():
    """Removes a student record by name."""
    name = input("Enter student name to remove: ")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(f"Student {name} removed successfully.")
            return
    print("Student not found.")

# Function to update student details
def update_student():
    """Updates the name and/or mark of a student."""
    name = input("Enter student name to update: ")
    for student in students:
        if student["name"].lower() == name.lower():
            new_name = input("Enter new name (or press Enter to keep current): ")
            new_mark_input = input("Enter new mark (or press Enter to keep current): ")
            if new_mark_input:
                if new_mark_input.isnumeric():
                    new_mark = int(new_mark_input)
                    if 0 <= new_mark <= 100:
                        student["mark"] = new_mark
                        student["grade"] = categorise_grade(new_mark)
                    else:
                        print("Mark must be between 0 and 100.")
                        return
                else:
                    print("Invalid mark.")
                    return
            if new_name:
                student["name"] = new_name
            print("Student record updated successfully.")
            return
    print("Student not found.")

# Function to display all student records
def view_students():
    """Displays all student records."""
    if not students:
        print("No student records available.")
        return
    print("\nStudent List:")
    for student in students:
        print(f"Name: {student['name']}, Mark: {student['mark']}, Grade: {student['grade']}")

# Main loop to show the menu and call relevant functions
while True:
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Remove Student")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        remove_student()
    elif choice == "5" or choice == "":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")