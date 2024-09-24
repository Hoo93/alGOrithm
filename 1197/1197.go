package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

var (
	//file, _ = os.Open("input.txt") // 동일 경로의 input.txt 파일을 엽니다.
	//sc      = bufio.NewScanner(file)
	sc    = bufio.NewScanner(os.Stdin)
	wr    = bufio.NewWriter(os.Stdout)
	V, E  int
	edges map[int][]Edge
)

type Edge struct {
	value   int
	endNode int
}

type PriorityQueue []*Edge

func (pq PriorityQueue) Len() int {
	return len(pq)
}

// value 가 작은 값이 우선순위가 높음
func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].value < pq[j].value
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x any) {
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
	solve()
}

func solve() {

	// 우선순위 큐 시작
	pq := make(PriorityQueue, 0)
	heap.Init(&pq)

	// 방문 확인
	issued := map[int]bool{}

	// 결과값
	result := 0

	// PRIM Algorithm start at vertex 1
	issued[1] = true
	for _, edge := range edges[1] {
		heap.Push(&pq, &edge)
	}

	for len(issued) < V {
		// 최소값을 가지는 edge 를 찾는다.
		minEdge := heap.Pop(&pq).(*Edge)
		if issued[minEdge.endNode] {
			continue
		}

		issued[minEdge.endNode] = true
		result += minEdge.value
		for _, edge := range edges[minEdge.endNode] {
			if issued[edge.endNode] {
				continue
			}
			heap.Push(&pq, &edge)
		}
	}

	fmt.Fprintln(wr, result)
	wr.Flush()
}

func input() {
	// input 을 띄어쓰기, \n 단위로 입력받기
	sc.Split(bufio.ScanWords)

	// 배열에 숫자 입력 받기
	V, E = nextInt(), nextInt()

	edges = make(map[int][]Edge)
	for i := 1; i <= V; i++ {
		edges[i] = make([]Edge, 0)
	}

	for i := 0; i < E; i++ {
		node1, node2, value := nextInt(), nextInt(), nextInt()
		edges[node1] = append(edges[node1], Edge{value: value, endNode: node2})
		edges[node2] = append(edges[node2], Edge{value: value, endNode: node1})
	}
}

// 입력 받은 숫자를 Int 로 형변환
func nextInt() int {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.Atoi(text)
	return v
}
