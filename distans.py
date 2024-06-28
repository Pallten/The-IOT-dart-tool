from machine import Pin, time_pulse_us
import time

# LED setup
green_led = Pin(16, Pin.OUT)  # Green LED connected to GPIO 15
yellow_led = Pin(17, Pin.OUT)  # Yellow LED connected to GPIO 14
red_led = Pin(14, Pin.OUT)  # Red LED connected to GPIO 13

# Constants for distance measurement
SOUND_SPEED = 340  # Speed of sound in m/s
TRIG_PULSE_DURATION_US = 10  # Duration of trigger pulse in microseconds

# Pin setup for ultrasonic sensor
trigPin = Pin(26, Pin.OUT)
echoPin = Pin(27, Pin.IN)

# Initialize pins
trigPin.value(0)
time.sleep_us(5)  # Wait for sensors to settle

def measure_distance():

     
    trigPin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trigPin.value(0)

    ultrason_duration = time_pulse_us(echoPin, 1, 30000)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000
    
        # LED logic based on distance
    if 238 <= distance_cm <= 246:
        green_led.on()
        yellow_led.off()
        red_led.off()
    elif 230 <= distance_cm < 238 or 246 < distance_cm <= 254:
        green_led.on()
        yellow_led.on()
        red_led.off()
    elif 210 <= distance_cm < 230 or 254 < distance_cm <= 274:
        green_led.off()
        yellow_led.on()
        red_led.off()
    else:
        green_led.off()
        yellow_led.off()
        red_led.on()
        
        
    return distance_cm
