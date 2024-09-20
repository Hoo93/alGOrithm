package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	//file, _ = os.Open("input.txt") // 동일 경로의 input.txt 파일을 엽니다.
	//sc      = bufio.NewScanner(file)
	sc      = bufio.NewScanner(os.Stdin)
	wr      = bufio.NewWriter(os.Stdout)
	board   [][]int
	visited [][]int
	N, M    int
	deltaY  = [4]int{0, 0, -1, 1}
	deltaX  = [4]int{-1, 1, 0, 0}
)

func main() {
	input()

	dfs(0, 0)

	fmt.Fprintln(wr, visited[0][0])
	wr.Flush()
}

func dfs(y int, x int) int {
	if visited[y][x] > -1 {
		return visited[y][x]
	}
	if y == N-1 && x == M-1 {
		return 1
	}

	visited[y][x] = 0

	for i := 0; i < 4; i++ {
		ny, nx := y+deltaY[i], x+deltaX[i]

		if ny < 0 || ny >= N || nx < 0 || nx >= M {
			continue
		}
		if board[ny][nx] >= board[y][x] {
			continue
		}

		visited[y][x] += dfs(ny, nx)
	}

	return visited[y][x]
}

func input() {
	// input 을 띄어쓰기, \n 단위로 입력받기
	sc.Split(bufio.ScanWords)

	// 배열에 숫자 입력 받기
	N, M = nextInt(), nextInt()
	board = make([][]int, N)
	visited = make([][]int, N)
	for i := 0; i < N; i++ {
		board[i] = make([]int, M)
		visited[i] = make([]int, M)
		for j := 0; j < M; j++ {
			board[i][j] = nextInt()
			visited[i][j] = -1
		}
	}

}

// 입력 받은 숫자를 Int 로 형변환
func nextInt() int {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.Atoi(text)
	return v
}
