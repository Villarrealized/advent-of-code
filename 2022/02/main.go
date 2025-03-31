package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	input := readInput()
	result := part1(input)
	result2 := part2(input)
	fmt.Printf("part 1: %v\n", result)
	fmt.Printf("part 2: %v\n", result2)
}

const (
	ROCK     = 1
	PAPER    = 2
	SCISSORS = 3

	WIN  = 6
	DRAW = 3
	LOSE = 0
)

// opponent: me: score
var scoreCard = map[string]map[string]int{
	"A": {"X": DRAW + ROCK, "Y": WIN + PAPER, "Z": LOSE + SCISSORS},
	"B": {"X": LOSE + ROCK, "Y": DRAW + PAPER, "Z": WIN + SCISSORS},
	"C": {"X": WIN + ROCK, "Y": LOSE + PAPER, "Z": DRAW + SCISSORS},
}

var scoreCard2 = map[string]map[string]int{
	"A": {"X": LOSE + SCISSORS, "Y": DRAW + ROCK, "Z": WIN + PAPER},
	"B": {"X": LOSE + ROCK, "Y": DRAW + PAPER, "Z": WIN + SCISSORS},
	"C": {"X": LOSE + PAPER, "Y": DRAW + SCISSORS, "Z": WIN + ROCK},
}

func part1(input string) int {
	total := 0
	for line := range strings.SplitSeq(input, "\n") {
		game := strings.Split(line, " ")
		total += scoreCard[game[0]][game[1]]
	}
	return total
}

func part2(input string) int {
	total := 0
	for line := range strings.SplitSeq(input, "\n") {
		game := strings.Split(line, " ")
		total += scoreCard2[game[0]][game[1]]
	}
	return total
}

func readInput() string {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	return strings.TrimRight(string(data), "\n")
}
