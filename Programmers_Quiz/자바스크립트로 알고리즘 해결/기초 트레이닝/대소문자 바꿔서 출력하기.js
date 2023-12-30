const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

function isUpperCase(str) {
    return str === str.toUpperCase();
}

rl.on('line',function(inputted_value) {
    input = inputted_value.split('')
}).on('close',function() {
    for (let i = 0; i < input.length; i++ ) {
        if (isUpperCase(input[i])) {
            input[i] = input[i].toLowerCase()
        } else {
            input[i] = input[i].toUpperCase()
        }
    }

    const combined_input = input.join('');
    console.log(combined_input)
})