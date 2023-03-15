import PIL

imagea = PIL.Image.open('temp.png')
imageb = PIL.Image.open('temp.png')

for y in range(imagea.size[1]):
  for x in range(imagea.size[0]):
    currentPixel = imagea.getpixel((x,y))

    if currentPixel[0] >  50:
    #if currentPixel ==(0,0,0):
      #this is a black pixel, you can directly modify image 2 now
      imageb.putpixel((x,y),(0,0,0))

imageb.save('outputfile.png')