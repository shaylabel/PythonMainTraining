from PIL import Image



path_ref_error = "..//Images//imageCropRefError.png"
path_ref_to_test = "..//Images//imageCrop.png"
path_res = "..//Images//imageCrop5.png"

im = Image.open(path_ref_to_test)
for i in range(1, 100):
    for j in range (1,199):
        im.putpixel((i, j), (255, 0, 255))


im.save(path_res)

def redOrBlack (im):
    newimdata = []
    redcolor = (0,255,0)
    blackcolor = (0,255,0)
    for color in im.getdata():
        if color == redcolor:
            newimdata.append(redcolor)
        else:
            newimdata.append( blackcolor )




    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

# redOrBlack(im).save(path_res)