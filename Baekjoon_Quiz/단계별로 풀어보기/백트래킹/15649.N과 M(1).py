n,m = map(int,input().split())
visited = [False] * (n-1)
answer = []

def visit(depth, n, m):

    if depth == m:
        print(' '.join(map(str, answer)))
    
    for i in range(1, n+1):

        if not visited[i]:
            visited[i] = True
            answer.append(i)
            visit(depth+1,n,m)
            visited[i] = False
            answer.pop()

visit(0, n, m)    

