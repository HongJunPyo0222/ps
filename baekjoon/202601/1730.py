"""
W대학교 미술대학 조소과에서는 지루한 목판화 작업을 하는 학생들을 돕기 위해 판화 기계를 제작하였다.

기계는 로봇 팔이 쥔 조각도를 상하좌우 네 방향으로 움직일 수 있는 구조로서, 조각도 아래에 목판을 놓으면 그 위에 선들을 자동으로 그어주는 기능을 가지고 있다.

목판에는 N2개의 점들이 일정한 간격으로 N행 N열의 격자모양을 이루며 찍혀있다. 처음 로봇의 조각도를 올려놓는 위치는 항상 이 점들 중 맨 왼쪽 맨 위의 꼭짓점이다.

로봇 팔을 움직이는 명령의 순서가 주어졌을 때, 목판 위에 패인 조각도의 혼적을 출력하는 프로그램을 작성하시오.

판화 기계는 작동 도중 로봇 팔이 격자 바깥으로 나가도록 하는 움직임 명령을 만나면, 무시하고 그 다음 명령을 진행한다.

입력
첫째 줄에 목판의 크기 N (2 ≤ N ≤ 10)이 주어진다. 행 열의 점들이 찍혀 있다는 의미이다. 둘째 줄에 로봇팔의 움직임이 한 줄로 공백 없이 입력된다. 위쪽으로 이동은 'U', 아래쪽으로 이동은 'D', 왼쪽으로 이동은 'L', 오른쪽으로 이동은 'R'로 표시된다. 로봇팔의 움직임을 나타내는 이 문자열의 길이는 최대 250이다.

출력
로봇팔이 지나지 않은 점은 '.'으로, 로봇팔이 수직 방향으로만 지난 점은 '|'으로, 로봇팔이 수평 방향으로만 지난 점은 '-'으로, 수직과 수평 방향 모두로 지난 점은 '+'로 표기하도록 한다. 네 문자의 ASCII 코드는 각각 46, 124, 45, 43이다.

예제 입력 1 
5
DRDRRUU

예제 출력 1 
|..|.
++.|.
.+-+.
.....
.....
"""

# class RobotCurve:
#     def __init__(self,n:int):
#         self.map = [['.' for _ in range(n)] for _ in range(n)]
#         self.currnet_x = 0
#         self.currnet_y = 0
    
#     def check_horizen_curved(self,x, y):
#         if self.map[x][y] == "-":
#             return True
#         else :
#             return False
        
#     def check_vertical_curved(self,x, y):
#         if self.map[x][y] == "|":
#             return True
#         else :
#             return False

#     def curve(self,input :str):
#         if input == 'U':
#             if self.check_horizen_curved(self,self.current_x, self.current_y):
#                 self.map[self.currnet_x][self.currnet_y] ='+'
#             else:
#                 self.map[self.current_x][self.currenx] = "|"
#             self.currnet_y += 1

#         if input == 'D':
#             if self.check_horizen_curved(self,self.current_x, self.current_y):
#                 self.map[self.currnet_x][self.currnet_y] ='+'
#             else:
#                 self.map[self.current_x][self.currenx] = "|"
#             self.currnet_y -= 1

#         if input == 'R':
#             if self.check_vertical_curved(self,self.current_x, self.current_y):
#                 self.map[self.currnet_x][self.currnet_y] ='+'
#             else:
#                 self.map[self.current_x][self.currenx] = "-"
#             self.currnet_x += 1

#         if input == 'L':
#             if self.check_vertical_curved(self,self.current_x, self.current_y):
#                 self.map[self.currnet_x][self.currnet_y] ='+'
#             else:
#                 self.map[self.current_x][self.currenx] = "-"
#             self.currnet_x -= 1
        
# n = int(input())
# game = RobotCurve(n)
# strinput = input()
# for index in range(len(strinput)):
#     game.curve(strinput[index])

# print(game.map)

import sys

class RobotCurve:
    def __init__(self, n: int):
        self.n = n
        # map[y][x] 구조 (y: 행/세로, x: 열/가로)
        self.map = [['.' for _ in range(n)] for _ in range(n)]
        self.x = 0  # 현재 가로 위치 (Column)
        self.y = 0  # 현재 세로 위치 (Row)

    # 세로 흔적 남기기 (기존 흔적 유지하면서 합치기)
    def mark_vertical(self, x, y):
        if self.map[y][x] == '.':
            self.map[y][x] = '|'
        elif self.map[y][x] == '-':
            self.map[y][x] = '+'
        # 이미 '|' 이거나 '+' 이면 건들지 않음

    # 가로 흔적 남기기 (기존 흔적 유지하면서 합치기)
    def mark_horizontal(self, x, y):
        if self.map[y][x] == '.':
            self.map[y][x] = '-'
        elif self.map[y][x] == '|':
            self.map[y][x] = '+'
        # 이미 '-' 이거나 '+' 이면 건들지 않음

    def curve(self, command: str):
        # 1. 이동할 예상 좌표 계산
        nx, ny = self.x, self.y
        
        if command == 'U':
            ny -= 1
        elif command == 'D':
            ny += 1
        elif command == 'L':
            nx -= 1
        elif command == 'R':
            nx += 1
            
        # 2. 격자 바깥으로 나가는지 확인 (나가면 무시하고 함수 종료)
        if not (0 <= nx < self.n and 0 <= ny < self.n):
            return

        # 3. 흔적 남기기 (출발점과 도착점 모두 마킹해야 선이 이어짐)
        if command in ['U', 'D']:
            self.mark_vertical(self.x, self.y) # 출발점
            self.mark_vertical(nx, ny)         # 도착점
        elif command in ['L', 'R']:
            self.mark_horizontal(self.x, self.y) # 출발점
            self.mark_horizontal(nx, ny)         # 도착점

        # 4. 실제 좌표 이동
        self.x, self.y = nx, ny

# --- 실행 부분 ---
n = int(input())
# 명령어가 없는 경우(빈 줄) 예외 처리
try:
    strinput = input().strip()
except:
    strinput = ""

game = RobotCurve(n)

for char in strinput:
    game.curve(char)

# 출력 부분: 리스트를 문자열로 변환하여 출력
for row in game.map:
    print("".join(row))