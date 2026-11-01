# Student Performance Analytics Toolkit
def add_student(student_id, name, marks):
    if student_id == "":
        return None, "Student ID cannot be empty!"
    if name == "":
        return None, "Student name cannot be empty!"
    if len(marks) != 3:
        return None, "Enter marks for all three subjects!"
    for mark in marks:
        if mark < 0 or mark > 100:
            return None, "Invalid marks! Enter marks between 0 and 100."
    student = {
        "name": name,
        "marks": marks
    }
    return student, "Record added successfully!"
def calculate_total(marks):
    total = 0
    for mark in marks:
        total += mark
    return total
def calculate_average(marks):
    if len(marks) == 0:
        return 0
    total = calculate_total(marks)
    return total / len(marks)
def get_grade(average):
    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Division"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"
def build_report(student):
    marks = student["marks"]
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)
    return {
        "name": student["name"],
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }
def get_top_students(records):
    return list(filter(
        lambda student: student["average"] >= 75,
        records
    ))
# Function using *args
def calculate_average_args(*marks):
    if len(marks) == 0:
        return 0
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)
# Function using **kwargs
def class_summary_options(**options):
    title = options.get("title", "Class Report")
    passing_mark = options.get("passing_mark", 40)
    print("\n", title)
    print("Passing Mark:", passing_mark)
def show_student(name, grade="Not Calculated"):
    print("Student Name:", name)
    print("Grade:", grade)
def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)
def scope_demo():
    message = "This is a local variable"
    print(message)
def main():
    student_records = {}
    subjects = ("Python", "Maths", "DBMS")
    total_students = int(input("Enter number of students: "))
    # Add student records
    for i in range(total_students):
        print("\nEnter Student", i + 1, "Details")
        student_id = input("Enter Student ID: ")
        if student_id in student_records:
            print("Student ID already exists!")
            continue
        name = input("Enter Student Name: ")
        marks = []
        for subject in subjects:
            mark = int(input("Enter " + subject + " Marks: "))
            marks.append(mark)
        student, message = add_student(student_id, name, marks)
        if student is not None:
            student_records[student_id] = student
        print(message)
    # Calculate student reports
    reports = []
    print("\n===== STUDENT PERFORMANCE REPORT =====")
    for student_id, student in student_records.items():
        report = build_report(student)
        reports.append(report)
        print("\nStudent ID:", student_id)
        print("Name:", report["name"])
        print("Marks:", report["marks"])
        print("Total:", report["total"])
        print("Average:", round(report["average"], 2))
        print("Grade:", report["grade"])
    # Use filter() to find high performers
    high_performers = get_top_students(reports)
    # Use map() with lambda to extract names
    high_performer_names = list(
        map(lambda student: student["name"], high_performers)
    )
    print("\nHigh Performers (Average >= 75):")
    print(high_performer_names)
    # Class average
    class_average = calculate_average_args(
        *map(lambda student: student["average"], reports)
    )
    print("\nClass Average:", round(class_average, 2))
    # Demonstrate *args with individual marks
    marks_average = calculate_average_args(78, 65, 88)
    print("Average of supplied marks:", marks_average)
    class_summary_options(
        title="Student Class Summary",
        passing_mark=40
    )
    # Positional argument example
    show_student("Aman", "Distinction")
    show_student(grade="Pass", name="Riya")
    # Default argument example
    show_student("Rahul")
    # Recursion test with three values
    print("\n===== RECURSION TEST =====")
    print("Sum from 1 to 3:", recursive_sum(3))
    print("Sum from 1 to 5:", recursive_sum(5))
    print("Sum from 1 to 7:", recursive_sum(7))
    print("\n===== SCOPE DEMONSTRATION =====")
    scope_demo()
# Start the program
main()
