//package main
//
//import (
//	"bufio"
//	"fmt"
//	"os"
//)
//
//const MAX_SIZE int = 15
//
//var (
//	sc                    = bufio.NewScanner(os.Stdin)
//	wr                    = bufio.NewWriter(os.Stdout)
//	cnt, n                int
//	issued_x              = [MAX_SIZE]bool{}
//	issued_rignt_diagonal = [2*MAX_SIZE - 1]bool{}
//	issued_left_diagonal  = [2*MAX_SIZE - 1]bool{}
//)
//
//func toInt(n *int, buf []byte) {
//	for _, v := range buf {
//		*n = (*n)*10 + int(v-'0')
//	}
//	return
//}
//
//func main() {
//	if sc.Scan() {
//		toInt(&n, sc.Bytes())
//	}
//
//	nqueen(0)
//
//	fmt.Fprintln(wr, cnt)
//	wr.Flush()
//}
//
//func nqueen(y int) {
//	if y == n {
//		cnt++
//		return
//	}
//	for x := 0; x < n; x++ {
//		if !isValid(x, y) {
//			continue
//		}
//		issued_x[x] = true
//		issued_rignt_diagonal[x+y] = true
//		issued_left_diagonal[y-x+n-1] = true
//
//		nqueen(y + 1)
//
//		issued_x[x] = false
//		issued_rignt_diagonal[x+y] = false
//		issued_left_diagonal[y-x+n-1] = false
//	}
//}
//
//func isValid(x int, y int) bool {
//	if issued_x[x] {
//		return false
//	}
//	if issued_rignt_diagonal[x+y] {
//		return false
//	}
//	if issued_left_diagonal[y-x+n-1] {
//		return false
//	}
//	return true
//}
