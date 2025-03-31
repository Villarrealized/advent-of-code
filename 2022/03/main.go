package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	input := readInput()
	result := part1(input)
	// result2 := part2(input)
	fmt.Printf("part 1: %v\n", result)
	// fmt.Printf("part 2: %v\n", result2)
}

func part1(input string) int {
	priorities := generatePriorities()
	total := 0

	for rucksack := range strings.SplitSeq(input, "\n") {
		leftHalf := rucksack[:len(rucksack)/2]
		rightHalf := rucksack[len(rucksack)/2:]
		for _, char := range leftHalf {
			if strings.Contains(rightHalf, string(char)) {
				total += priorities[string(char)]
				break
			}
		}

	}
	return total
}

func part2(input string) int {
	priorities := generatePriorities()
	rucksacks := strings.Split(input, "\n")
	total := 0

	for i := 0; i < len(rucksacks); i += 3 {
		set1, set2 := stringToSet(rucksacks[i+1]), stringToSet(rucksacks[i+2])
		for char := range strings.SplitSeq(rucksacks[i], "") {
			if set1[char] && set2[char] {
				total += priorities[char]
				break
			}
		}
	}
	return total
}

func generatePriorities() map[string]int {
	var priorities = map[string]int{}
	for i := range 26 {
		priorities[string(rune('a'+i))] = i + 1
		priorities[string(rune('A'+i))] = i + 27
	}

	return priorities
}

func stringToSet(s string) map[string]bool {
	set := map[string]bool{}
	for char := range strings.SplitSeq(s, "") {
		set[char] = true
	}

	return set
}

func readInput() string {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	return strings.TrimRight(string(data), "\n")
}
