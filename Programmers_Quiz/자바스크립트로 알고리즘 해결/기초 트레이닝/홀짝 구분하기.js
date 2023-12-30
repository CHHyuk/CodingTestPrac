const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = 0

rl.on('line', function(inputted_value) {
    input = inputted_value
}).on('close', function() {
    if (input % 2 == 0) {
        console.log(`${input} is even`)
    } else {
        console.log(`${input} is odd`)
    }
})