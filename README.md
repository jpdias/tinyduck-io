# duck2spark + PlatformIO

## What?

A Rubber Ducky is a device that acts as an USB Human Interface Device with the purpose of doing "stuff" (e.g. run a script) on a target machine. The original Rubber Ducky was created by [Hak5](http://www.hak5.org/) along with a simple DSL for quickly creating scripts known as Ducky Script ([see more](https://github.com/hak5darren/USB-Rubber-Ducky/wiki)). 

Although expensive, the same tool can be recreated using cheap alternatives such as the Digispark. *Digispark is a microcontroller board which has ATTINY 85 MCU as its heart and running with 16.5Mhz frequency with 8KB of memory and have 5 GPIO pins, this MCU board is cheapest and smallest Arduino Board available in the market good for wearables and small projects.*^[https://www.instructables.com/id/Digispark-Attiny-85-With-Arduino-IDE/] 

However, there it is hard to reprogram the board with a new script without depending on Arduino IDE and its *particularities*. Addressing such issues, and using the scripts created by [mame82](https://github.com/mame82/duck2spark), this repository is a sample of a [PlatformIO](https://platformio.org) project that allows one to quickly deploy scripts specified in Ducky Script to the Digispark Attiny85 board.

## Requirements

- [Digispark Attiny85 by Digistump](http://digistump.com/products/1) ~ 1.4$ on Aliexpress
- [PlatformIO CLI](https://platformio.org)

## Deploying a new Ducky Script

0. Start with your Digispark disconnected from your computer
1. Install PlatformIO (CLI tools part of [PlatformIO Core](https://platformio.org/install/cli) are enough)
2. Specify the payload to be run (Ducky Script) in the file `script.duck`. Some examples are available [here](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Payloads)
3. *temporary* Set the target operating system language in the `build.py` script.
    - E.g.: `env.Execute("java -jar encoder.jar -i script.duck -o output.bin -l pt")` the `pt` sets the target machine keyboard as Portuguese. 
4. `$ platformio run` to check if everything is ok in the project (build the project).
5. `$ platformio run --target upload` to build the project and send it to the board.
    - When the phrase `Uploading .pio/build/attiny85/firmware.hex` appears connect the Digispark an wait for the upload to complete.
6. Try it.