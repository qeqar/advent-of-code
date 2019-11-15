package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

func main(){
	input := "bgvyzdsv"
	number := 0
	for true {
		key := input + strconv.Itoa(number)
		hasher :=md5.New()
		hasher.Write([]byte(key))
		md5sum := hex.EncodeToString(hasher.Sum(nil))
		fmt.Printf("key: %s Number: %d, SUM: %s\n", key, number, md5sum)
		if strings.HasPrefix(md5sum, "000000") {
			break
		}
		number++
	}
	fmt.Printf("\nkey: %s%d", input, number )
}
