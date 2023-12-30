function odd_check_function(n) {
    if (n % 2 != 0) {
        return true
    } else {
        return false
    }
}

function solution(a,b) {
    let result = 0
    
    if (odd_check_function(a) && odd_check_function(b)) {
        result = result + (a**2) + (b**2)
    } else if (odd_check_function(a) != odd_check_function(b)) {
        result = result + (2*(a + b))
    } else {
        result = result + (Math.abs(a - b))
    }

    return result
}