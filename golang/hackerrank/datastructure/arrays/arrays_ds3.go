/*
Solution to https://www.hackerrank.com/challenges/arrays-ds
*/

package main

import (
	"fmt"
)

func reverseOrder(a [1002]int, n, i int) {
	if i == n-1 {
		fmt.Printf("%d", a[i])
		return
	}
	reverseOrder(a, n, i+1)
	fmt.Printf(" %d", a[i])
}

func main() {
	var n int
	var a [1002]int // using array

	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &a[i])
	}

	// use a simple recursion
	reverseOrder(a, n, 0)

	fmt.Printf("\n")
}
