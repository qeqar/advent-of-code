with open('input2') as f:
    content = f.readlines()

two_inv = 0
three_inv = 0

for inv in content:
    #print(inv)
    letters = {}
    for char in inv:
        #print(char)
        if char in letters:
            #print(char + " is in already in inv")
            letters[char] += 1
            #print(letters)
        else:
            letters[char] = 1
    #print(letters)
    two = 0
    two_found = False
    three = 0
    three_found = False
    for letter in letters:
        if letters[letter] == 2 and not two_found:
            two = 1
            two_found = True
        if letters[letter] == 3 and not three_found:
            three = 1
            three_found = True
        if two_found and three_found:
            break
    two_inv += two
    three_inv += three

print(three_inv * two_inv)

