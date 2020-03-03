import bottle
import render
import random

@bottle.route('/<width:int>/<height:int>')
def image(width, height):
    if width % 2 == 1:
        width -= 1
    if height % 2 == 1:
        height -= 1
    pixels = [0] * (width * height)
    for x in range(0, width // 2, 1):
        for y in range(0, height // 2, 1):
            val = int(random.uniform(0, 255))
            pixels[x + y * height] = val
            pixels[x + (height - y -1) * height] = val
            pixels[width - x - 1 + y * height] = val
            pixels[width - x - 1 + (height - y - 1) * height] = val
    return render.image(width, height, pixels)

bottle.run(host='localhost', port=8080)
