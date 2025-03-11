from time import sleep


def sender(lora):
    def send_message(message):
        print("Sending:", message)
        lora.println(message)
        sleep(1)  # Delay between messages

    while True:
        send_message("Hello, LoRa!")
        print("Sent")
        sleep(1)
