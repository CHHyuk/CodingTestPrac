function solution(num_list) {
    const product = num_list.reduce((accumulator, currentValue) => accumulator * currentValue, 1);
    const sum = num_list.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    const squaredSum = sum ** 2;

    if (product < squaredSum) {
        return 1;
    } else {
        return 0;
    }
}
