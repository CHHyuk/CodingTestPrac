function solution(num_list) {
    let even_sum = 0
    let odd_sum = 0
    for (let i = 0; i < num_list.length; i++) {
        if (i % 2 == 0) {
            even_sum += num_list[i]
        } else {
            odd_sum += num_list[i]
        }
    }

    if (even_sum >= odd_sum) {
        return even_sum
    } else {
        return odd_sum
    }
}