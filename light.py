from machine import ADC, Pin
import time

# Function to measure light levels
def measure_light():
    ldr = ADC(Pin(28))
    light_value = ldr.read_u16()
    darknessPercentage = round(light_value / 65535 * 100, 2)
    light = 100 - darknessPercentage
    return light
