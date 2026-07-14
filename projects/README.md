# ATmega328P OLED Image Viewer (SSD1306, Bare Metal)

This project drives a 128x64 SSD1306 OLED from an ATmega328P/Arduino Uno using **bit-banged I2C** (no Wire library).

It currently renders a full-screen monochrome bitmap from bytes embedded directly in `src/main.c`.

## Features

- Bare-metal AVR C (direct register control)
- Software I2C on `PC4`/`PC5` (`A4`/`A5` on Uno)
- SSD1306 init + page addressing
- Draw full 128x64 image from `image_data[1024]`
- PlatformIO build support

## Project Structure

- `platformio.ini` - PlatformIO environment (`uno`)
- `src/main.c` - OLED driver + image rendering logic
- `src/im.py` - Optional PNG-to-SSD1306 byte converter
- `wokwi/` - Wokwi helper files/docs

## Hardware Mapping

For Arduino Uno / ATmega328P:

- `SDA` -> `A4` (`PC4`)
- `SCL` -> `A5` (`PC5`)
- `VCC` -> module spec (3.3V/5V)
- `GND` -> `GND`

SSD1306 I2C address used in code: `0x3C` (written as `0x78` because of left-shifted write format).

## Build

From project root:

```bash
platformio run
```

If your setup needs explicit env:

```bash
platformio run -e uno
```

## Flash to Real Board

```bash
platformio run -t upload
```

If auto-port fails:

```bash
platformio run -t upload --upload-port /dev/ttyUSB0
```

## Run in Wokwi

1. Open Wokwi and create an Arduino Uno project.
2. Add part: `SSD1306 128x64 I2C`.
3. Copy your firmware (`src/main.c`) into the editor code.
4. Start simulation.

If you prefer a zip project, create one locally and import/drag into Wokwi:

```bash
zip -r wokwi_project.zip platformio.ini src
```

## Using Your Own Image

### Option A: Inline bytes in `main.c` (current approach)

Replace the `image_data[1024]` array in `src/main.c` with your converted bytes.

### Option B: Generate bytes from PNG

Use `src/im.py`:

```bash
python3 -m pip install --user pillow
python3 src/im.py input.png src/image.h
```

Then either:

- Copy values from `src/image.h` into the inline array, or
- Include the header from `main.c` and use `image_data` from there.

## Image Format Notes

- Size must be `128x64`
- Monochrome (`1-bit` behavior after thresholding)
- SSD1306 page format: `8 pages x 128 columns = 1024 bytes`
- If output looks inverted, flip threshold logic in converter (`v < threshold` vs `v > threshold`)

## Common Issues

- **Blank screen**: check SDA/SCL wiring and power level.
- **Wrong orientation/inverted**: conversion bit order or threshold polarity mismatch.
- **Build warning (`F_CPU redefined`)**: usually harmless in this setup.

## License

Add your preferred license (MIT/Apache-2.0/etc.) if this project will be shared publicly.
