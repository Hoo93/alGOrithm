//package main
//
//import (
//	"bufio"
//	"fmt"
//	"os"
//	"sort"
//	"strconv"
//	"strings"
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
//func toInt(n *int, buf []byte) {
//	for _, v := range buf {
//		*n = (*n)*10 + int(v-'0')
//	}
//	return
//}
//
//func input() {
//	var input string
//	if sc.Scan() {
//		input = sc.Text()
//	}
//	parts := strings.Split(input, " ")
//	N, _ = strconv.Atoi(parts[0])
//	S, _ = strconv.Atoi(parts[1])
//
//	if sc.Scan() {
//		input = sc.Text()
//	}
//	parts = strings.Split(input, " ")
//
//	for _, part := range parts {
//		num, _ := strconv.Atoi(part)
//		nums = append(nums, num)
//	}
//
//	sort.Ints(nums)
//}
//
//func main() {
//	input()
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
