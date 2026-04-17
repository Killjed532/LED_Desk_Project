import pygame

from gif_to_matrix import frames  # Assuming you have your frames defined in frames_data.py

# Configuration for the simulation
LED_WIDTH = 50  # Width of the matrix
LED_HEIGHT = 30  # Height of the matrix
LED_SIZE = 10  # Size of each simulated LED in pixels

# Initialize Pygame
pygame.init()
window_size = (LED_WIDTH * LED_SIZE, LED_HEIGHT * LED_SIZE)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("LED Matrix Simulation")


def display_frame_on_simulated_led(frame):
    """Displays a single frame on the simulated LED matrix."""
    for y in range(LED_HEIGHT):
        for x in range(LED_WIDTH):
            # Extract the RGB values for the current pixel from the frame
            r, g, b = frame[y, x]
            color = (int(g), int(r), int(b))
            # Draw each LED as a square
            rect = (x * LED_SIZE, y * LED_SIZE, LED_SIZE, LED_SIZE)
            pygame.draw.rect(screen, color, rect)

    # Update the display
    pygame.display.flip()


# Main loop to display each frame
running = True
frame_index = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the current frame
    display_frame_on_simulated_led(frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)  # Loop through the frames

    # Limit the frame rate (e.g., 10 frames per second)
    clock.tick(10)

pygame.quit()
