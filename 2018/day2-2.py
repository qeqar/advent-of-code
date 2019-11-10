with open('input2') as f:
    content = f.readlines()


for inv in content:
    for inv2 in content:
        pos = [i for i in range(len(inv)) if inv[i] != inv2[i]]
        if len(pos) == 1:
            s = inv[:pos[0]] + inv[(pos[0]+1):]
            print(s)
            exit(0)
