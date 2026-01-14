'''
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 
다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭
의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치
의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-
1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.
'''
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    grid = [[0 for _ in range(m)]for _ in range(n)]
    visted = [[0 for _ in range(m)]for _ in range(n)]
    count = 0


    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1


    def in_range(x, y):
        return 0<=x and x <m and 0<=y and y < n

    def dfs_near(x, y):
        dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if in_range(new_x, new_y) and visted[new_y][new_x] == 0 and grid[y][x] == 1:
                visted[new_y][new_x] = 1
                dfs_near(new_x, new_y)
        
    for y in range(n):
        for x in range(m):
            if grid[y][x] == 1 and visted[y][x] == 0:
                visted[y][x] = 1
                dfs_near(x, y)
                count+=1
            else:
                pass

    print(count)
