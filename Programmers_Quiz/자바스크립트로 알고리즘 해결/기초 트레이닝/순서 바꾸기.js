function solution(num_list, n) {
    let sliced_list = num_list.slice(n,num_list.length)
    let temp_list = num_list.slice(0,n)

    return sliced_list.concat(temp_list)
}