import board
import neopixel
    
    
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
    
num_leds = 36
num_tiles = 6
num_pixels = num_leds * num_tiles
    
tiles = [{
    "name": "consul",
    "r": 198,
    "g": 42,
    "b": 113
}, {
    "name": "vagrant",
    "r": 21,
    "g": 99,
    "b": 255
}, {
    "name": "packer",
    "r": 29,
    "g": 174,
    "b": 255
},{
    "name": "terraform",
    "r": 92,
    "g": 78,
    "b": 229
},{
    "name": "vault",
    "r": 106,
    "g": 109,
    "b": 122
}, {
    "name": "nomad",
    "r": 37,
    "g": 186,
    "b": 129
}, {
    "name": "hashicorp",
    "r": 255,
    "g": 255,
    "b": 255
}]

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB
    
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
    
while True:
    current_tile = 0
    for tile in tiles:
        start_pixel = current_tile * num_leds
        end_pixel = start_pixel + num_leds
        for pixel in range(start_pixel, end_pixel):
            pixels[pixel] = (tile["r"], tile["g"], tile["b"])
            # print((tile["r"], tile["g"], tile["b"]))

    pixels.show()