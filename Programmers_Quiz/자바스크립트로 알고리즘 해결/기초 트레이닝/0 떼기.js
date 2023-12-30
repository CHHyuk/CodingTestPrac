function solution(n_str) {
    let zero_cutting = 0
    for (let i = 0; i < n_str.length; i++) {
        if (n_str[i] != '0') {
            zero_cutting = i
            break
        }
    }
    return n_str.slice(zero_cutting,n_str.length)
}