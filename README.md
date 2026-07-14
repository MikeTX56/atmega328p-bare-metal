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

## Getting Started

### Prerequisites
Make sure you have the AVR toolchain installed on your machine.

**For Linux (Ubuntu/Debian):**
```bash
sudo apt-get install gcc-avr binutils-avr avr-libc avrdude
