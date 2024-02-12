#!/usr/bin/node
const num = process.argv[2];
let result = 1;
for (let i = 1; i <= num; i++) {
  result *= i;
}
console.log(result);
