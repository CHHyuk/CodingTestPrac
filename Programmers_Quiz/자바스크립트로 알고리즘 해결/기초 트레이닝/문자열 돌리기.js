const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function(inputted_value) {
    input = inputted_value.split('')
}).on('close', function() {
    for (let i = 0; i < input.length; i++) {
        console.log(input[i])
    }
})