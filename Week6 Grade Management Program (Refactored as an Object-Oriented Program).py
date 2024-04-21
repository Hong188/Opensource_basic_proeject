class 학생:
    def __init__(self, 학생_아이디, 이름, 영어_점수, C_점수, 파이썬_점수):
        self.학생_아이디 = 학생_아이디
        self.이름 = 이름
        self.영어_점수 = 영어_점수
        self.C_점수 = C_점수
        self.파이썬_점수 = 파이썬_점수
        self.총_점수 = self.영어_점수 + self.C_점수 + self.파이썬_점수
        self.평균_점수 = self.총_점수 / 3
        self.등급 = self.등급_계산()

    def 등급_계산(self):
        if self.평균_점수 >= 90:
            return 'A'
        elif self.평균_점수 >= 80:
            return 'B'
        elif self.평균_점수 >= 70:
            return 'C'
        elif self.평균_점수 >= 60:
            return 'D'
        else:
            return 'F'


class 학생_관리자:
    def __init__(self):
        self.학생들 = []

    def 학생_입력(self):
        학생_아이디 = input("학생 ID: ")
        이름 = input("이름: ")
        영어_점수 = int(input("영어 점수: "))
        C_점수 = int(input("C 점수: "))
        파이썬_점수 = int(input("파이썬 점수: "))
        self.학생들.append(학생(학생_아이디, 이름, 영어_점수, C_점수, 파이썬_점수))
        print("학생이 성공적으로 추가되었습니다.\n")

    def 학생_삭제(self):
        학생_아이디 = input("삭제할 학생 ID 입력: ")
        for 학생 in self.학생들:
            if 학생.학생_아이디 == 학생_아이디:
                self.학생들.remove(학생)
                print("학생이 성공적으로 삭제되었습니다.")
                return
        print("학생을 찾을 수 없습니다.")

    def 학생_검색(self):
        검색_입력 = input("검색할 ID 또는 이름을 입력하세요: ")
        찾음 = False
        for 학생 in self.학생들:
            if 검색_입력 in [학생.학생_아이디, 학생.이름]:
                print(f"ID: {학생.학생_아이디}, 이름: {학생.이름}, 영어: {학생.영어_점수}, "
                      f"C: {학생.C_점수}, 파이썬: {학생.파이썬_점수}, "
                      f"총점: {학생.총_점수}, 평균: {학생.평균_점수}, 등급: {학생.등급}")
                찾음 = True
        if not 찾음:
            print("학생을 찾을 수 없습니다.")

    def 학생_정렬(self):
        self.학생들.sort(key=lambda x: x.총_점수, reverse=True)
        print("학생들이 성공적으로 정렬되었습니다.")

    def 학생_출력(self):
        if not self.학생들:
            print("출력할 학생이 없습니다.")
            return
        for 학생 in self.학생들:
            print(f"ID: {학생.학생_아이디}, 이름: {학생.이름}, 총점: {학생.총_점수}, "
                  f"평균: {학생.평균_점수}, 등급: {학생.등급}")

    def 평균_80초과_학생_수_계산(self):
        평균_80초과_학생_수 = sum(1 for 학생 in self.학생들 if 학생.평균_점수 > 80)
        print(f"평균이 80점을 넘는 학생 수: {평균_80초과_학생_수}")

    def 메인_메뉴(self):
        while True:
            print("\n1. 추가")
            print("2. 삭제")
            print("3. 검색")
            print("4. 정렬")
            print("5. 출력")
            print("6. 평균 80점 초과 학생 수")
            print("7. 종료")
            선택 = input("원하는 작업을 선택하세요: ")

            if 선택 == '1':
                self.학생_입력()
            elif 선택 == '2':
                self.학생_삭제()
            elif 선택 == '3':
                self.학생_검색()
            elif 선택 == '4':
                self.학생_정렬()
            elif 선택 == '5':
                self.학생_출력()
            elif 선택 == '6':
                self.평균_80초과_학생_수_계산()
            elif 선택 == '7':
                print("프로그램을 종료합니다...")
                break
            else:
                print("잘못된 선택입니다. 다시 시도해주세요.")


if __name__ == "__main__":
    관리자 = 학생_관리자()
    관리자.메인_메뉴()