import random
import time

# 플레이어, 몬스터 클래스


def ment1(a):
    time.sleep(1)
    return a


def ment2(b):
    time.sleep(2)
    return b


class Character:

    def __init__(self, name, hp, mp, power, magic):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.magic = magic

    # 플레이어 몬스터 일반공격
    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        ment2(print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다."))
        if other.hp == 0:
            ment2(print(f"{other.name}이가 쓰러졌습니다."))

    # 플레이어의 마법공격
    def magic_attack(self, other):
        self.mp = max(self.mp - 50, 0)
        if self.mp == 0:
            ment2(print(f"{self.name}의 MP가 부족해 마법공격을 쓸 수 없습니다."))
            return

        damage = random.randint(self.magic - 20, self.magic + 20)
        other.hp = max(other.hp - damage, 0)
        ment2(print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다."))
        if other.hp == 0:
            ment2(print(f"{other.name}이가 쓰러졌습니다."))

    # 플레이어와 몬스터의 상태 출력
    def show_status(self, other):
        ment2(print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp} | MP {self.mp}/{self.max_mp}"))
        ment2(print(f"{other.name}의 상태: HP {other.hp}/{other.max_hp}"))


# 인스턴스(객체) = 클래스
P = Character(ment2(input("플레이어의 이름을 입력하세요 : ")), 1000, 200, 10, 10)
M = Character("세히몬", 100, 0, 10, 0)

# 게임 스타트!

ment2(print("여기는 평화로운 스파르타 내배캠 게더타운."))
print(
    ment2("""
° :.　 . • ○ ° ★　 .　 *　.
★ ° . .　　　　.　☾ °☆　 . * ● ¸ .
    ∩ │◥███◣ ╱◥███◣
    ╱◥◣ ◥████◣▓∩▓│∩ ║
    │╱◥█◣║∩∩∩ ║◥█▓ ▓█◣
    ││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║
            """))

print(
    ment2("""
            ° :.　 . • ○ ° ★　 .　 *　.
        ★ ° . .　　　　.　☾ °☆　 . * ● ¸ .
                    오늘도 코드 헤는 밤...
            """))


ment2(print(f"앗! 플레이어 {P.name}의 앞에 야생의 세히몬이 나타났다!"))

# 게임의 턴을 위한 while문
while P.hp or M.hp > 0:
    ment2(P.show_status(M))
    ment2(print(f"플레이어 {P.name}의 선공!\n1.일반공격, 2.마법공격(mp -50)\n번호를 선택하세요."))
    choice = input()
    if choice == '1':
        P.attack(M)
    elif choice == '2':
        P.magic_attack(M)
        if P.mp == 0:
            continue
    else:
        ment2(print("잘못 입력하셨습니다."))

    if P.hp == 0:
        ment2(print(f"플레이어 {P.name}의 체력이 0 이 되었다.\n 세히몬의 승리!"))
        break
    elif M.hp == 0:
        ment2(print(f"세히몬의 체력이 0 이 되었다. 플레이어 {P.name}의 승리!"))
        break

    ment2(print(f"세히몬이 떽떽거리기!! 를 시전하였습니다."))
    M.attack(P)
