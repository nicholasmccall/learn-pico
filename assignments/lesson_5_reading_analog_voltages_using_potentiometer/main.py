import machine
from time import sleep

POTENTIOMETER_PIN = 28

potentiometer = machine.ADC(POTENTIOMETER_PIN)

while True:
    potentiometer_value = potentiometer.read_u16()
    volts = potentiometer_value * (3.3/65535)
    print("Volts: ", volts)
    sleep(0.5)