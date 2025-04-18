from time import sleep
import machine
from machine import Pin
import json
import time


uart = machine.UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))
external_temperature = machine.ADC(28)
temperature_sensor = machine.ADC(4)


def calculate_checksum(data):
    """Calculate checksum for the data (sum of the first three bytes excluding the checksum)"""
    checksum = sum(data[:-1]) & 0xFF  # Sum the first three bytes and mask to 8 bits
    return checksum

def get_distance():
    uart.write(b'1')  # Send command to the sensor to request distance measurement
    
    # Read 4 bytes of data
    if uart.any():
        data = uart.read(4)
        
        if data and len(data) == 4:
            # Extract the high and low bytes of the distance
            high_byte = data[1]
            low_byte = data[2]
            distance = (high_byte << 8) | low_byte  # Combine the high and low byte to form the distance
            
            # Extract the checksum byte
            checksum = data[3]
            
            # Validate checksum
            if checksum == calculate_checksum(data):
                return distance
            else:
                print("Checksum error!")
    return None


def get_avg_distance(count):
    total = 0
    samples = 0
    for i in range(count):
        cm = get_distance()
        if cm:
            total += cm
            samples += 1
        sleep(1)
            
    if samples > 0:
        return total / (samples*1.0)
        

def get_internal_temperature():
    adc_value = temperature_sensor.read_u16()
    voltage = adc_value * (3.3 / 65535.0)
    return 27 - (voltage - 0.706) / 0.001721


def get_external_temperature():
    V0_C = 0.500  # Output voltage at 0°C in volts (500 mV)
    TC = 0.010    # Temperature coefficient in volts per °C (10 mV/°C)
    adc_value = external_temperature.read_u16()
    voltage = adc_value * (3.3 / 65535.0)
    return (voltage - V0_C) / TC


def sender(lora):
    def send_message(message):
        print("Sending:", message)
        lora.println(message)
        sleep(1)  # Delay between messages

    internal_temp = get_internal_temperature()
    cm = get_avg_distance(5)
    ext_temp = get_external_temperature()
    msg = {"it": internal_temp, "et": ext_temp, "cm":cm}
    msg_str = json.dumps(msg)
    send_message(msg_str)
    print(msg_str)

