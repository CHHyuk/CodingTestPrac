function solution(a, b) {
    const a_plus_b = String(a) + String(b)
    const b_plus_a = String(b) + String(a)

    if (Number(a_plus_b) > Number(b_plus_a)) {
        return Number(a_plus_b)
    } else {
        return Number(b_plus_a)
    }
}