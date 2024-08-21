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
	sc                 = bufio.NewScanner(os.Stdin)
	wr                 = bufio.NewWriter(os.Stdout)
	board              [][]int
	N, M, stickerCount int
	stickers           [][][]int
)

func main() {
	input()

	for _, sticker := range stickers {
		findPossible(sticker)
	}

	fmt.Fprintln(wr, calculateAttachedSurface())
	wr.Flush()
}

func calculateAttachedSurface() int {
	result := 0
	for r := 0; r < N; r++ {
		for c := 0; c < M; c++ {
			result += board[r][c]
		}
	}
	return result
}

func rotateSticker(sticker [][]int) [][]int {
	stickerWidth := len(sticker[0])
	stickerHeight := len(sticker)

	// 회전된 스티커의 배열 크기를 설정
	rotated := make([][]int, stickerWidth)
	for r := 0; r < stickerWidth; r++ {
		rotated[r] = make([]int, stickerHeight)
	}

	// 90도 회전
	for r := 0; r < stickerHeight; r++ {
		for c := 0; c < stickerWidth; c++ {
			rotated[c][stickerHeight-1-r] = sticker[r][c]
		}
	}
	return rotated
}

func findPossible(sticker [][]int) {
	isAttached := false
	isAttached = attachSticker(sticker)
	if isAttached {
		return
	}
	var rotatedSticker = sticker
	for rotateCount := 0; rotateCount < 3; rotateCount++ {
		rotatedSticker = rotateSticker(rotatedSticker)
		isAttached = attachSticker(rotatedSticker)
		if isAttached {
			return
		}
	}
}

func attachSticker(sticker [][]int) bool {
	stickerWidth := len(sticker[0])
	stickerHeight := len(sticker)

	for y := 0; y < N-stickerHeight+1; y++ {
		for x := 0; x < M-stickerWidth+1; x++ {
			if !canAfford(sticker, y, x) {
				continue
			}
			for r := 0; r < stickerHeight; r++ {
				for c := 0; c < stickerWidth; c++ {
					if sticker[r][c] == 0 {
						continue
					}
					board[y+r][x+c] = 1
				}
			}
			return true
		}
	}

	return false
}

func canAfford(sticker [][]int, start_y, start_x int) bool {
	stickerWidth := len(sticker[0])
	stickerHeight := len(sticker)

	if start_x+stickerWidth > M {
		return false
	}

	if start_y+stickerHeight > N {
		return false
	}

	for y := 0; y < stickerHeight; y++ {
		for x := 0; x < stickerWidth; x++ {
			if sticker[y][x] == 1 && board[start_y+y][start_x+x] == 1 {
				return false
			}
		}
	}
	return true
}
func findStartY(sticker [][]int) int {
	for r := 0; r < len(sticker); r++ {
		if sticker[r][0] == 1 {
			return r
		}
	}
	panic("sticker must stick to left")
}

func input() {
	// input 을 띄어쓰기, \n 단위로 입력받기
	sc.Split(bufio.ScanWords)

	// 배열에 숫자 입력 받기
	N, M, stickerCount = nextInt(), nextInt(), nextInt()

	// setup board
	board = make([][]int, N)
	for i := 0; i < N; i++ {
		board[i] = make([]int, M)
		for j := 0; j < M; j++ {
			board[i][j] = 0
		}
	}

	// setup stickers
	stickers = make([][][]int, stickerCount)
	for i := 0; i < stickerCount; i++ {
		row, col := nextInt(), nextInt()
		sticker := make([][]int, row)
		for r := 0; r < row; r++ {
			sticker[r] = make([]int, col)
			for c := 0; c < col; c++ {
				sticker[r][c] = nextInt()
			}
		}
		stickers[i] = sticker
	}
}

func printSticker(sticker [][]int) {
	for _, row := range sticker {
		fmt.Println(row)
	}
	fmt.Println()
}

func printBoard() {
	for _, row := range board {
		fmt.Println(row)
	}
	fmt.Println()
}

// 입력 받은 숫자를 Int 로 형변환
func nextInt() int {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.Atoi(text)
	return v
}
