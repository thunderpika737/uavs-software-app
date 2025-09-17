for i in range(0, 1801):
    if i%3 == 0:
        label_dir = 'vision/labels/val/'
    else:
        label_dir = 'vision/labels/train/'

    newline = ''
    with open(label_dir + f'image_{i}.txt', 'r') as f:
        lines = f.read().strip().split(' ')
        x, y = float(lines[1]), float(lines[2])
        w, h = float(lines[3]), float(lines[4])
        x += w / 2
        y += h / 2
        newline = f"1 {x} {y} {w} {h}"
    with open(label_dir + f'image_{i}.txt', 'w') as f:
        f.write(newline)