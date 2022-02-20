package sum

func Sum(args ...int) int {
	var result int
	for _, v := range args {
		result += v
	}
	return result
}
