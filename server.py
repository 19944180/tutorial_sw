import bottle
import render

@bottle.route('/<width:int>/<height:int>')
def image(width, height):
    pixels = [0] * (width * height)
    # your code goes here
    return render.image(width, height, pixels)

bottle.run(host='localhost', port=8080)
