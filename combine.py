import sys, os, math
from PIL import Image
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
print (os.getcwd())
imagelist = os.listdir("images")
os.chdir("images")
imagelist.sort()
print(imagelist)
#image dimentions
sample = Image.open(imagelist[0])
width, height = sample.size
if int(math.sqrt(width)) > len(imagelist):
    row_limit = len(imagelist)
else:
    row_limit = int(math.sqrt(width))
x_offset = 0
y_offset = 0
new_im = Image.new('RGB', (width*row_limit,math.ceil((len(imagelist)/row_limit))*height))
print(int(math.sqrt(width)))
for x in imagelist:
    if x_offset == width * row_limit:
        x_offset = 0
        y_offset += height
    out_image = Image.open(f"{x}").convert('RGBA')
    new_im.paste(out_image, (x_offset,y_offset))
    print(f"{x}: X:{x_offset}, Y:{y_offset}")
    x_offset += width
new_im.save(f'{dir_path}/combine.png')
