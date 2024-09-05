def draw_star(num):
    # 전체 패턴의 크기는 (4 * num - 3) x (4 * num - 3)
    size = 4 * num - 3
    # 2차원 배열을 공백으로 초기화
    grid = [[' ' for _ in range(size)] for _ in range(size)]

    # 재귀적으로 패턴을 그리는 함수
    def draw_recursive(x, y, n):
        if n == 1:
            grid[x][y] = '*'
            return
        
        length = 4 * n - 3
        
        # 테두리 그리기
        for i in range(length):
            grid[x][y + i] = '*'  # 상단 테두리
            grid[x + i][y] = '*'  # 좌측 테두리
            grid[x + length - 1][y + i] = '*'  # 하단 테두리
            grid[x + i][y + length - 1] = '*'  # 우측 테두리
        
        # 내부 패턴을 재귀적으로 그리기
        draw_recursive(x + 2, y + 2, n - 1)

    # 초기 위치와 패턴 크기 설정
    draw_recursive(0, 0, num)
    
    # 결과 출력
    for row in grid:
        print(''.join(row))

# 사용자 입력
T = int(input())
draw_star(T)