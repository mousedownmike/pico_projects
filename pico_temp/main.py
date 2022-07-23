# noinspection PyPackageRequirements
import machine
from machine import Pin
import time

led = Pin(25, Pin.OUT)
led_external = Pin(15, machine.Pin.OUT)
sensor_temp = machine.ADC(4)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
conversion_factor = 3.3 / 65535


def flash_temp(temp):
    count_left = temp / 10
    while count_left > 0:
        led_external(1)
        time.sleep_ms(500)
        led_external(0)
        time.sleep_ms(500)
        count_left = count_left - 1


while True:
    led_external(0)
    led(1)
    if button.value() == 1:
        led(0)
        reading = sensor_temp.read_u16() * conversion_factor
        celsius = 27 - (reading - 0.706)/0.001721
        fahrenheit = celsius * (9 / 5) + 32
        flash_temp(fahrenheit)
        led(1)
