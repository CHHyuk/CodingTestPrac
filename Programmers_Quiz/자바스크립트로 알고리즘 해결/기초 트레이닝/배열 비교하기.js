function sumOfArray(array) {
    return array.reduce((sum, current) => sum + current, 0);
}

function solution(arr1, arr2) {
    if (arr1.length == arr2.length) {
        if(sumOfArray(arr1) > sumOfArray(arr2)) {
            return 1
        } else if (sumOfArray(arr1) < sumOfArray(arr2)) {
            return -1
        } else {
            return 0
        }
    } else if (arr1.length > arr2.length) {
        return 1
    } else {
        return -1
    }
}