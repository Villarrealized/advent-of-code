package main

import "testing"

var example = `vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw`

type Test struct {
	name  string
	input string
	want  int
}

func TestPart1(t *testing.T) {
	tests := []Test{
		{
			name:  "example",
			input: example,
			want:  157,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if have := part1(tt.input); have != tt.want {
				t.Errorf("wrong output\nhave: %v \nwant: %v", have, tt.want)
			}
		})
	}
}

func TestPart2(t *testing.T) {
	tests := []Test{
		{
			name:  "example",
			input: example,
			want:  70,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if have := part2(tt.input); have != tt.want {
				t.Errorf("wrong output\nhave: %v \nwant: %v", have, tt.want)
			}
		})
	}
}
