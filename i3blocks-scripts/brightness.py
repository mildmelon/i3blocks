#!/bin/python
# Those are the brightness paths on my laptop, change it properly
######################################################################
brighPath = '/sys/class/backlight/intel_backlight/actual_brightness' #
maxBrighPath = '/sys/class/backlight/intel_backlight/max_brightness' #
######################################################################
import math
file=open(brighPath)
brightness = int(file.read());
file.close()
file=open(maxBrighPath)
maxBrightness = int(file.read())
file.close()
brightnessPerc = math.ceil(brightness * 100 / maxBrightness)
print('<span font="FontAwesome">\uf185</span>{:>3}%'.format(brightnessPerc))
