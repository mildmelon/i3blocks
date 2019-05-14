#!/usr/bin/env python3

# Constants for tempature (in celsius)
COOL = 45
WARM = 55
HOT  = 65
HELL = 75
STOP = 90

# This is the cpu temperature path on my laptop, change it properly
cpu_temp_path = '/sys/class/thermal/thermal_zone1/temp'


with open(cpu_temp_path) as file:
    temp = int(file.read()) / 1000;

def color(temp):
	if temp <= COOL:
		return "#00FF00"
	if temp <= WARM:
		return "#bfff00"
	if temp <= HOT:
		return "#ffff00"
	if temp <= HELL:
		return "#ffbf00"
	if temp <= STOP:
		return "#ff8000"
	return "#ff0000"

def icon(temp):
	if temp <= COOL:
		return "\uf2cb"
	if temp <= WARM:
		return "\uf2ca"
	if temp <= HOT:
		return "\uf2c9"
	if temp <= HELL:
		return "\uf2c8"
	return "\uf2c7"

print(f'<span color="{color(temp)}"><span font="FontAwesome">{icon(temp)}</span> {str(temp).zfill(2)}ºC</span>')
