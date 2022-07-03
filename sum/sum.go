package sum

type integer interface {
	int | int16 | int32 | int64
}

type unsigned interface {
	uint | uint16 | uint32 | uint64
}

type floating interface {
	float32 | float64
}

type number interface {
	integer | unsigned | floating
}

func Sum[T number](args ...T) T {
	var result T
	for _, v := range args {
		result += v
	}
	return result
}
