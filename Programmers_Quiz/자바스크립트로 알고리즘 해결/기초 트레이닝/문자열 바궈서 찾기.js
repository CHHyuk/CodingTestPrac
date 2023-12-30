function solution(myString, pat) {
    let changed_string = ''
    for (let i = 0; i < myString.length; i++) {
        if (myString[i] == 'A') {
            changed_string = changed_string + 'B'
        } else {
            changed_string = changed_string + 'A'
        }
    }

    if (changed_string.includes(pat)) {
        return 1
    } else {
        return 0
    }
}