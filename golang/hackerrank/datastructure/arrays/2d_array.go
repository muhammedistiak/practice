/*
Solution to https://www.hackerrank.com/challenges/2d-array
*/

package main

import (
	"fmt"
)

func main() {
	var a [6][6]int

	for i := 0; i < 6; i++ {
		for j := 0; j < 6; j++ {
			fmt.Scanf("%d", &a[i][j])
		}
	}

	largestSum := -100

	for i := 0; i <= 3; i++ {
		for j := 0; j <= 3; j++ {
			sum := a[i][j] + a[i][j+1] + a[i][j+2]
			sum += a[i+1][j+1]
			sum += a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
			if sum > largestSum {
				largestSum = sum
			}
		}
	}

	fmt.Printf("%d\n", largestSum)
}
