import paho.mqtt.client as mqtt
from constants import USERNAME, PASSWORD, TOPIC, HOST, PORT


def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode("utf-8")))
    if message.payload.decode("utf-8") == "ON":
        turn_on()
    elif message.payload.decode("utf-8") == "OFF":
        turn_off()

def turn_on():
    light = """
      \\ \\ _ / /
       \ / \\ /
     -- /   \\ --
     -- |    | --
        \\   /
         \\_/ 
         |_|
    """

    print(light)

def turn_off():
    light = """
          _
         / \\
        /   \\
        |    |
        \\   /
         \\_/ 
         |_|
    """

    print(light)


if __name__ == "__main__":
    # MQTT Connection 
    try:
        client = mqtt.Client()
        client.username_pw_set(username=USERNAME, password=PASSWORD)
        client.connect(host=HOST, port=PORT)
        client.on_message = on_message
        client.subscribe(TOPIC)
    except Exception:
        print("Failed to connect to MQTT broker")
        exit(1)
    
    print("Connected")

    try:
        client.loop_forever()
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("\nDisconnected")
        client.disconnect()
        exit(1)
