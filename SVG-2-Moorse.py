import argparse
from PIL import Image
import numpy as np
from itertools import groupby

def extract_morse_from_image(image_path):
    rgb_image = Image.open(image_path).convert("RGB")
    rgb_array = np.array(rgb_image)

    green_mask = (
        (rgb_array[:, :, 1] > 200) &
        (rgb_array[:, :, 0] < 100) &
        (rgb_array[:, :, 2] < 100)
    )

    green_signal_1d = green_mask.any(axis=0).astype(int)
    runs = [(val, sum(1 for _ in group)) for val, group in groupby(green_signal_1d)]

    signal_lengths = [length for val, length in runs if val == 1]
    space_lengths = [length for val, length in runs if val == 0]

    if not signal_lengths or not space_lengths:
        return "No Morse signal detected."

    min_dot = min(signal_lengths)
    dot_dash_threshold = min_dot * 2

    min_space = min(space_lengths)
    letter_space_threshold = min_space * 3
    word_space_threshold = min_space * 6

    morse_code = ""
    for val, length in runs:
        if val == 1:
            morse_code += "." if length < dot_dash_threshold else "-"
        else:
            if length >= word_space_threshold:
                morse_code += "   "
            elif length >= letter_space_threshold:
                morse_code += " "

    return morse_code

def main():
    parser = argparse.ArgumentParser(description="Extract Morse code from an image of neon green dots on black.")
    parser.add_argument("image_path", help="Path to the input image file.")
    args = parser.parse_args()

    morse = extract_morse_from_image(args.image_path)
    print("Extracted Morse Code:")
    print(morse)

if __name__ == "__main__":
    main()
