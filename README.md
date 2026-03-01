# IDE
Thonny is not professional but it is damn easy. Flash the pi with the `u2f`
file.

# Todo
- Still need to figure out why the RFM95 module does not work when the RESET
line is connected


```sh

uv pip install mpremote
# List the files on the remote
mpremote fs ls
# Copy all the basestation files over
mpremote cp sx127x.py :
mpremote cp base_station/* :

mpremote cp field_node/* :

```

Homeassistant configuration.yaml
```yaml
mqtt:
  sensor:
    - name: "lora_heartbeat"
      unique_id: "lora_heartbeat"
      state_topic: "pico/w/test/hb"
      value_template: >
        {% set rssi = value.split('HB: ')[1] | trim %}
        {{ rssi | int }}
      unit_of_measurement: "count"

    - name: "LoRa RSSI"
      unique_id: "lora_rssi"
      state_topic: "pico/w/test"
      value_template: >
        {% set rssi = value.split('RSSI:')[1] | trim %}
        {{ rssi | int }}
      unit_of_measurement: "dBm"

    - name: "LoRa et"
      unique_id: "lora_et"
      state_topic: "pico/w/test"
      value_template: >
        {% set json_str = value.split('RX:')[1].split('|')[0] | trim %}
        {% set data = json_str | from_json %}
        {{ data.et | float }}
      unit_of_measurement: "°C"
      device_class: temperature
      state_class: measurement

    - name: "LoRa it"
      unique_id: "lora_it"
      state_topic: "pico/w/test"
      value_template: >
        {% set json_str = value.split('RX:')[1].split('|')[0] | trim %}
        {% set data = json_str | from_json %}
        {{ data.it | float }}
      unit_of_measurement: "°C"
      device_class: temperature
      state_class: measurement

    - name: "LoRa cm"
      unique_id: "lora_cm"
      state_topic: "pico/w/test"
      value_template: >
        {% set json_str = value.split('RX:')[1].split('|')[0] | trim %}
        {% set data = json_str | from_json %}
        {{ data.cm | float }}
      unit_of_measurement: "cm"

```


# farmassistant networking setup
```sh
# You can ssh
ssh farmassistant.local
# since avahi is set up

vim /etc/network/interfaces
```
.. add
```
auto eno1
iface eno1 inet static
   address 192.168.0.142
   netmask 255.255.255.0
   gateway 192.168.0.1
   dns-nameservers 192.168.0.1 8.8.8.8 8.8.4.4
```

# Lora Pinout
```
Pico	RP20401	            SX1276	RFM95W
3V3         	            VCC     VIN
GND     GND	                GND	    GND
Pin 10  GP7	                DIO0    G0
Pin 14  GP10                DIO1    G1
Pin 11  GP8	                NSS	    CS
Pin 12  GP9	                RESE    RST
Pin 21  GP16 (SPI0 RX)	    MISO    MISO
Pin 24  GP18 (SPI0 SCK)	    SCK	    SCK
Pin 25  GP19 (SPI0 TX)	    MOSI    MOSI
```

# Ultrasonic (aj-sr04m)
Datasheet: https://www.fabian.com.mt/viewer/42585/pdf.pdf
https://wiki.dfrobot.com/Weatherproof_Ultrasonic_Sensor_With_Separate_Probe_SKU_SEN0208
https://www.robotics.org.za/AJ-SR04M
```
        GP12                RX
        GP13                TX
```

# Temp
https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/MCP970X-Family-Data-Sheet-DS20001942.pdf
```
        GP28                Vdd
```


Source: https://www.raspberrypi.com/news/how-to-add-lorawan-to-raspberry-pi-pico/

(The pin number in the code refer to the `GPxx` numbers, not the "pico" pins)
    

