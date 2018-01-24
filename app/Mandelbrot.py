'''
David Fuller

Mandelbrot class: Class to handle creating and displaying a Mandelbrot set.

1-24-2018
'''

from .Constants import color, resolution, point


class Pixel(object):
    '''
    Sets up a Pixel object.
    '''
    
    def __init__(self,
                 position = point(x = 0, y = 0),
                 size = resolution(width = 1, height = 1),
                 pixel_color = color(r = 0, g = 0, b = 0)):
        '''
        App's init method.

        Stores pixel attributes.

        Args:
            size (int): Height and width of a pixel.
            pixel_color (rgb): Default color of a pixel.
        '''

        self.position = position
        self.size = size
        self.color = pixel_color

    def show(self, surface):
        '''
        Shows pixel on a given surface at a given coordinate.

        Args:
            surface (pygame.surface): Surface to show pixel on.
        '''
        
        surface.fill(self.color, (self.position, self.size))

class Mandelbrot(object):
    '''
    Sets up a Mandelbrot object.
    '''
    
    def __init__(self):
        '''
        App's init method.

        Initializes pixel array.
        '''
        
        self.pixel_array = []

    @staticmethod
    def map_value(value, old_lower, old_upper, new_lower, new_upper):
        '''
        Maps a value from an old range into a new range.

        Args:
            value (int): Input value to map.
            old_lower (int): Lower boundary of old range.
            old_uppper (int): Upper boundary of old range.
            new_lower (int): Lower boundary of new range.
            new_lower (int): Lower boundary of new range.

        Returns:
            Int: The mapped value.
        '''
        
        old_range = old_upper - old_lower
        new_range = new_upper - new_lower
        return ((value - old_lower) / old_range) * new_range + new_lower

    def update(self, surface, surface_resolution):
        '''
        Creates the mandelbrot set and stores pixels appropriately.

        Args:
            surface (pygame.surface): Surface to show pixel on.
            surface_resolution (width, height): Width and height of surface.
        '''
        
        width = surface_resolution.width
        height = surface_resolution.height
        for x in range(width):
            self.pixel_array.append([])
            for y in range(height):
                a = Mandelbrot.map_value(x, 0, width, -2.5, 2.5)
                b = Mandelbrot.map_value(y, 0, height, -2.5, 2.5)

                current_a = a
                current_b = b

                iteration = 0

                while iteration < 100:
                    real = (a * a) - (b * b)
                    composite = 2 * a * b

                    a = real + current_a
                    b = composite + current_b

                    if abs(a + b) > 16:
                        break

                    iteration = iteration + 1

                if iteration == 100:
                    hue = 0
                else:
                    hue = Mandelbrot.map_value(iteration, 0, 100, 0, 255)
                    
                pixel_color = color(r = hue, g = hue, b = hue)
                position = point(x = x, y = y)
                self.pixel_array[x].append(Pixel(position = position,
                                                 pixel_color = pixel_color))
                
    def show(self, surface, surface_resolution):
        '''
        Shows pixel on a given surface at a given coordinate.

        Args:
            surface (pygame.surface): Surface to show pixel on.
            surface_resolution (width, height): Width and height of surface.
        '''
        
        for x in range(surface_resolution.width):
            for y in range(surface_resolution.height):
                self.pixel_array[x][y].show(surface)
                
