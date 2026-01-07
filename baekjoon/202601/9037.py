import sys


input = sys.stdin.readline

class CandyGame:
    def __init__(self, n, candies):
        self.n = n
        self.students = candies

    def make_even(self):
        for i in range(self.n):
            if self.students[i] % 2 != 0:
                self.students[i] += 1

    def all_same(self):
        first_candy = self.students[0]
        for i in range(1, self.n):
            if self.students[i] != first_candy:
                return False
        return True

    def cycle(self):
        give_away = [x // 2 for x in self.students]
        

        for i in range(self.n):
            self.students[i] = give_away[i] + give_away[i-1]
        

        self.make_even()

    def solve(self):
        count = 0

        self.make_even()
        
        while not self.all_same():
            self.cycle()
            count += 1
            
        return count

t = int(input())

for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    
    game = CandyGame(n, candies)
    print(game.solve())