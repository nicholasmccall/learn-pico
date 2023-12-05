from machine import Pin, ADC

GREEN_LED = Pin(13, Pin.OUT)
YELLOW_LED = Pin(14, Pin.OUT)
RED_LED = Pin(15, Pin.OUT)

POTENTIOMETER = ADC(28)

def calculate_power_percentage(analog_digital_converter: ADC) -> int:
    adc_max = 65535
    adc_min = 340
    adc_current_value = analog_digital_converter.read_u16()

    max_mapped_value = 100
    min_mapped_value = 0

    mapped_value = ((adc_current_value-adc_min)/(adc_max - adc_min)) * (max_mapped_value - min_mapped_value) + min_mapped_value

    mapped_value = round(mapped_value, 0)

    return int(mapped_value)

is_green_led_on = False
is_yellow_led_on = False
is_red_led_on = False
previous_power_percentage = 0

while True:
    
    power_percentage = calculate_power_percentage(POTENTIOMETER)
    print("Power Percentage: ", power_percentage)

    # Only print our change in power percentage when it's gone up by at least 1
    if abs(power_percentage - previous_power_percentage) >= 5:
        previous_power_percentage = power_percentage
        print("Power Percentage: ", power_percentage)

    if power_percentage <= 79 and not is_green_led_on:
        YELLOW_LED.off()
        is_yellow_led_on = False
        RED_LED.off()
        is_red_led_on = False
        GREEN_LED.on()
        is_green_led_on = True
        print("Power level is 79% or lower")

    if power_percentage >= 80 and power_percentage <= 94 and not is_yellow_led_on:
        GREEN_LED.off()
        is_green_led_on = False
        RED_LED.off()
        is_red_led_on = False
        YELLOW_LED.on()
        is_yellow_led_on = True
        print("Power level is above 80%")

    if power_percentage >= 95 and not is_red_led_on:
        GREEN_LED.off()
        is_green_led_on = False
        YELLOW_LED.off()
        is_yellow_led_on = False
        RED_LED.on()
        is_red_led_on = True
        print("Power level dangerously close to 100")