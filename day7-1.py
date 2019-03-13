from collections import defaultdict

with open('input7') as f:
    content = f.read().splitlines()

test_long = [
             "Step C must be finished before step A can begin.",
             "Step C must be finished before step F can begin.",
             "Step A must be finished before step B can begin.",
             "Step A must be finished before step D can begin.",
             "Step B must be finished before step E can begin.",
             "Step D must be finished before step E can begin.",
             "Step F must be finished before step E can begin.",
            ]

edges = defaultdict(list)
dots = []
stack = []
for dep in content:
    x = dep[5]
    y = dep[36]
    edges[y].append(x)
    if y not in dots:
        dots.append(y)
    if x not in dots:
        dots.append(x)

print(edges)
print(sorted(dots))
print(len(edges))

x = 0
while True:  # x < 10:
    #print("while")
    for point in sorted(dots):
        #print(" point: " + point)
        if point in edges.keys() and len(edges[point]) > 0:
            continue
        for edge, dep in edges.items():
                #print(edge, dep)
                if point in dep:
                    #print("  remove " + point)
                    edges[edge].remove(point)
                    #print(edges)
                    #if len(dep) == 0:
                    #    print("   empty dep " + point)
                    #    del edges[edge]
        stack.append(point)
        #print(" stack: " + str(stack))
        dots.remove(point)
        #print(" dots" + str(dots))
        break  # start from the beginning

    if len(dots) == 0:
        break
    x += 1

print("".join(stack))
