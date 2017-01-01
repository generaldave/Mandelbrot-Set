########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# init class: App initializer                                          #
#                                                                      #
# Created on 2016-1-1                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Constants import *   # Constants file
from   Pixel     import *   # Pixel Class
import pygame               # For GUI

########################################################################
#                                                                      #
#                              INIT CLASS                              #
#                                                                      #
########################################################################

class init(object):
    def __init__(self, appDirectory):
        self.appDirectory = appDirectory

        # Set up GUI
        self.setupGUI()

        # Set up pixel array
        self.setupPixelArray()

        # Draw Mandelbrot set
        self.drawMandelbrot()

        # Run app
        self.runApp()

    # Mehtod sets up GUI
    def setupGUI(self):
        # Screen attributes
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()      # For frames per second
        self.mouse = pygame.mouse.get_pos()   # For mouse position

        # Initialize Pixel object
        self.pixel = Pixel(self.screen)

    # Method sets up pixel array
    def setupPixelArray(self):
        self.pixelArray = []
        for y in range(SCREEN_HEIGHT):
            for x in range(SCREEN_WIDTH):
                self.pixelArray.append((x, y))

    # Method maps to new range
    def Map(self, value, mini, maxi, tomini, tomaxi):
        oldRange = (maxi - mini)
        newRange = (tomaxi - tomini)
        return (((value - mini) * newRange) / oldRange) + tomini

    # Method draws Mandelbrot
    def drawMandelbrot(self):
        for x in range(SCREEN_WIDTH):
            for y in range(SCREEN_HEIGHT):
                # f(z) = z^2 + c
                # c = a + bi
                # i = sqrt(-1)
                a = self.Map(x, 0, SCREEN_WIDTH,  MIN_RANGE, MAX_RANGE)
                b = self.Map(y, 0, SCREEN_HEIGHT, MIN_RANGE, MAX_RANGE)

                # Current a and b
                currenta = a
                currentb = b

                # iteration counter
                iteration = ZERO

                # Iterate toward 'infinity'
                while iteration < MAX_ITERATION:
                    # Store real and composite calculations
                    real      = (a * a) - (b * b)
                    composite = TWO * a * b

                    # '+ c' part
                    a = real      + currenta
                    b = composite + currentb

                    # Break if approaching 'infinity'
                    if abs(a + b) > 16:
                        break

                    # Increment iteration
                    iteration = iteration + ONE

                # Colour generator part of Mandelbrot set
                red = green = blue = self.Map(iteration,           \
                                              ZERO, MAX_ITERATION, \
                                              ZERO, COLOR_MAX)
                colour = (red, green, blue)

                # If not part of Mandelbrot set, make colour black
                if iteration == MAX_ITERATION:
                    colour = Colour['BLACK']

                # Draw pixel
                coord = (x, y)
                self.pixel.drawPixel(coord, colour)
        
    # Method runs app
    def runApp(self):
        running = True
        while running:
            for event in pygame.event.get():

                # Handle quit event
                if event.type == pygame.QUIT:
                    running = False

            # Update Screen
            pygame.display.update()
            self.clock.tick(FPS)            

        # Close app cleanly
        pygame.quit()
        
