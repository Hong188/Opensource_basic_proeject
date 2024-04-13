import random

class 틱택토:
    def __init__(self):
        self.게임판 = [[" " for _ in range(3)] for _ in range(3)]

    def 게임판_출력(self):
        for 행 in self.게임판:
            print(" | ".join(행))
            print("-" * 5)

    def 승자_확인(self):
        for i in range(3):
            if self.게임판[i][0] == self.게임판[i][1] == self.게임판[i][2] != " ":
                return self.게임판[i][0]
            if self.게임판[0][i] == self.게임판[1][i] == self.게임판[2][i] != " ":
                return self.게임판[0][i]
        if self.게임판[0][0] == self.게임판[1][1] == self.게임판[2][2] != " ":
            return self.게임판[0][0]
        if self.게임판[0][2] == self.게임판[1][1] == self.게임판[2][0] != " ":
            return self.게임판[0][2]
        return None

    def 게임판_가득참_확인(self):
        for 행 in self.게임판:
            if " " in 행:
                return False
        return True

    def 플레이어_차례(self, 행, 열):
        if 0 <= 행 < 3 and 0 <= 열 < 3 and self.게임판[행][열] == " ":
            self.게임판[행][열] = "X"
            return True
        else:
            return False

    def 컴퓨터_차례(self):
        while True:
            행 = random.randint(0, 2)
            열 = random.randint(0, 2)
            if self.게임판[행][열] == " ":
                self.게임판[행][열] = "O"
                break

    def 플레이(self):
        print("틱택토 게임을 시작합니다!")
        self.게임판_출력()

        while True:
            # 플레이어 차례
            while True:
                try:
                    행 = int(input("행을 입력하세요 (0, 1, 2): "))
                    열 = int(input("열을 입력하세요 (0, 1, 2): "))
                    if self.플레이어_차례(행, 열):
                        break
                    else:
                        print("잘못된 위치입니다. 다시 시도하세요.")
                except ValueError:
                    print("잘못된 입력입니다. 숫자를 입력하세요.")
            self.게임판_출력()
            if self.승자_확인() == "X":
                print("축하합니다! 당신이 이겼어요!")
                break
            if self.게임판_가득참_확인():
                print("비겼습니다!")
                break

            # 컴퓨터 차례
            print("컴퓨터의 차례입니다:")
            self.컴퓨터_차례()
            self.게임판_출력()
            if self.승자_확인() == "O":
                print("컴퓨터가 이겼어요!")
                break
            if self.게임판_가득참_확인():
                print("비겼습니다!")
                break

if __name__ == "__main__":
    게임 = 틱택토()
    게임.플레이()
