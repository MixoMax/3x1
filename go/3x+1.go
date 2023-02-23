package main

import (
	"fmt"
	"time"
)

func main() {
	total_n := 1000000
	max_n := 0
	max_count := 0
	start_time := time.Now().UnixNano()

	for n := 1; n <= total_n; n++ {
		count := 0
		var i int64 = int64(n)
		for i > 1 {
			if i%2 == 0 {
				i = i / 2
			} else {
				i = 3*i + 1
			}
			count++
		}
		if count > max_count {
			max_count = count
			max_n = n
		}
	}

	end_time := time.Now().UnixNano()

	fmt.Printf("%d %d %d ms\n", max_n, max_count, (end_time-start_time)/1000000)
}
