const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function(inputted_value) {
    input = inputted_value.split(' ');
}).on('close', function() {
    const str = input[0];
    const repeatCount = Number(input[1]);

    let result = '';
    for (let i = 0; i < repeatCount; i++) {
        result += str;
    }

    console.log(result)
})