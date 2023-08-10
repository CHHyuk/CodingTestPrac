def find_receiving_towers(heights):
    stack = []  # 스택을 사용하여 탑의 정보를 저장하는 리스트
    result = [0] * len(heights)  # 결과를 저장할 리스트, 초기값은 0

    for i in range(len(heights)):
        while stack:
            if stack[-1][0] <= heights[i]:  # 스택의 탑 높이가 현재 탑보다 작거나 같으면 레이저 신호 수신 가능
                stack.pop()
            else:
                result[i] = stack[-1][1] + 1  # 수신한 탑의 인덱스를 결과 리스트에 저장
                break
        stack.append((heights[i], i))  # 현재 탑의 높이와 인덱스를 스택에 저장

    return result

# 입력 받기
N = int(input())
heights = list(map(int, input().split()))

# 결과 계산 및 출력
result = find_receiving_towers(heights)
print(' '.join(map(str, result)))
