function solution(myString) {
    let answer = []
    const answer_array = myString.split('x')
    for (let i = 0; i < answer_array.length; i++) {
        answer.push(answer_array[i].length)
    }
    return answer
}