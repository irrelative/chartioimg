import StringIO, os
import web
from PIL import Image

class Index(object):

    def GET(self):
        return '''
        <html><body>
            <form enctype="multipart/form-data" method="post" action="">
                <input type="file" name="img" />
                <button>Convert</button>
            </form>
        '''

    def POST(self):
        inp = web.input()
        im = Image.open(StringIO.StringIO(inp.img))
        size = 100, 100
        im.thumbnail(size, Image.ANTIALIAS)
        values = []
        for x in range(im.width):
            for y in range(im.height):
                values.append('%d, %d, %d' % (x, y, (255 * 3 - sum(im.getpixel((x,y))))))

        return 'SELECT ' + ' UNION ALL\nSELECT '.join(values)


urls = ('/', Index)

app = web.application(urls)

if __name__ == '__main__':
    app.run()
