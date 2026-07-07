class Student:
    def __init__(self, name: str, age: int = 13, grade: str = "12th"):
        self._name = ""
        self._age = 13
        self._grade = "12th"

        self.name = name
        self.age = age
        self.grade = grade

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name_val: str) -> None:
        if isinstance(name_val, str) and len(name_val.strip()) >= 3:
            self._name = name_val.strip().title()

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age_int: int) -> None:
        if isinstance(age_int, int) and 11 < age_int < 18:
            self._age = age_int

    @property
    def grade(self) -> str:
        return self._grade

    @grade.setter
    def grade(self, grade_val: str) -> None:
        if isinstance(grade_val, str) and grade_val[:-2].isdigit() and grade_val.endswith("th"):
            grade_number = int(grade_val[:-2])
            if 9 <= grade_number <= 12:
                self._grade = grade_val

    def __str__(self) -> str:
        return f"Student 1: Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def advance(self, years_advanced: int = 1) -> str:
        current_grade = int(self.grade[:-2])
        new_grade = current_grade + years_advanced
        return f"{self.name} has advanced to the {new_grade}th grade"

    def study(self, subject: str) -> str:
        return f"{self.name} is studying {subject}"