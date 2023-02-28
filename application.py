import paho.mqtt.client as mqtt
from constants import USERNAME, PASSWORD, TOPIC, HOST, PORT

def send_mqtt_message(client: mqtt.Client, topic: str, message: str):
    client.publish(topic, message)

def turn_on(client: mqtt.Client):
    print("Light turned on")
    send_mqtt_message(client, TOPIC, "ON")

def turn_off(client: mqtt.Client):
    print("Light turned off")
    send_mqtt_message(client, TOPIC, "OFF")

def menu(client: mqtt.Client):
    value = input("""
        1. Turn on light
        2. Turn off light
        3. Exit
    \n""")

    if value == "1":
        turn_on(client)
    elif value == "2":
        turn_off(client)
    elif value == "3":
        client.disconnect()
        exit(0)
    else:
        print("Invalid input")

    menu(client)

if __name__ == "__main__":
    # MQTT Connection 
    try:
        client = mqtt.Client()
        client.username_pw_set(username=USERNAME, password=PASSWORD)
        client.connect(host=HOST, port=PORT)
    except Exception:
        print("Failed to connect to MQTT broker")
        exit(1)


    # Main loop
    try:
        menu(client)
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("\nGoodbye")
        client.disconnect()
        exit(1)
