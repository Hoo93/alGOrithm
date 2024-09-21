package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

var (
	file, _ = os.Open("input.txt") // 동일 경로의 input.txt 파일을 엽니다.
	sc      = bufio.NewScanner(file)
	//sc   = bufio.NewScanner(os.Stdin)
	wr    = bufio.NewWriter(os.Stdout)
	V, E  int
	edges [][]int
)

type Edge struct {
	value     int
	startNode int
	endNode   int
}

type PriorityQueue []*Edge

func (pq PriorityQueue) Len() int {
	fmt.Println("Len Called")
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	fmt.Println("Less Called")
	fmt.Println(i, j)
	fmt.Println(pq.Len())
	return pq[i].value < pq[j].value
}

func (pq PriorityQueue) Swap(i, j int) {
	fmt.Println("Swap Called")
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x any) {
	fmt.Println("Push Called")
	item := x.(*Edge)
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil // don't stop the GC from reclaiming the item eventually
	*pq = old[0 : n-1]
	return item
}

func main() {
	input()
}

func simulateQueue() {
	pq := make(PriorityQueue, 0)
	heap.Init(&pq)

	heap.Push(&pq, &Edge{value: 3, startNode: 1, endNode: 2})
	heap.Push(&pq, &Edge{value: 1, startNode: 2, endNode: 3})
	heap.Push(&pq, &Edge{value: 3, startNode: 3, endNode: 4})

	for pq.Len() > 0 {
		item := heap.Pop(&pq).(*Edge)
		fmt.Println(item)
	}
}

func input() {
	// input 을 띄어쓰기, \n 단위로 입력받기
	sc.Split(bufio.ScanWords)

	// 배열에 숫자 입력 받기
	V, E = nextInt(), nextInt()
	//board = make([][]int, N)
	//for i := 0; i < N; i++ {
	//	board[i] = make([]int, M)
	//	for j := 0; j < M; j++ {
	//		board[i][j] = nextInt()
	//	}
	//}

}

// 입력 받은 숫자를 Int 로 형변환
func nextInt() int {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.Atoi(text)
	return v
}
