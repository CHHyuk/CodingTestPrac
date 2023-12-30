function solution(start_num, end_num) {
    answer = []

    for (i= start_num; i >= end_num; i--) {
        answer.push(i)
    }

    return answer 
}