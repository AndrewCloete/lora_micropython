import network
import time
from umqttsimple import MQTTClient
import env

# --- Wi‑Fi Configuration ---
WIFI_SSID = env.wifi_ssid
WIFI_PASSWORD = env.wifi_psw

# --- MQTT Configuration ---
MQTT_BROKER = env.mqtt_host
MQTT_PORT = 1883
MQTT_USER = env.mqtt_user
MQTT_PSW = env.mqtt_psw
CLIENT_ID = "pico-w-mqtt"
TOPIC = b"pico/w/test"


def receiver(lora, wd):
    # Initialize the Wi‑Fi interface in station mode
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    # Wait until the connection succeeds
    print("Connecting to Wi‑Fi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to Wi‑Fi!")
    print("Network config:", wlan.ifconfig())

    client = MQTTClient(CLIENT_ID, MQTT_BROKER, MQTT_PORT, MQTT_USER, MQTT_PSW)

    # Connect to the MQTT broker
    client.connect()
    print("Connected to MQTT broker:", MQTT_BROKER)

    while True:
        if lora.receivedPacket():
            try:
                payload = lora.readPayload().decode()
                rssi = lora.packetRssi()
                msg = "RX: {} | RSSI: {}".format(payload, rssi)
                print(msg)
                client.publish(TOPIC, msg)
                print("Published a message to", TOPIC)
            except Exception as e:
                print(e)
        wd.feed()
