package hello

import "testing"

func TestHelloWorld(t *testing.T) {
	want := "Hello, world!"
	if got := HelloWorld(); want != got {
		t.Fatalf("No hello unu...")
	}
}
