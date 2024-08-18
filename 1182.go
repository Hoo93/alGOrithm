//package main
//
//import (
//	"bufio"
//	"fmt"
//	"os"
//	"sort"
//	"strconv"
//)
//
//var (
//	sc     = bufio.NewScanner(os.Stdin)
//	wr     = bufio.NewWriter(os.Stdout)
//	N, S   int
//	nums   []int
//	result int
//)
//
//func input() {
//	sc.Split(bufio.ScanWords)
//	N, S = nextInt(), nextInt()
//
//	nums = make([]int, N)
//	for i := 0; i < N; i++ {
//		nums[i] = nextInt()
//	}
//
//	sort.Ints(nums)
//}
//
//func main() {
//	input()
//	defer wr.Flush()
//
//	backTracking(0, 0)
//
//	if S == 0 {
//		result -= 1
//	}
//	fmt.Fprintln(wr, result)
//	wr.Flush()
//}
//
//func backTracking(x int, total int) {
//	if x == N && total == S {
//		result += 1
//		return
//	}
//	if x >= N {
//		return
//	}
//	if total > S && nums[x] > 0 {
//		return
//	}
//
//	backTracking(x+1, total)
//	backTracking(x+1, total+nums[x])
//}
//
//func nextInt() int {
//	sc.Scan()
//	text := sc.Text()
//	v, _ := strconv.Atoi(text)
//	return v
//}
//
//func nextInt64() int64 {
//	sc.Scan()
//	text := sc.Text()
//	v, _ := strconv.ParseInt(text, 10, 64)
//	return v
//}
