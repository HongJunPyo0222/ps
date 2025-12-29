"""
1003 피포나치 함수 실버3
"""


repeat = int(input())

numOfTotal = 0
def fibonacci(n):
    global numOfTotal
    a, b = 0, 1
    for _ in range(n):
        a, b = b , a + b
        numOfTotal +=1
    return a
        

for i in range(repeat):
    numOfTotal = 0
    inputNum = int(input())
    b = fibonacci(inputNum)
    print(numOfTotal, b)

    #print(fibonacci(inputNum))

