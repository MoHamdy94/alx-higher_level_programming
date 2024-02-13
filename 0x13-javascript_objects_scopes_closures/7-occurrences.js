#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Validate inputs
  if (!Array.isArray(list)) {
    throw new Error('Input list must be an array.');
  }

  // Initialize count to 0
  let count = 0;

  // Iterate through the list
  for (const element of list) {
    // Compare elements using strict equality (===)
    if (element === searchElement) {
      count++;
    }
  }

  // Return the count of occurrences
  return count;
};
