/*
--- Day 1: The Tyranny of the Rocket Equation ---
Santa has become stranded at the edge of the Solar System while delivering presents to other planets! 
To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to
save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a
module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate 
the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
*/

const moduleMasses = [132897, 131436, 107839, 98498, 141198, 147530, 65491, 142162, 89575, 95090, 147097, 129782,
  144858, 68745, 102201, 103225, 113363, 111744, 91402, 72832, 122801, 121257, 52343, 73228, 92718, 147235, 88278,
  86305, 75761, 63778, 60566, 125207, 65341, 72035, 117227, 101003, 91830, 121549, 116387, 62337, 124495, 76900,
  149440, 94380, 72932, 74131, 147816, 137870, 135540, 99187, 78513, 81784, 77323, 122089, 126365, 148263, 71299,
  56483, 100098, 118856, 101395, 106244, 129590, 104179, 76867, 57756, 83790, 80722, 133943, 78243, 92963, 69222,
  117193, 63871, 111459, 107930, 116514, 124433, 84165, 144701, 144033, 99114, 52861, 86496, 134584, 126356, 149743,
  70192, 142814, 73271, 111543, 60035, 146067, 100679, 116636, 104316, 84510, 59851, 101893, 55611];

const hrstart = process.hrtime();

// To find the fuel required to launch a module
// we must divide its mass by 3, round down, and subtract 2
// then we must add up all the results and return a single value
const fuelRequirement = moduleMasses
  .map(mass => Math.floor(mass / 3) - 2)
  .reduce((accumulator, current) => accumulator + current);

console.log('Part 1:', fuelRequirement);

/*
--- Part Two ---
During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence.
Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that
fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be
treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass
and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the
input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0,
which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2).
216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel.
So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the
mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)
*/

/// Used commented function for submission, refactored to calculateFuel function below later

// const completeFuelRequirement = moduleMasses
//   .map((mass) => {
//     let cumulativeFuel = 0;
//     const calculateFuel = (fuel) => {
//       const fuelRequired = Math.floor(fuel / 3) - 2;
//       if (fuelRequired > 0) {
//         cumulativeFuel += fuelRequired;
//         return calculateFuel(fuelRequired);
//       }
//       return cumulativeFuel;
//     }
//     return calculateFuel(mass);
//   })
//   .reduce((accumulator, mass) => accumulator + mass);

function calculateFuel(mass) {
  const fuel = Math.floor(mass / 3) - 2;
  return fuel > 0 ? fuel + calculateFuel(fuel) : 0;
}

const completeFuelRequirement = moduleMasses
  .map(calculateFuel)
  .reduce((accumulator, mass) => accumulator + mass);

console.log('Part 2:', completeFuelRequirement);

const hrend = process.hrtime(hrstart);
console.info('Execution time: %dms', hrend[1] / 1000000);
