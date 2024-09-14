package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	//file, _ = os.Open("../input.txt") // 동일 경로의 input.txt 파일을 엽니다.
	//sc      = bufio.NewScanner(file)
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)
)

type Pair struct {
	index int
	value int
}

func main() {
	// input 을 띄어쓰기, \n 단위로 입력받기
	sc.Split(bufio.ScanWords)

	// 배열에 숫자 입력 받기
	N, L := nextInt(), nextInt()
	numList := make([]int, N)
	for i := 0; i < N; i++ {
		numList[i] = nextInt()
	}

	d := make([]int, N)
	dq := make([]Pair, 0, L)

	for idx := 0; idx < N; idx++ {
		// 입력 하는 값보다 큰 값은 최소 값에서 제외되야 하므로 pop
		for len(dq) > 0 && dq[len(dq)-1].value > numList[idx] {
			dq = dq[:len(dq)-1]
		}

		if len(dq) > 0 && idx-dq[0].index >= L {
			dq = dq[1:]
		}

		dq = append(dq, Pair{index: idx, value: numList[idx]})

		d[idx] = dq[0].value
	}

	for _, value := range d {
		fmt.Fprintf(wr, "%d ", value)
	}
	wr.Flush()
}

// 입력 받은 숫자를 Int 로 형변환
func nextInt() int {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.Atoi(text)
	return v
}
