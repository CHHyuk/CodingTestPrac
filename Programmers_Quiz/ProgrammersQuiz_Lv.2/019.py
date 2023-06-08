# 괄호 회전하기 

def solution(s):
    answer = 0
    temp = list(s)

    for _ in range(len(s)): # s의 길이 횟수만큼 진행해야 하므로

        stack = [] # 스택 리스트 생성
        for i in range(len(temp)): # temp 길이만큼 진행해야 하므로
            if len(stack) > 0: # 스택 리스트에 뭔가 요소가 있다면
                if stack[-1] == '[' and temp[i] == ']': # 대괄호가 있고 temp[i] 가 대괄호 닫힘이라면
                    stack.pop() # 스택 리스트의 요소 빼줌
                elif stack[-1] == '{' and temp[i] == '}': # 마찬가지
                    stack.pop()
                elif stack[-1] == '(' and temp[i] == ')':
                    stack.pop()
                else:
                    stack.append(temp[i]) # 만약 일치하는 항목이 없다면 그 요소도 스택 리스트에 담아둠
            else:
                stack.append(temp[i]) # 스택 리스트에 아무것도 없다면 temp[i]를 스택리스트에 넣어줌1
        if len(stack) == 0: # 최종적으로 스택의 길이가 0이라면 모두 매치되는 상황이므로
            answer += 1 # answer를 +1 해준다
        temp.append(temp.pop(0)) # temp의 첫번째 값을 pop해서 끝에 붙여줌
    
    return answer

            
                

solution("}]()[{")
