import network
import urequests as requests
import machine
from time import sleep
import distans  # Import the distans file
import light    # Import the light file 
import keys     # Import the keys module (containing token, device_label, VARIABLE_LABELs, WIFI_SSID AND WIFI_PASS)
import wifiConnection  # Import the wifiConnection module

DELAY = 1  # Delay in seconds between data sends
MEASUREMENT_INTERVAL = 0.5  # Interval in seconds between individual measurements
NUM_MEASUREMENTS = 5  # Number of measurements to take for computing the median

def build_json(variable_label, value):
    """
    Build JSON data structure for sending to Ubidots.

    Args:
    - variable_label: Label of the variable being sent (e.g., "distance", "light").
    - value: Value of the variable being sent.

    Returns:
    - JSON data structure ready to be sent.
    """
    try:
        data = {variable_label: {"value": value}}
        return data
    except Exception as e:
        print("Exception in build_json:", e)
        return None

def sendData(device_label, variable_label, value):
    """
    Send data to Ubidots API.

    Args:
    - device_label: Label of the device in Ubidots.
    - variable_label: Label of the variable being sent (e.g., "distance", "light").
    - value: Value of the variable being sent.

    Returns:
    - JSON response from the server, or None if there's an error.
    """
    try:
        # Construct URL for Ubidots API
        url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{device_label}"
        headers = {"X-Auth-Token": keys.TOKEN, "Content-Type": "application/json"}
        data = build_json(variable_label, value)

        if data is not None:
            print("Sending data:", data)
            # Send POST request to Ubidots API
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()  # Return JSON response from Ubidots
        else:
            print("Data is None, not sending.")
            return None
    except Exception as e:
        print("Exception in sendData:", e)
        return None

def calculate_median(data):
    """
    Calculate the median of a list of numbers.

    Args:
    - data: List of numbers.

    Returns:
    - Median value.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median = sorted_data[mid]

    return median

def measure_median_distance():
    
    """
    Measure distance multiple times and return the median value.

    Returns:
    - Median distance in centimeters.
    """
    measurements = []
    for _ in range(NUM_MEASUREMENTS):
        distance = distans.measure_distance()
        print(distance)
        measurements.append(distance)
        sleep(MEASUREMENT_INTERVAL)
    return calculate_median(measurements)


# WiFi connection
wifiConnection.connect()  # Connect to WiFi using credentials in wifiConnection module

# Main loop for sending data to Ubidots
try:
    while True:
        # Measure distance and send data
        distanceSend = measure_median_distance()  # Measure and get median distance
        returnValue_distance = sendData(keys.DEVICE_LABEL, keys.VARIABLE_LABEL_1, distanceSend)
        
        # Measure light and send data
        lightSend = light.measure_light()  # Call the function from light.py
        returnValue_light = sendData(keys.DEVICE_LABEL, "light", lightSend) 

        sleep(DELAY)  # Wait for DELAY seconds before next iteration

except KeyboardInterrupt:
    print("Program interrupted by user.")
except Exception as e:
    print("Exception in main loop:", e)

# WiFi disconnection
wifiConnection.disconnect()  # Disconnect from WiFi
