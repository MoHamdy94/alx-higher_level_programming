#!/usr/bin/node

exports.esrever = function (list) {
    // Validate input
    if (!Array.isArray(list)) {
      throw new Error('Input must be an array.');
    }
  
    // Create an empty result array
    const reversedList = [];
  
    // Iterate through the original list in reverse order
    for (let i = list.length - 1; i >= 0; i--) {
      // Push each element of the original list in reverse order to the new array
      reversedList.push(list[i]);
    }
  
    // Return the reversed list
    return reversedList;
  };
  