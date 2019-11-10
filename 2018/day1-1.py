x = 0

with open('input1') as f:
    content = f.readlines()

for l in content:
    x += int(l)

print(x)
