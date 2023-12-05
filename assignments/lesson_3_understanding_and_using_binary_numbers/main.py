from machine import Pin
from time import sleep
from random import randint

def calculate_binary_state(number: int, ones_pin: Pin, twos_pin: Pin, fours_pin: Pin, eights_pin: Pin) -> None:
    """
    Given a number 0-15 and four Pins, toggles the indicator pins
    on and off to represent the number as a binary value
    """
    # Start by turning all the pins off
    ones_pin.off()
    twos_pin.off()
    fours_pin.off()
    eights_pin.off()

    # If the number is isn't between 0 and 15 we can't represent it
    if number < 0 or number > 15:
        print("Number can't be represented with 4 binary values")
        return
    
    # Let's create a dictionary to associate our pins with their corresponding numbers
    led_values = {
        8: eights_pin,
        4: fours_pin,
        2: twos_pin,
        1: ones_pin
    }

    # Beginning with our largest available value, begin subtracting the value and toggling pins
    current_value = number

    for number, pin in led_values.items():
        if current_value >= number:
            pin.on()
            current_value -= number
        
        if current_value == 0: break
    


def main_routine():
    print("Initiating Main")
    
    ONE_PIN = Pin(15, Pin.OUT)
    TWO_PIN = Pin(14, Pin.OUT)
    FOUR_PIN = Pin(27, Pin.OUT)
    EIGHT_PIN = Pin(28, Pin.OUT)

    while True:

        # Get a random number between 0 and 15
        random_number = randint(0, 15)

        # Let the user know what number we are representing with our LEDs
        print("New random number selected: " + str(random_number))

        # Adjust our leds to represent the number
        calculate_binary_state(random_number, ONE_PIN, TWO_PIN, FOUR_PIN, EIGHT_PIN)

        # Sleep for 5 seconds to enjoy our efforts :D
        sleep(5)


if __name__ == "__main__":
    main_routine()