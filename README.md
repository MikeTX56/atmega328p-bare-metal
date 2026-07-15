<<<<<<< HEAD
# ATmega328P Bare-Metal C Development

A collection of bare-metal C drivers, applications, and register-level firmware for the **ATmega328P** 8-bit AVR microcontroller. 

The goal of this repository is to bypass the Arduino abstraction layer entirely—communicating directly with the hardware by manipulating control registers, configuring interrupts, and managing system clocks using the official ATmega328P datasheet.

---

## 🛠️ Tech Stack & Toolchain
* **Language:** Pure Embedded C (C99)
* **Compiler:** `avr-gcc`
* **Flashing Tool:** `avrdude`
* **Build System:** Custom GNU `Makefile`
* **Hardware:** ATmega328P (standalone chip or Arduino Uno board) / USBasp or Arduino as ISP programmer

---

## Repository Structure
This repository is organized into modular drivers and hardware-verification projects:

* `drivers/` — Reusable hardware abstraction layers (HAL) written from scratch.
  * `gpio/` — Port configuration, input/output, and register bitmask macros.
  * `usart/` — Polling and interrupt-driven serial communication.
  * `timer/` — Hardware delay timers, system ticks, and PWM generation.
  * `adc/` — Analog-to-digital conversion using polling and interrupts.
* `projects/` — Complete bare-metal applications (e.g., UART terminal, sensor readers, custom bootloaders).

---

# ATmega328P Bare-Metal C Development

A collection of bare-metal C drivers, applications, and register-level firmware for the **ATmega328P** 8-bit AVR microcontroller.

The goal of this repository is to bypass the Arduino abstraction layer entirely by communicating directly with the hardware through control registers, interrupts, and clock configuration based on the official ATmega328P datasheet.

## Tech Stack & Toolchain

- Language: Pure Embedded C (C99)
- Compiler: `avr-gcc`
- Flashing Tool: `avrdude`
- Build System: Custom GNU `Makefile`
- Hardware: ATmega328P standalone chip or Arduino Uno board

## Repository Structure

- `drivers/` - Reusable hardware abstraction layers (HAL) written from scratch
  - `gpio/` - Port configuration, input/output, and register bitmask macros
  - `usart/` - Polling and interrupt-driven serial communication
  - `timer/` - Hardware delay timers, system ticks, and PWM generation
  - `adc/` - Analog-to-digital conversion using polling and interrupts
- `projects/` - Complete bare-metal applications and demos

### Included Project

- `atmega328p-oled-image-viewer/` - SSD1306 OLED image viewer using bit-banged I2C and PlatformIO

## Getting Started

### Prerequisites

Install the AVR toolchain on your machine.

For Linux (Ubuntu/Debian):

```bash
sudo apt-get install gcc-avr binutils-avr avr-libc avrdude
```

## OLED Image Viewer

This project drives a 128x64 SSD1306 OLED from an ATmega328P/Arduino Uno using bit-banged I2C with no Wire library.

### Features

- Bare-metal AVR C with direct register control
- Software I2C on `PC4`/`PC5` (`A4`/`A5` on Uno)
- SSD1306 init and page addressing
- Full 128x64 image rendering from `image_data[1024]`
- PlatformIO build support

### Project Structure

- `platformio.ini` - PlatformIO environment (`uno`)
- `src/main.c` - OLED driver and image rendering logic
- `src/im.py` - Optional PNG-to-SSD1306 byte converter
- `wokwi/` - Wokwi helper files and docs

### Hardware Mapping

For Arduino Uno / ATmega328P:

- `SDA` -> `A4` (`PC4`)
- `SCL` -> `A5` (`PC5`)
- `VCC` -> module spec (3.3V/5V)
- `GND` -> `GND`

SSD1306 I2C address used in code: `0x3C` (written as `0x78` because of left-shifted write format).

### Build

From the project root:

```bash
platformio run
```

If your setup needs an explicit environment:

```bash
platformio run -e uno
```

### Flash to Real Board

```bash
platformio run -t upload
```

If auto-port detection fails:

```bash
platformio run -t upload --upload-port /dev/ttyUSB0
```

### Run in Wokwi

1. Open Wokwi and create an Arduino Uno project.
2. Add the `SSD1306 128x64 I2C` part.
3. Copy the firmware from `src/main.c` into the editor.
4. Start the simulation.

If you prefer a zip project, create one locally and import it into Wokwi:

```bash
zip -r wokwi_project.zip platformio.ini src
```

### Using Your Own Image

Option A: Inline bytes in `main.c`.

Replace the `image_data[1024]` array in `src/main.c` with converted bytes.

Option B: Generate bytes from a PNG.

Use `src/im.py`:

```bash
python3 -m pip install --user pillow
python3 src/im.py input.png src/image.h
```

Then either copy the values from `src/image.h` into the inline array or include the header from `main.c`.

### Image Format Notes

- Size must be `128x64`
- Monochrome, with 1-bit behavior after thresholding
- SSD1306 page format: `8 pages x 128 columns = 1024 bytes`
- If output looks inverted, flip the threshold logic in the converter

### Common Issues

- Blank screen: check SDA/SCL wiring and power level
- Wrong orientation or inversion: conversion bit order or threshold polarity mismatch
- Build warning `F_CPU redefined`: usually harmless in this setup

## License

Add your preferred license if this project will be shared publicly.
