package sum

import (
	"math/rand"
	"testing"
	"time"
)

const N = 100

func TestSum(t *testing.T) {
	rand.Seed(time.Now().UnixNano())
	var values []int
	for i := 0; i < N; i++ {
		values = append(values, rand.Int()%N)
	}

	for i := 0; i < N; i++ {
		var toAdd []int
		for j := 0; j < rand.Int()%N; j++ {
			toAdd = append(toAdd, values[rand.Int()%N])
		}

		var want int
		for _, v := range toAdd {
			want += v
		}
		if got := Sum(toAdd...); want != got {
			t.Fatalf("Sum test failed for input: %v", toAdd)
		}
	}
}
