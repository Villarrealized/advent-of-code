import Foundation

let gravityAssistIntcode = [
  1, 0, 0, 3,
  1, 1, 2, 3,
  1, 3, 4, 3,
  1, 5, 0, 3,
  2, 1, 10, 19,
  1, 6, 19, 23,
  1, 10, 23, 27,
  2, 27, 13, 31,
  1, 31, 6, 35,
  2, 6, 35, 39,
  1, 39, 5, 43,
  1, 6, 43, 47,
  2, 6, 47, 51,
  1, 51, 5, 55,
  2, 55, 9, 59,
  1, 6, 59, 63,
  1, 9, 63, 67,
  1, 67, 10, 71,
  2, 9, 71, 75,
  1, 6, 75, 79,
  1, 5, 79, 83,
  2, 83, 10, 87,
  1, 87, 5, 91,
  1, 91, 9, 95,
  1, 6, 95, 99,
  2, 99, 10, 103,
  1, 103, 5, 107,
  2, 107, 6, 111,
  1, 111, 5, 115,
  1, 9, 115, 119,
  2, 119, 10, 123,
  1, 6, 123, 127,
  2, 13, 127, 131,
  1, 131, 6, 135,
  1, 135, 10, 139,
  1, 13, 139, 143,
  1, 143, 13, 147,
  1, 5, 147, 151,
  1, 151, 2, 155,
  1, 155, 5, 0,
  99, 2, 0, 14, 0
];

let startTime = CFAbsoluteTimeGetCurrent()

func process(intcode: [Int], noun: Int, verb: Int) -> Int {
  let opcodeLength = 4;
  var code = intcode
  
  code[1] = noun
  code[2] = verb
  
  var pointer = 0
  while(pointer < code.count && code[pointer] != 99) {
    let firstValue = code[code[pointer + 1]]
    let secondValue = code[code[pointer + 2]]
    let position = code[pointer + 3]
    if (code[pointer] == 1) {
      code[position] = firstValue + secondValue
    } else if (code[pointer] == 2) {
      code[position] = firstValue * secondValue
    }
    pointer += opcodeLength;
  }
  
  return code[0]
}

let result = process(intcode: gravityAssistIntcode, noun: 12, verb: 2)
print("Part 1: \(result)")


func nounAndVerb(for output: Int, with intcode: [Int]) -> (Int, Int, Int)? {
  for noun in 0...99 {
    for verb in 0...99 {
      let result = process(intcode: gravityAssistIntcode, noun: noun, verb: verb)
      if (result == output) {
        return (noun, verb, (100 * noun) + verb)
      }
    }
  }
  return nil
}

if let complexResult = nounAndVerb(for: 19690720, with: gravityAssistIntcode) {
  print("Part 2: \(complexResult)")
}

let timeElapsed = CFAbsoluteTimeGetCurrent() - startTime
print("Execution time: \(timeElapsed * 1000)ms")
