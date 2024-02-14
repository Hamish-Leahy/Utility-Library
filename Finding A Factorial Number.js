// File: utilityLibrary.js

/**
 * Utility Library
 * Contains various utility functions.
 */

/**
 * Calculate the factorial of a given number.
 * @param {number} n - The input number.
 * @returns {number} - The factorial of the input number.
 */
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// Example usage
const num = 5;
console.log(`Factorial of ${num}: ${factorial(num)}`);

// Export the utility functions if needed in a module system
// module.exports = { factorial };
