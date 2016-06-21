from PIL import Image


size = 64, 64

im = Image.open('dog2.jpg')
im.thumbnail(size, Image.ANTIALIAS)


values = []
for x in range(im.width):
    for y in range(im.height):
        values.append('%d, %d, %d' % (x, y, (255 * 3 - sum(im.getpixel((x,y))))))

print 'SELECT ' + ' UNION ALL\nSELECT '.join(values)
