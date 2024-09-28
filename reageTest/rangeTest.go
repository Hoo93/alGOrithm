package main

import "fmt"

type Edge struct {
	value   int
	endNode int
}

func main() {
	edges := []Edge{{value: 3, endNode: 2}, {value: 6, endNode: 4}, {value: 9, endNode: 5}}

	// pq := []*Edge{}
	pq := make([]*Edge, 0)

	for index, edge := range edges {
		fmt.Println("------------------------------")
		fmt.Printf("%v, %v, %p \n", index, edge, &edge)
		pq = append(pq, &edge)
		fmt.Println("------------------------------")
		fmt.Printf("%v, %v, %p \n", index, edge, &edges[index])
		for i := 0; i < len(pq); i++ {
			fmt.Print(pq[i], " ")
		}
		fmt.Println()
	}

}
