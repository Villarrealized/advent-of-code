/*
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. 
The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

  - It is a six-digit number.
  - The value is within the range given in your puzzle input.
  - Two adjacent digits are the same (like 22 in 122345).
  - Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

  - 111111 meets these criteria (double 11, never decreases).
  - 223450 does not meet these criteria (decreasing pair of digits 50).
  - 123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?
*/

const passwordRange = '125730-579381';
const [low, high] = passwordRange.split('-');

function isAscendingOrEqual(digits) {
  return digits.slice(1)
    .map((number, index) => number >= digits[index])
    .every(bool => bool);
}

function hasAdjacentSet(digits, isolatedPair = false) {
  var unique = [...new Set(digits)]
  if (unique.length === digits.length) return false;
  // find every number's index that appears more than once
  const duplicateIndexes = unique
    .map(uniqueNumber => {
      return digits.flatMap((num, index) => num === uniqueNumber ? index : []);
    })
    .filter(indexes => indexes.length > 1);
  if (!duplicateIndexes) return false;
  
  // Find at least one index that is within 1 index of another to be considered adjacent
  const adjacentSets = duplicateIndexes
    .map(indexArray => indexArray.map((item, index) => item + 1 === indexArray[index + 1])
      .filter(i => i));
  
  // at least one set cannot be part of a larger grouping
  // must be a pair. ex. 4,4,4 is invalid, But 4,4 is fine.
  if (isolatedPair) {
    return adjacentSets.some(set => set.length === 1)
  }

  return adjacentSets.some(set => set.length > 0)
}

function isCandidate(number, isolatedPairRequired = false) {
  const digits = Array.from(number.toString()).map(Number);
  // left to right numbers should stay the same or increase
  if (!isAscendingOrEqual(digits)) return false;
  // Must have two adjacent digits that are equal
  if (hasAdjacentSet(digits, isolatedPairRequired)) return true;
}

const hrstart = process.hrtime();

const candidates = [];
for (let number = low; number <= high; number++) {
  if(isCandidate(number)) {
    candidates.push(number);
  }
}

console.log('Part 1:', candidates.length);

/*
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching 
digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

  - 112233 meets these criteria because the digits never decrease and all 
    repeated digits are exactly two digits long.
  - 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
  - 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
*/

const isolatedCandidates = [];
for (let number = low; number <= high; number++) {
  if(isCandidate(number, true)) {
    isolatedCandidates.push(number);
  }
}

console.log('Part 2:', isolatedCandidates.length);

const hrend = process.hrtime(hrstart);
console.info('Execution time: %dms', hrend[1] / 1000000);