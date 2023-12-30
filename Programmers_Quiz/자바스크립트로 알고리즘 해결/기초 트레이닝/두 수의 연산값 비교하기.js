function solution(a, b) {
    let attached_number = Number(String(a) + String(b))
    let calculated_number = 2 * a * b

    if (attached_number > calculated_number) {
        return attached_number
    } else {
        return calculated_number
    }
}