#!/usr/bin/env python
# This is the cpu temperature path on my laptop, change it properly
#######################################################
cpuTempPath = '/sys/class/thermal/thermal_zone1/temp' #
#######################################################
file=open(cpuTempPath)
temp = int(int(file.read())/1000);
file.close()
def color(temp):
	if temp < 50:
		return "#00FF00"
	if temp < 55:
		return "#bfff00"
	if temp < 60:
		return "#ffff00"
	if temp < 65:
		return "#ffbf00"
	if temp < 70:
		return "#ff8000"
	return "#ff0000"
def icon(temp):
	if temp < 50:
		return "\uf2cb"
	if temp < 55:
		return "\uf2ca"
	if temp < 60:
		return "\uf2c9"
	if temp < 65:
		return "\uf2c8"
	return "\uf2c7"

print('<span color="{}"><span font="FontAwesome">{}</span> {:>2}ºC</span>'.format(color(temp), icon(temp), temp))
