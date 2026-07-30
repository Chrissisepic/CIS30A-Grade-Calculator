# main.py
# Program File for Course Project Part 2

import grade_utils

def save_report_to_file(filename: str, student_name: str, scores: list, average: float, grade: str, feedback: str):
    """Function to implement File Operations & File Output."""
    with open(filename, "w") as file:
        file.write("========================================\n")
        file.write("   GRADE CALCULATOR ACADEMIC REPORT     \n")
        file.write("========================================\n")
        file.write(f"Student Name : {student_name}\n")
        file.write(f"Scores       : {scores}\n")
        file.write(f"Final Average: {average:.2f}%\n")
        file.write(f"Letter Grade : {grade}\n")
        file.write(f"Feedback     : {feedback}\n")
        file.write("========================================\n")
    print(f"\n[File Operation Success]: Academic report exported to '{filename}'!")


def main():
    print("==========================================")
    print("   Welcome to Student Grade Calculator    ")
    print("==========================================\n")

    # Get student information and construct Class Objects
    student_name = input("Enter Student Name: ").strip()
    
    # Objects instantiated from classes
    base_student = grade_utils.Student(student_name)
    honors_student = grade_utils.HonorsStudent(student_name)

    print(base_student.get_greeting())

    # Data containers (Lists & Dictionaries)
    categories = ["Homework", "Quiz", "Exam"]
    scores_list = []
    category_objects = {}

    # Loop (for loop)
    for category in categories:
        while True:
            try:
                raw_input = input(f"Enter score for {category} (0 - 100): ")
                score = float(raw_input)

                # Conditional Statement for validation
                if score < 0 or score > 100:
                    raise ValueError("Score must be between 0 and 100.")
                
                # Store in list & dictionary objects
                scores_list.append(score)
                category_objects[category] = grade_utils.CourseCategory(category, score)
                break  

            except ValueError as e:
                print(f" Invalid Input Error: {e}. Please enter a valid number.")

    # Function calls
    raw_average = grade_utils.calculate_average(scores_list)

    # Ask if student is in Honors program
    is_honors = input("\nIs this student in Honors? (yes/no): ").strip().lower()
    if is_honors in ["yes", "y"]:
        # Sub-class method execution
        final_average = honors_student.apply_bonus(raw_average)
        print(f"\n[Honors Bonus Applied]: +{honors_student.honors_bonus}% added!")
    else:
        final_average = raw_average

    # Function call for letter grade determination
    letter_grade, feedback = grade_utils.determine_letter_grade(final_average)

    # Controlled String Formatting Output
    summary_output = (
        f"\n------------------------------------------\n"
        f"RESULTS SUMMARY FOR {base_student.name.upper()}:\n"
        f"Individual Scores : {[obj.format_summary() for obj in category_objects.values()]}\n"
        f"Final Average     : {final_average:.2f}%\n"
        f"Calculated Grade  : {letter_grade}\n"
        f"Academic Feedback : {feedback}\n"
        f"------------------------------------------"
    )
    print(summary_output)

    # File Output
    save_report_to_file("Grade_Report.txt", student_name, scores_list, final_average, letter_grade, feedback)


if __name__ == "__main__":
    main()
