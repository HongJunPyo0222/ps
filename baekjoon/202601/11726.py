"""
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
9
예제 출력 2 
55
"""

import math
"""
2
0 1

9
0   1   2   3   4
1   8   21  10  5 -> 55

9 c 1 = 1

8c 1

5 c 4

5
1
"""

n = int(input())
result = 0
for longNum in range(0, n//2 + 1):
    result += math.comb(n - longNum,longNum)
    # print("long num: ", longNum, math.comb(n - longNum,longNum))

print(result %10007)

