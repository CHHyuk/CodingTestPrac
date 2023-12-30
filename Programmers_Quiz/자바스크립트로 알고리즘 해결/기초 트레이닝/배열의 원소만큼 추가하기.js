function solution(arr) {
    answer = []
    
    for (let i = 0; i < arr.length; i++) {
        for (let j = arr[i]; j > 0; j--) {
            answer.push(arr[i])
        }
    }

    return answer
}