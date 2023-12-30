function solution(num_list) {
    
    let even_sum = ''
    let odd_sum = ''
    
    for (let i = 0; i < num_list.length; i++) {
        if (num_list[i] % 2 == 0) {
            even_sum = even_sum + String(num_list[i])
        } else {
            odd_sum = odd_sum + String(num_list[i])
        }
    }

    return Number(even_sum) + Number(odd_sum)
}