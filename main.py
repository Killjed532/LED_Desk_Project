import time
from rpi_ws281x import *
from gif_to_matrix import get_frames_from_gif
import os
import random

# Define the directory containing the GIF files
gif_dir = 'testfolder/'

# Get a list of all files in the directory
gif_files = [f for f in os.listdir(gif_dir) if f.endswith('.gif')]
# LED strip configuration:
LED_WIDTH = 50          # Width of the matrix
LED_HEIGHT = 30         # Height of the matrix
LED_COUNT = 2330        # Total number of LEDs
LED_PIN = 18            # GPIO pin connected to the pixels (18 uses PWM).
LED_FREQ_HZ = 800000    # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10            # DMA channel to use for generating signal
LED_BRIGHTNESS = 30      # Set to 0 for darkest and 255 for brightest
LED_INVERT = False      # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0         # set to '1' for GPIOs 13, 19, 41, 45 or 53
WS2812_STRIP = ws.WS2812_STRIP
GAMMA = None
START_LED = 1500
END_LED = 2330

# Create PixelStrip object with the specified configuration
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, WS2812_STRIP, GAMMA)
strip.begin()
color_index = 0


def update_led_strip_with_current_color():
    global color_index

    r = color_index // (255 * 255)
    g = (color_index // 255) % 255
    b = color_index % 255

    color_index = (color_index + 1) % (255 * 255 * 255)

    color = Color(r, g, b)
    for i in range(START_LED, END_LED):
        strip.setPixelColor(i, color)
    strip.show()


def display_frame_on_led(frame):
    """Displays a single frame on the LED matrix.
    Args:
        frame (np.array): The frame to display, with shape (LED_HEIGHT, LED_WIDTH, 3 or 4).
                          Each entry in the array is an RGB or RGBW tuple."""

    for y in range(LED_HEIGHT):
        for x in range(LED_WIDTH):
            # Calculate the index of the pixel in the strip
            index = y * LED_WIDTH + x

            # Adjust for matrices wired in a zigzag pattern
            if y % 2 == 1:
                index = y * LED_WIDTH + (LED_WIDTH - 1 - x)

            # Get the RGB (and optionally W) values for the current pixel
            r, g, b = int(frame[y, x][0]), int(frame[y, x][1]), int(frame[y, x][2])
            color = Color(r, g, b)
            # Set the color of the pixel
            strip.setPixelColor(index, color)

    strip.show()

def display_frames(frames):
    # Display the current frame
    for frame in frames:
        display_frame_on_led(frame)
        update_led_strip_with_current_color()
        time.sleep(.15)


index = 0  # Initialize index to start from the first GIF file

while True:  # Loop indefinitely
    # Get the full path of the GIF file
    gif_file = gif_files[index]
    gif_path = os.path.join(gif_dir, gif_file)

    # Get frames from the current GIF file
    frames = get_frames_from_gif(gif_path)

    # Display frames on LED matrix
    display_frames(frames)
    # Increment index and loop back to 0 if it exceeds the length of gif_files
    index = (index + 1) % len(gif_files)



