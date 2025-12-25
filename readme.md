# Fala’s Hackpad

Hey! This is my custom built macropad made as part of the Hackpad project.  
The goal was to design something simple, clean, and fully functional while following all the project rules. This hackpad uses the Seeed XIAO RP2040 and is designed with a custom PCB and a fully 3D printed case.

I focused on keeping the design compact, easy to build, and reliable, while also making sure everything fits together properly in the final assembly.

## Overview

This is a four key macropad with a custom PCB and case.  
The firmware is written using KMK and runs on CircuitPython.

Everything in this repository is structured so anyone can understand how the hackpad was built and how the parts fit together.

## Hackpad Preview

Below are screenshots of the complete project.

1. Overall hackpad design and assembly  
   This shows how the PCB and case fit together as a complete unit.

2. Schematic  
   The electrical schematic used to design the PCB.

3. PCB layout  
   The routed PCB design created in KiCad.

4. Case design  
   The top and bottom case parts and how they assemble around the PCB.

## Bill of Materials

1. Seeed XIAO RP2040  
2. MX style mechanical switches x4  
3. 1N4148 diodes x4  
4. SK6812 Mini E RGB LEDs x2  
5. M3 screws  
6. 3D printed case parts

All parts used are from the approved list for the Hackpad project.

## Repository Structure

The repository is organized into three main folders.

1. CAD  
   Contains the final assembled 3D model of the hackpad exported as a STEP file.

2. PCB  
   Contains the KiCad project files including the schematic and PCB layout.

3. Firmware  
   Contains the KMK firmware used to run the macropad.

## Firmware

The firmware is written using KMK and runs on CircuitPython.  
Each key is connected directly to a GPIO pin on the XIAO RP2040. The current keymap is simple and meant for testing, and it can be easily modified later.

## Final Notes

This project was a great learning experience and helped me understand PCB design, 3D case design, and firmware integration better. Everything here is designed to be buildable and practical.

Thanks for checking it out.
