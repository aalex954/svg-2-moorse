# svg-2-moorse
Morse Code Extractor from Green Dot-Wave Images

This project processes an image containing neon green dots on a black background, typically formatted in a sine-wave pattern, to extract embedded Morse code and convert it into a plain-text string.

It's especially useful for decoding steganographic messages or visually encoded signals from stylized images.

## How It Works

- Image Preprocessing
  - The script starts by converting the input image into an RGB array. It isolates bright green pixels using color thresholding — looking for high green values and low red/blue components.
- Signal Detection
  - It then collapses the 2D green signal vertically, yielding a 1D binary array representing the presence (1) or absence (0) of signal at each horizontal pixel.
- Run-Length Analysis
  -  Using groupby, it measures the lengths of continuous signals (1s) and spaces (0s) to distinguish between:
    -  Dots (short pulses)
    -  Dashes (longer pulses)
    -  Letter breaks
    -  Word breaks
- Morse Code Construction
  - By analyzing the lengths and comparing them to adaptive thresholds, the script rebuilds the original Morse code message.
