const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let str = ''

rl.question('',function (input) {
    str = input;
    console.log(str);
    rl.close();
})