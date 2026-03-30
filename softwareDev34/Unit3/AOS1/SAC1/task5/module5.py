# Input: Year level (7 or 9), Mathematics marks, English marks, Science marks (for Year 9 only)
# Process: Validate inputs, create student object, calculate weighted average
# Output: Display year level and weighted average

class Student:
    """Base class for all students"""
    
    def __init__(self, math, english, year_level):
        self.intMathematics = math
        self.intEnglish = english
        self.intYearLevel = year_level
    
    def calculate_weighted_average(self):
        pass
    
    def display_result(self):
        # Process: Calculate weighted average
        # Output: Display year level and weighted average
        avg = self.calculate_weighted_average()
        print(f"\n")
        print(f"Student is enrolled in Year {self.intYearLevel} and the weighted average is {avg:.2f}")


class Year7Student(Student):
    """Year 7 student - weighted average based on Math and English"""
    
    def __init__(self, math, english):
        super().__init__(math, english, 7)
    
    def calculate_weighted_average(self):
        # Process: (math + english) / 2
        return (self.intMathematics + self.intEnglish) / 2


class Year9Student(Student):
    """Year 9 student - weighted average based on Math, English, and Science"""
    
    def __init__(self, math, english, science):
        super().__init__(math, english, 9)
        self.intScience = science
    
    def calculate_weighted_average(self):
        # Process: (math + english + science) / 3
        return (self.intMathematics + self.intEnglish + self.intScience) / 3


def get_math_grade():
    # Input: Mathematics marks from user
    # Process: Validate not empty, is integer, between 0-100
    # Output: Return valid math grade
    math_input = input("Enter the Mathematics marks: ")
    
    if math_input == "":
        print("Score can't be empty")
        return get_math_grade()
    elif math_input.isdigit() == False:
        print("Score should be a whole number")
        return get_math_grade()
    else:
        math = int(math_input)
        if math < 0 or math > 100:
            print("Score should be between 0 and 100 inclusive")
            return get_math_grade()
        else:
            return math


def get_english_grade():
    # Input: English marks from user
    # Process: Validate between 0-100
    # Output: Return valid english grade
    english_input = input("Enter the English marks: ")
    english = int(english_input)
    
    if english < 0 or english > 100:
        print("Score should be between 0 and 100 inclusive")
        return get_english_grade()
    else:
        return english


def get_science_grade():
    # Input: Science marks from user
    # Process: Validate between 0-100
    # Output: Return valid science grade
    science_input = input("Enter the Science marks: ")
    science = int(science_input)
    
    if science < 0 or science > 100:
        print("Score should be between 0 and 100 inclusive")
        return get_science_grade()
    else:
        return science


# Input: Get year level from user
intYearLevel = input("Enter the year level (7 or 9): ")

# Process: Create appropriate student object based on year level
if intYearLevel == "7":
    math = get_math_grade()
    english = get_english_grade()
    student = Year7Student(math, english)
    student.display_result()
elif intYearLevel == "9":
    math = get_math_grade()
    english = get_english_grade()
    science = get_science_grade()
    student = Year9Student(math, english, science)
    student.display_result()