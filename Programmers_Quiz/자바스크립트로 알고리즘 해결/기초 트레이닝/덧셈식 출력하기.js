const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function(inputted_value) {
    input = inputted_value.split(' ')
}).on('close', function() {
    console.log(`${Number(input[0])} + ${Number(input[1])} = ${Number(input[0]) + Number(input[1])}`)
})