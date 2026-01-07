import sys

input = sys.stdin.readline

numOfMember = int(input())
members = []

for _ in range(numOfMember):
    age, name = input().split()
    members.append([int(age), name])


members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])