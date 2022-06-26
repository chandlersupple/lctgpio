# Imports
import os

# Maps pin numbers to Linux pin
pin_map = {
    3: 12,
    5: 11,
    7: 2,
    8: 198,
    10: 199,
    11: 1, 12: 203,
    13: 0,
    15: 3,
    16: 201,
    18: 200,
    19: 64,
    21: 65,
    22: 14,
    23: 66,
    24: 67,
    26: 17,
    27: 19,
    28: 18,
    29: 20,
    31: 21,
    32: 13,
    33: 6,
    34: 15,
    35: 202,
    37: 16,
    38: 205,
    40: 204,
}


def close_pin(pin_number):
    """Closes the specified pin number.
        :param pin_number: Pin number specified by Libre Computer diagram.
        :type pin_number: int
        :rtype None
    """
    result = os.popen(f'echo {pin_map[pin_number]} | sudo tee > /sys/class/gpio/unexport')

    if result and 'Permission denied' in result:
        return Exception('Error: Permission denied')


def open_pin(pin_number):
    """Opens the specified pin number.
        :param pin_number: Pin number specified by Libre Computer diagram.
        :type pin_number: int
        :rtype None
    """
    result = os.popen(f'echo {pin_map[pin_number]} | sudo tee > /sys/class/gpio/export').read()

    if result:
        if 'Permission denied' in result:
            return Exception('Error: Permission denied')
        else:
            close_pin(pin_number)
            open_pin(pin_number)


def set_input(pin_number):
    """Sets pin as input.
        :param pin_number: Pin number specified by Libre Computer diagram.
        :type pin_number: int
        :rtype None
    """
    result = os.popen(f'echo in | sudo tee > /sys/class/gpio/gpio{pin_map[pin_number]}/direction')

    if result and 'Permission denied' in result:
        return Exception('Error: Permission denied')


def set_output(pin_number):
    """Sets pin as output.
        :param pin_number: Pin number specified by Libre Computer diagram.
        :type pin_number: int
        :rtype None
    """
    result = os.popen(f'echo out | sudo tee > /sys/class/gpio/gpio{pin_map[pin_number]}/direction')

    if result and 'Permission denied' in result:
        return Exception('Error: Permission denied')


def set_val(pin_number, val):
    """Sets the value of a pin.
        :param pin_number: Pin number specified by Libre Computer diagram.
        :type pin_number: int
        :param val: Desired value of the specified pin.
        :type val: int
        :rtype None
    """
    result = os.popen(f'echo {val} | sudo tee > /sys/class/gpio/gpio{pin_map[pin_number]}/value')

    if result and 'Permission denied' in result:
        return Exception('Error: Permission denied')


def get_val(pin_number):
    """Gets value of pin.
        :param pin_number: Pin number specified by Libre Computer diagram.
        :type pin_number: int
        :rtype None
    """
    result = os.popen(f'cat /sys/class/gpio/gpio{pin_map[pin_number]}/value')

    if result and 'Permission denied' in result:
        return Exception('Error: Permission denied')
