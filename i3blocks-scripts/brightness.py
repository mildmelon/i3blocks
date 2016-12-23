#!/bin/python
# Those are the brightness paths on my laptop, change it properly
######################################################################
brighPath = '/sys/class/backlight/intel_backlight/actual_brightness' #
maxBrighPath = '/sys/class/backlight/intel_backlight/max_brightness' #
######################################################################

file=open(brighPath)
brightness = int(file.read());
file.close()
maxBrighPath = '/sys/class/backlight/intel_backlight/max_brightness'
file=open(maxBrighPath)
maxBrightness = int(file.read())
file.close()
perc = int(brightness * 100 / maxBrightness)
print('<span font="FontAwesome">\uf185</span>{:>3}%'.format(perc))
