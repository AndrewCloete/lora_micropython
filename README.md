# IDE
Thonny is not professional but it is damn easy. Flash the pi with the `u2f`
file.

# Todo
- Still need to figure out why the RFM95 module does not work when the RESET
line is connected




# Pinout
Pico	RP20401	            SX1276	RFM95W
3V3         	            VCC     VIN
GND     GND	                GND	    GND
Pin 10  GP7	                DIO0    G0
Pin 11  GP8	                NSS	    CS
Pin 12  GP9	                RESE    RST
Pin 14  GP10                DIO1    G1
Pin 21  GP16 (SPI0 RX)	    MISO    MISO
Pin 24  GP18 (SPI0 SCK)	    SCK	    SCK
Pin 25  GP19 (SPI0 TX)	    MOSI    MOSI

Source: https://www.raspberrypi.com/news/how-to-add-lorawan-to-raspberry-pi-pico/

(The pin number in the code refer to the `GPxx` numbers, not the "pico" pins)
