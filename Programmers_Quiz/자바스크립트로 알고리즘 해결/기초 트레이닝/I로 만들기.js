const alp = ['a','b','c','d','e','f','g','h','i','j','k']

function solution(myString) {
    answer = ''
    for (let i = 0; i < myString.length; i++) {
        if (alp.includes(myString[i])) {
            answer = answer + 'l'
        } else {
            answer = answer + myString[i]
        }
    }
    return answer
}