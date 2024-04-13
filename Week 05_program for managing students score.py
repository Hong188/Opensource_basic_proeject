class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = english_score + c_score + python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average_score >= 90:
            return 'A'
        elif self.average_score >= 80:
            return 'B'
        elif self.average_score >= 70:
            return 'C'
        elif self.average_score >= 60:
            return 'D'
        else:
            return 'F'

class ScoreManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def search_student(self, identifier):
        for student in self.students:
            if student.student_id == identifier or student.name == identifier:
                return student
        return None

    def sort_students_by_total_score(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)

    def count_students_above_80(self):
        count = sum(1 for student in self.students if student.total_score >= 80)
        return count

    def display_students(self):
        for student in self.students:
            print(f"학번: {student.student_id}, 이름: {student.name}, 총점: {student.total_score}, 평균: {student.average_score}, 학점: {student.grade}")

def input_student():
    student_id = input("학번을 입력하세요: ")
    name = input("이름을 입력하세요: ")
    english_score = int(input("영어 점수를 입력하세요: "))
    c_score = int(input("C언어 점수를 입력하세요: "))
    python_score = int(input("파이썬 점수를 입력하세요: "))
    return Student(student_id, name, english_score, c_score, python_score)

def main():
    score_manager = ScoreManager()

    
    print("5명의 학생 정보를 입력하세요.")
    for _ in range(5):
        student = input_student()
        score_manager.add_student(student)

    score_manager.sort_students_by_total_score()

    print("성적 순으로 학생 정보를 출력합니다.")
    score_manager.display_students()

    print("80점 이상을 받은 학생 수:", score_manager.count_students_above_80())

if __name__ == "__main__":
    main()