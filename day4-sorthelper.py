with open('input4') as f:
    content = f.readlines()

content.sort(key=lambda x: ' '.join(x.split(' ')[:2]))

with open('sorted_input4', 'w') as w:
    for line in sorted(content):
        w.write(line)
