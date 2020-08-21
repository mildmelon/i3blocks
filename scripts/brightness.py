#!/bin/python
# Custom i3blocks python script for displaying current screen brightness
#
# Those are the brightness paths on my laptop, change it properly

import math

# Edit these to match the paths on your machine
bright_path = '/sys/class/backlight/intel_backlight/actual_brightness'
max_bright_path = '/sys/class/backlight/intel_backlight/max_brightness'

# You can see the icon here: https://fontawesome.com/icons/sun?style=solid
icon = '<span font="FontAwesome">\uf185</span>'


with open(bright_path) as file:
    brightness = int(file.read())

with open(max_bright_path) as file:
    max_brightness = int(file.read())

brightness_perc = math.ceil(brightness * 100 / max_brightness)
print(f'{icon}{brightness_perc:>3}%')
