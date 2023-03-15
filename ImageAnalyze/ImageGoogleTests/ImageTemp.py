from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

path_ref_error = "..//Images//imageCropRefError.png"
path_ref_to_test = "..//Images//imageCrop.png"
path_ref_to_test1 = "..//Images//imageCrop1.png"
path_res = "..//Images//imageRes.png"


im=Image.open(path_ref_to_test1)
im1 = Image.open(path_ref_to_test).convert('1') # binary image for pixel evaluation
p1 = im1.load()

im2 = Image.open(path_ref_error).convert('1') # binary image for pixel evaluation
p2 = im2.load()

width = im1.size[0]
height = im1.size[1]

for i in range(0, width):
      for j in range(0, height):

            if (p1[i,j] != p2[i,j]) :
                print ('mismatch found i=',i,',j=',j)
                im.putpixel((i, j), (0, 255, 0))


im.show()
im.save(path_res)