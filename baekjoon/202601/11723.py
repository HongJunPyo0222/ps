import sys

# 1. 입력 속도를 위해 sys.stdin.readline 사용 (필수)
input = sys.stdin.readline

class Set:
    def __init__(self):
        self.sets = set()

    def check(self, x):
        if x in self.sets:
            return 1
        else:
            return 0

    def add(self, x):
        self.sets.add(x)
    
    def remove(self, x):
        # 2. remove 대신 discard 사용 (없어도 에러 안 남)
        self.sets.discard(x)

    def toggle(self, x):
        if x in self.sets:
            self.sets.discard(x) # 여기도 remove 대신 discard가 안전
        else:
            self.sets.add(x)
    
    def all(self):
        # 1~20 채우기
        self.sets = set(range(1, 21))

    def empty(self):
        self.sets.clear()

repeat = int(input())

result = Set()
for _ in range(repeat):
    inputs = input().split()
    cmd = inputs[0]

    if cmd == "all":
        result.all()
    elif cmd == "empty":
        result.empty()
    else:
        # all, empty 외에는 숫자가 반드시 따라옴
        num = int(inputs[1])
        
        if cmd == "add":
            result.add(num)
        elif cmd == "remove":
            result.remove(num)
        elif cmd == "check":
            print(result.check(num))
        elif cmd == "toggle":
            result.toggle(num)