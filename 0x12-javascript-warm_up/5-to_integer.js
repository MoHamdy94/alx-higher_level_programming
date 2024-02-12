#!/usr/bin/node
const number = Number(process.argv);

// Check if conversion is successful and a finite number
if (Number.isFinite(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
