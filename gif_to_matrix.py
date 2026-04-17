from PIL import Image, ImageSequence
import numpy as np

# Open the GIF file
def get_frames_from_gif(gif_path):
    try:
        gif = Image.open(gif_path)
        frames = []
        for frame in ImageSequence.Iterator(gif):
            frame = frame.convert('RGB')
            frame = frame.resize((50, 30))
            np_frame = np.array(frame)
            frames.append(np_frame)
        return frames
    except Exception as e:
        print(f"An error occurred while processing {gif_path}: {e}")
        return []


