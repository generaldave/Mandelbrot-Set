'''
David Fuller

Constants file - File contains application constants.

10-15-2017
'''

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
color = namedtuple('color', ['r', 'g', 'b'])
resolution = namedtuple('resolution', ['width', 'height'])

screen_resolution = resolution(width = 360, height = 360)

app_title = "Mandelbrot Set"
fps = 60
