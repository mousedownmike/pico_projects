import machine
import time

led = machine.Pin(25, machine.Pin.OUT)
led_external = machine.Pin(15, machine.Pin.OUT)
sensor_temp = machine.ADC(4)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
conversion_factor = 3.3 / 65535


def flash_temp(temp):
    tens_left = temp / 10
    ones_left = temp % 10
    while tens_left > 0:
        led_external(1)
        time.sleep_ms(200)
        led_external(0)
        time.sleep_ms(200)
        tens_left = tens_left - 1
    led(1)
    time.sleep_ms(500)
    led(0)
    while ones_left > 0:
        led_external(1)
        time.sleep_ms(500)
        led_external(0)
        time.sleep_ms(500)
        ones_left = ones_left - 1


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
