#!/usr/bin/node
function factorial (num) {
  let result = 1;
  for (let i = 1; i <= num; i++) {
    result *= i;
  }
  console.log(result);
}
factorial(process.argv[2]);
