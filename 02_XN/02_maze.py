
from collections import deque

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [
    lambda x, y: (x-1, y), #上
    lambda x, y: (x, y+1), #右
    lambda x, y: (x+1, y), #下
    lambda x, y: (x, y-1), #左
]

def solve_maze(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    maze[x1][y1] = 2
    while len(stack) > 0:  # 当栈不空时循环
        cur_node = stack[-1]
        if cur_node == (x2, y2): # 如果到终点了
            print(stack)
            return True
        for d in dirs:
            next_node = d(*cur_node)
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = 2  # 2表示已经走过的点
                break
        else:
            stack.pop()
    else:
        print("无路")
        return False


def solve_maze_queue(x1, y1, x2, y2):
    q = deque()
    q.append((x1, y1, -1))
    maze[x1][y1] = 2
    traceback = []
    while len(q) > 0:   # 队不空时循环
        cur_node = q.popleft()
        traceback.append(cur_node)
        if cur_node[:-1] == (x2, y2):
            path = []
            i = len(traceback)-1
            while i >= 0:
                path.append(traceback[i][0:2])
                i = traceback[i][2]
            path.reverse()
            print(path)
            # for i, v in enumerate(traceback):
            #     print(i, v)
            return
        for d in dirs:
            next_x, next_y = d(cur_node[0], cur_node[1])
            if maze[next_x][next_y] == 0:
                q.append((next_x, next_y, len(traceback)-1))
                maze[next_x][next_y] = 2
    else:
        print('无路')
        return False


solve_maze_queue(1,1,8,8)