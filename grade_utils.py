
class Student:
    """Base Class representing a student."""
    
    def __init__(self, name: str):
        # Attribute: Object variable
        self.name = name

    # Method 1 in Base Class
    def get_greeting(self) -> str:
        """Returns a formatted welcome string."""
        return f"Student Record Initialized for: {self.name}"


class CourseCategory:
    """Class representing a coursework category (e.g., Homework, Exams)."""
    
    def __init__(self, category_name: str, score: float):
        self.category_name = category_name
        self.score = score

    # Method 1 in CourseCategory Class
    def format_summary(self) -> str:
        """Returns a string description of the score."""
        return f"{self.category_name}: {self.score:.2f}%"


class HonorsStudent(Student):
    """Sub-class inheriting from Student (Demonstrates OOP Inheritance)."""
    
    def __init__(self, name: str, honors_bonus: float = 2.0):
        # Call parent constructor
        super().__init__(name)
        self.honors_bonus = honors_bonus

    # Method in Sub-class
    def apply_bonus(self, calculated_avg: float) -> float:
        """Adds a small honors bonus to the final average score."""
        adjusted = calculated_avg + self.honors_bonus
        return min(adjusted, 100.0)  # Cap at 100%


def calculate_average(scores_list: list) -> float:
    """Function 1: Takes a list of numerical scores and computes the average."""
    if not scores_list:
        return 0.0
    total = sum(scores_list)
    return total / len(scores_list)


def determine_letter_grade(average: float) -> tuple:
    """
    Function 2: Takes average score and returns letter grade and feedback using conditional statements.
    Returns tuple: (letter_grade, feedback)
    """
    # Conditional branching (if / elif / else)
    if average >= 90.0:
        return ("A", "Outstanding performance! Keep up the great work.")
    elif average >= 80.0:
        return ("B", "Good job! You have a solid grasp of the material.")
    elif average >= 70.0:
        return ("C", "Satisfactory. Consider reviewing key topics.")
    elif average >= 60.0:
        return ("D", "Warning: You are near passing limit. Seek tutoring.")
    else:
        return ("F", "Alert: Failing grade. Contact your instructor.")
