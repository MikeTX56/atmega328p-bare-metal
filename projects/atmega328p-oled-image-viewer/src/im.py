#!/usr/bin/env python3
# Requires Pillow: pip install pillow
from PIL import Image
import sys

if len(sys.argv) < 3:
    print("Usage: img2ssd1306.py in.png out.h")
    sys.exit(1)

img = Image.open(sys.argv[1]).convert("L").resize((128,64))
threshold = 128
pix = img.load()

buf = []
for page in range(8):
    for x in range(128):
        byte = 0
        for bit in range(8):
            y = page*8 + bit
            v = pix[x,y]
            if v < threshold:           # black pixel -> set bit (change invert logic if needed)
                byte |= (1 << bit)     # bit0 is top of page
        buf.append(byte)

name = "image_data"
with open(sys.argv[2],"w") as f:
    f.write("#pragma once\n")
    f.write("#include <stdint.h>\n")
    f.write("const uint8_t %s[1024] = {\n" % name)
    for i,b in enumerate(buf):
        if i % 12 == 0:
            f.write("    ")
        f.write("0x%02X," % b)
        if i % 12 == 11:
            f.write("\n")
        else:
            f.write(" ")
    f.write("\n};\n")
print("Wrote", sys.argv[2])