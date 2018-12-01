x = 0
y =1
sum = []

with open('input1') as f:
    content = f.readlines()

while True:
    print("round " + str(y))
    for l in content:
        x += int(l)

        if not x in sum:
            sum.append(x)
            #print("append to list: " + str(x))
        else:
            print("first double: " + str(x))
            exit(0)
    y += 1
