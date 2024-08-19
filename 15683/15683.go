package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var (
	// 파일 스캐너 생성
	//file, _ = os.Open("input.txt") // 동일 경로의 input.txt 파일을 엽니다.
	//sc      = bufio.NewScanner(file)
	sc                     = bufio.NewScanner(os.Stdin)
	wr                     = bufio.NewWriter(os.Stdout)
	N, M                   int
	board                  [][]int
	result                 = 999999
	cameras                []Camera
	CAMERA_DIRECTION_COUNT = [6]int{0, 4, 2, 4, 4, 1}
	CAMERA_DIRECTIONS      = [][]int{[]int{}, []int{0}, []int{0, 2}, []int{0, 3}, []int{0, 2, 3}, []int{0, 1, 2, 3}}
)

type Vertex struct {
	row, col int
}

type Camera struct {
	cameraType int
	vertex     Vertex
}

func (camera Camera) getDirectionKind() int {
	return CAMERA_DIRECTION_COUNT[camera.cameraType]
}

func main() {
	input()
	for row := 0; row < N; row++ {
		for col := 0; col < M; col++ {
			if 1 <= board[row][col] && board[row][col] < 6 {
				cameras = append(cameras, Camera{board[row][col], Vertex{row, col}})
			}
		}
	}

	sort.Slice(cameras, func(i, j int) bool {
		return cameras[i].cameraType > cameras[j].cameraType
	})

	var firstIndexNotFour int
	for idx, camera := range cameras {
		if camera.cameraType != 5 {
			firstIndexNotFour = idx
			break
		}

		board = monitor(camera, board, 0)
	}

	simulate(board, firstIndexNotFour)

	fmt.Println(result)

}
func simulate(board [][]int, index int) {
	if index == len(cameras) {
		result = min(result, getUnmonitoredRealm(board))
		return
	}
	for rotate := 0; rotate < cameras[index].getDirectionKind(); rotate++ {
		copiedBoard := deepCopyBoard(board)
		simulate(monitor(cameras[index], copiedBoard, rotate), index+1)
	}
}

func deepCopyBoard(board [][]int) [][]int {
	copied := make([][]int, N)
	for idx := range copied {
		copied[idx] = make([]int, M)
	}

	for r := 0; r < N; r++ {
		for c := 0; c < M; c++ {
			copied[r][c] = board[r][c]
		}
	}

	return copied
}

func getUnmonitoredRealm(board [][]int) int {
	var result int
	for _, row := range board {
		for _, col := range row {
			if col == 0 {
				result++
			}
		}
	}

	return result
}

func monitor(camera Camera, board [][]int, rotate int) [][]int {
	for _, direction := range CAMERA_DIRECTIONS[camera.cameraType] {
		var rotatedDirection = (direction + rotate) % 4
		monitorOneDirection(camera, rotatedDirection, &board)
	}
	return board
}

func monitorOneDirection(camera Camera, direction int, board *[][]int) {
	// direction 0123 , 동서남북
	if direction == 0 {
		for start := camera.vertex.col + 1; start < len((*board)[0]); start++ {
			if (*board)[camera.vertex.row][start] == 6 {
				break
			}
			if (*board)[camera.vertex.row][start] == 0 {
				(*board)[camera.vertex.row][start] = -1
			}
		}
	} else if direction == 2 {
		for start := camera.vertex.col - 1; start >= 0; start-- {
			if (*board)[camera.vertex.row][start] == 6 {
				break
			}
			if (*board)[camera.vertex.row][start] == 0 {
				(*board)[camera.vertex.row][start] = -1
			}
		}
	} else if direction == 1 {
		for start := camera.vertex.row + 1; start < len((*board)); start++ {
			if (*board)[start][camera.vertex.col] == 6 {
				break
			}
			if (*board)[start][camera.vertex.col] == 0 {
				(*board)[start][camera.vertex.col] = -1
			}
		}
	} else if direction == 3 {
		for start := camera.vertex.row - 1; start >= 0; start-- {
			if (*board)[start][camera.vertex.col] == 6 {
				break
			}
			if (*board)[start][camera.vertex.col] == 0 {
				(*board)[start][camera.vertex.col] = -1
			}
		}
	}

}

// IO
func input() {
	//defer file.Close()

	sc.Split(bufio.ScanWords)
	N, M = nextInt(), nextInt()

	board = make([][]int, N)
	for idx, _ := range board {
		board[idx] = make([]int, M)
	}
	for row := 0; row < N; row++ {
		for col := 0; col < M; col++ {
			board[row][col] = nextInt()
		}
	}

}

func nextInt() int {
	sc.Scan()
	input := sc.Text()
	v, _ := strconv.Atoi(input)
	return v
}
