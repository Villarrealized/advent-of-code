package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func readInput() string {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	return strings.TrimRight(string(data), "\n")
}

func parseInput(input string) (output [][]int) {
	for elf := range strings.SplitSeq(input, "\n\n") {
		bag := []int{}
		for food := range strings.SplitSeq(elf, "\n") {
			calories, err := strconv.Atoi(food)
			if err != nil {
				panic(err)
			}
			bag = append(bag, calories)
		}
		output = append(output, bag)
	}
	return
}

func main() {
	input := readInput()
	result := part1(input)
	result2 := part2(input)
	fmt.Printf("part 1: %v\n", result)
	fmt.Printf("part 2: %v\n", result2)
}

func part1(input string) int {
	elves := parseInput(input)

	max_cals := 0

	for _, elf := range elves {
		sum := 0
		for _, calories := range elf {
			sum += calories
		}
		if sum > max_cals {
			max_cals = sum
		}
	}

	return max_cals
}

func part2(input string) int {
	elves := parseInput(input)

	totals := []int{}

	for _, elf := range elves {
		sum := 0
		for _, calories := range elf {
			sum += calories
		}
		totals = append(totals, sum)
	}

	sort.Slice(totals, func(a, b int) bool {
		return totals[b] < totals[a]
	})
	topThree := 0

	for i := range 3 {
		topThree += totals[i]
	}
	return topThree
}
