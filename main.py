import network
import urequests as requests
import machine
from time import sleep
import distans  # Import the distans file
import light    # Import the light file 
import keys     # Import the keys module (containing token, device_label, VARIABLE_LABELs, WIFI_SSID AND WIFI_PASS)
import wifiConnection  # Import the wifiConnection file


DELAY = 1  # Delay in seconds between data sends
MEASUREMENT_INTERVAL = 0.5  # Interval in seconds between individual measurements
NUM_MEASUREMENTS = 5  # Number of measurements to take for calculating the median

def measure_median_distance():
    
    measurements = []                               # Creates a empty list
    for _ in range(NUM_MEASUREMENTS):               # Loop to collect 5 measurements
        distance = distans.measure_distance()       # Call function in distans.py file and in it the measure_distance function
        print(distance)                             # Print distance to Shell for overview
        measurements.append(distance)               # Add the measured distance to the 'measurements' list
        sleep(MEASUREMENT_INTERVAL)                 # Sleep for 0.5s before running again
    return calculate_median(measurements)

def calculate_median(data):

    sorted_data = sorted(data)  # Sorting the data
    median = sorted_data[2]     # For a sorted list of 5 values, the median is always the third value (index 2) 0,1,*2*,3,4
    return median


# Builds the json to send the request
def build_json(variable_label, value):
                        
    try:
        data = {variable_label: {"value": value}}
        return data
    except Exception as e:
        print("Exception in build_json:", e)
        return None

def sendData(device_label, variable_label, value):

    try:
        # Construct URL for Ubidots API
        url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{device_label}"
        headers = {"X-Auth-Token": keys.TOKEN, "Content-Type": "application/json"}
        data = build_json(variable_label, value)

        if data is not None:
            print("Sending data:", data)
                                                                        # Send POST request to Ubidots API
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()  											# Return JSON response from Ubidots
        else:
            pass
    except:
        pass


# WIFI connection
wifiConnection.connect()  # Connect to WiFi using credentials in wifiConnection module

# Main loop for sending data to Ubidots
try:
    while True:
        # Measure distance and send data
        distanceSend = measure_median_distance()  													# Measure and get median distance
        returnValue_distance = sendData(keys.DEVICE_LABEL, keys.VARIABLE_LABEL_1, distanceSend)
        
        # Measure light and send data
        lightSend = light.measure_light()  # Call the function from light.py
        returnValue_light = sendData(keys.DEVICE_LABEL, keys.VARIABLE_LABEL_2, lightSend) 

        sleep(DELAY)  # Wait for DELAY seconds before next iteration

except KeyboardInterrupt:
    print("Program interrupted by user.")
except Exception as e:
    print("Exception in main loop:", e)

# WiFi disconnection
wifiConnection.disconnect()  # Disconnect from WiFi

