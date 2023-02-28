# IoT Light Control

## Description

This is a simple IoT project that allows the user to remotely control a light using an MQTT broker. The project consists of two Python scripts: `application.py` (which runs on the user's computer) and `thing.py` (which runs on the device that controls the light).

## How to Run

1. Clone the repository:

    ```console
    git clone <https://github.com/username/repository.git>
    ```

2. Navigate to the repository:

    ```console
    cd repository
    ```

3. Install the required Python packages:

    ```console
    pip install -r requirements.txt
    ```

4. Create the `constants.py` file with the following content:

    ```python
    USERNAME = "your_username"
    PASSWORD = "your_password"
    TOPIC = "your_topic"
    HOST = "your_host"
    PORT = your_port
    ```

    Replace the placeholders with your own values.

5. Run the `thing.py` script on the device that controls the light:

    ```console
    python3 thing.py
    ```

6. Run the `application.py` script on your computer:

    ```console
    python3 application.py
    ```

1. Follow the instructions in the terminal to turn the light on or off.

## `constants.py` Content

    ```python
    USERNAME = "your_username"
    PASSWORD = "your_password"
    TOPIC = "your_topic"
    HOST = "your_host"
    PORT = your_port
    ```

Replace the placeholders with your own values. The `USERNAME` and `PASSWORD` are the credentials for your MQTT broker. The `TOPIC` is the MQTT topic that the device and the application subscribe to. The `HOST` is the hostname of your MQTT broker. The `PORT` is the port number of your MQTT broker.