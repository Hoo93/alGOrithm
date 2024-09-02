package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	//file, _ = os.Open("input.txt") // 동일 경로의 input.txt 파일을 엽니다.
	//sc      = bufio.NewScanner(file)
	sc   = bufio.NewScanner(os.Stdin)
	wr   = bufio.NewWriter(os.Stdout)
	a    []int
	b    []int
	aidx int = 0
	bidx int = 0
	n, m int
)

func input() {
	// input 을 띄어쓰기, \n 단위로 입력받기
	sc.Split(bufio.ScanWords)

	n, m = nextInt(), nextInt()

	// 배열에 숫자 입력 받기
	a = make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = nextInt()
	}

	b = make([]int, m)
	for i := 0; i < m; i++ {
		b[i] = nextInt()
	}
}

// 입력 받은 숫자를 Int 로 형변환
func nextInt() int {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.Atoi(text)
	return v
}

func main() {
	input()

	for aidx+bidx < n+m {
		if aidx == n {
			wr.WriteString(strconv.Itoa(b[bidx]) + " ")
			bidx++
		} else if bidx == m {
			wr.WriteString(strconv.Itoa(a[aidx]) + " ")
			aidx++
		} else if a[aidx] < b[bidx] {
			wr.WriteString(strconv.Itoa(a[aidx]) + " ")
			aidx++
		} else {
			wr.WriteString(strconv.Itoa(b[bidx]) + " ")
			bidx++
		}
	}

	wr.Flush()
}
