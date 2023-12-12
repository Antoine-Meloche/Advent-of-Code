package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"strconv"
)

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(content), "\n")

	//////////////////
	//    Part 1    //
	//////////////////

	sum := 0

	for i := 0; i < len(lines); i++ {
		line := lines[i]

		first_num := ""

		for j := 0; j < len(line); j++ {
			char := string(line[j])

			_, err := strconv.Atoi(char)

			if err == nil {
				first_num = char
				break
			}
		}

		last_num := first_num

		for j := len(line) - 1; j > 0; j-- {
			char := string(line[j])

			_, err := strconv.Atoi(char)

			if err == nil {
				last_num = char
				break
			}
		}

		combined_num, err := strconv.Atoi(first_num + last_num)

		if err == nil {
			// fmt.Println(combined_num)
			sum += combined_num
		}
	}

	fmt.Println("Part 1: " + strconv.Itoa(sum))

	//////////////////
	//    Part 1    //
	//////////////////
}
