import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print("isconnected:", wlan.isconnected())

