/*
Solution to https://www.hackerrank.com/challenges/arrays-ds
*/

package main

import (
	"fmt"
)

func main() {
	var n int
	var a []int // using slice

	fmt.Scanf("%d", &n)
	a = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &a[i])
	}

	// simplest way is just to print in reverse order
	for i := n - 1; i > 0; i-- {
		fmt.Printf("%d ", a[i])
	}
	fmt.Printf("%d\n", a[0])
}
