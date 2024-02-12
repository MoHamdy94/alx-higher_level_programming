#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const number = Number(process.argv[2]);
  for (let i = 0; i < number; i++) {
    console.log('x'.repeat(number));
  }
}
