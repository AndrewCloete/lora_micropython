import machine
from machine import SPI, Pin
from sx127x import SX127x
import rx

nss = Pin(8, Pin.OUT)  # Chip select
reset = Pin(9, Pin.OUT)  # Reset pin
dio0 = Pin(7, Pin.IN)  # IRQ pin
dio1 = Pin(10, Pin.IN)  # Interrupt pin (if used)


# Define SPI and pins based on your provided mapping
spi = SPI(
    0, baudrate=500000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16)
)
pins = {
    "ss": 8,  # NSS (CS)
    "reset": 9,  # RESET (RST)
    "dio0": 7,  # DIO0 (G0)
    "dio1": 10,  # DIO1 (G1)
}

lora = SX127x(spi, pins, parameters={"frequency": 868000000})


# SLEEP_DURATION = 10000  # 10 seconds
# tx.sender(lora)
# print("Going to deep sleep for 10 seconds...")
# time.sleep(1)
# machine.deepsleep(SLEEP_DURATION)

wd = machine.WDT(timeout=8000)
rx.receiver(lora, wd)
