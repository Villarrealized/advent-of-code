package main

import "testing"

var example = `1000
2000
3000

4000

5000
6000

7000
8000
9000

10000`

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
			want:  24000,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if have := part1(tt.input); have != tt.want {
				t.Errorf("wrong output\nhave: %v, \nwant: %v", have, tt.want)
			}
		})
	}
}
