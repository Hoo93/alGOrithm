package io

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	sc   = bufio.NewScanner(os.Stdin)
	wr   = bufio.NewWriter(os.Stdout)
	size int
	nums []int
)

func input() {
	// input 을 띄어쓰기, \n 단위로 입력받기
	sc.Split(bufio.ScanWords)

	// 배열에 숫자 입력 받기
	nums = make([]int, size)
	for i := 0; i < size; i++ {
		nums[i] = nextInt()
	}

	sort.Ints(nums)
}

// 입력 받은 숫자를 Int 로 형변환
func nextInt() int {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.Atoi(text)
	return v
}

// 입력 받은 숫자를 parseInt(text, base, bitsize) 로 형변환
func nextInt64() int64 {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.ParseInt(text, 10, 64)
	return v
}
