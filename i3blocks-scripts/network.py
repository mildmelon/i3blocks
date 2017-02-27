#!/usr/bin/env python
# Custom i3blocks python script for displaying network ip, ssid, and 
# wifi signal when connected to a network via ethernet or wifi
#
# Config proper device names
###########################
wirelessDevice = 'wifi0'  #
ethernetDevice = 'net0'   #
###########################
from subprocess import check_output
import re
file=open('/sys/class/net/' + wirelessDevice + '/operstate')
wifiState = file.read().split('\n')[0];
file.close()
file=open('/sys/class/net/' + ethernetDevice + '/operstate')
ethState = file.read().split('\n')[0];
file.close()
# If wifi is up we get its ip and ssid
if wifiState == 'up':
	aux = check_output(['ip', 'addr', 'show', wirelessDevice], universal_newlines=True)
	wifiIp = '&lt;uncknown ip&gt;'
	match = re.search(r'inet ([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)/', aux)
	if match:
		wifiIp = match.group(1);
	aux = check_output(['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'], universal_newlines=True)
	wifiSsid = '&lt;uncknown ssid&gt;'
	match = re.search('(sí|yes):(.*)', aux)
	if match:
		wifiSsid = match.group(2);
	aux = check_output(['nmcli', '-t', '-f', 'active,signal', 'dev', 'wifi'], universal_newlines=True)
	wifiSignal = 0
	match = re.search('(sí|yes):([0-9]*\n)', aux)
	if match:
		wifiSignal = int(match.group(2));
# If eth link is up we get its ip
if ethState == 'up':
	aux = check_output(['ip', 'addr', 'show', ethernetDevice], universal_newlines=True)
	match = re.search('inet ([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)/', aux)
	if match:
		ethIp = match.group(1);
output=''
def color(percent):
	if percent < 10:
		return "#FFFFFF"
	if percent < 20:
		return "#FF0000"
	if percent < 30:
		return "#FF3300"
	if percent < 40:
		return "#FF6600"
	if percent < 50:
		return "#FF9900"
	if percent < 60:
		return "#FFCC00"
	if percent < 70:
		return "#FFFF00"
	if percent < 80:
		return "#CCFF00"
	return "#00FF00"
if (wifiState == 'down') & (ethState == 'down'):
	output = '<span color="red"><span font="FontAwesome">\uf00d</span> NOT CONNECTED</span>'
if wifiState == 'up':
	output += '<span font="FontAwesome">\uf1eb</span> {} (<span color="{}">{}%</span>) {}'.format(wifiSsid, color(wifiSignal), wifiSignal, wifiIp)
if ethState == 'up':
	output += '<span font="FontAwesome">\uf0ec</span> {}'.format(ethIp)

print(output)