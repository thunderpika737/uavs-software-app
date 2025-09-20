from PIL import Image
import random

# in from vision/generator/backgrounds and vision/generator/objects
# out to vision/images/train and vision/images/val
# generate labels in vision/labels/train and vision/labels/val

backgrounds = ['dirt.jpg', 'grass.jpg', 'gravel1.png', 'gravel2.jpg']
objects = ['bike.png', 'frisbee.png', 'golfball.png', 'suitcase.png', 'traffic_cone.png', 'disccone.png', 'person.png', 'backpack.png']

def generate_image():
    bg = Image.open('vision/generator/backgrounds/' + random.choice(backgrounds))
    obj = Image.open('vision/generator/objects/' + random.choice(objects)).convert("RGBA")
    resize_factor = random.random() + 0.5
    obj = obj.resize((int(obj.size[0] * resize_factor), int(obj.size[1] * resize_factor)))
    obj = obj.rotate(random.randint(-180, 180), expand=True)

    pos = (random.randint(0, bg.size[0] - obj.size[0]), random.randint(0, bg.size[1] - obj.size[1]))
    bg.paste(obj, pos, obj)

    return {'image': bg, 'pos': pos, 'size': obj.size, 'bg': bg.size}

if __name__ == "__main__":
    for i in range(0, 3000):
        if i%3 == 0:
            out_dir = 'vision/images/val/'
            label_dir = 'vision/labels/val/'
        else:
            out_dir = 'vision/images/train/'
            label_dir = 'vision/labels/train/'

        data = generate_image()
        data['image'].save(out_dir + f'image_{i}.png')

        x_center = (data['pos'][0] + data['size'][0]/2) / data['bg'][0]
        y_center = (data['pos'][1] + data['size'][1]/2) / data['bg'][1]
        width = data['size'][0] / data['bg'][0]
        height = data['size'][1] / data['bg'][1]

        with open(label_dir + f'image_{i}.txt', 'w') as f:
            f.write(f"0 {x_center} {y_center} {width} {height}\n")

        if (i+1) % 100 == 0:
            print(f"Generated {i+1} images")