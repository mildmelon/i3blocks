#!/usr/bin/env python
# Config proper device names
###########################
wirelessDevice = 'wifi0'  #
ethernetDevice = 'net0'   #
###########################
from subprocess import check_output
file=open('/sys/class/net/wifi0/operstate')
wifiState = file.read().split('\n')[0];
file.close()
file=open('/sys/class/net/net0/operstate')
ethState = file.read().split('\n')[0];
file.close()
# If wifi is up we get its ip and ssid
if wifiState == 'up':
   aux = check_output(['ip', 'addr', 'show', wirelessDevice], universal_newlines=True).split('\n')
   wifiIp = '&lt;uncknown ip&gt;'
   for line in aux:
      if line.find('inet ') != -1:
         wifiIp = line.split('inet ')[1].split('/')[0]
   aux = check_output(['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'], universal_newlines=True).split('\n')
   wifiSsid = '&lt;uncknown ssid&gt;'
   for line in aux:
      if line.find('sí') != -1:
         wifiSsid = line.split(':')[1]
   aux = check_output(['nmcli', '-t', '-f', 'active,signal', 'dev', 'wifi'], universal_newlines=True).split('\n') 
   for line in aux:
      if line.find('sí') != -1:
         wifiSignal = int(line.split(':')[1])
# If eth link is up we get its ip
if ethState == 'up':
   aux = check_output(['ip', 'addr', 'show', ethernetDevice], universal_newlines=True).split('\n')
   for line in aux:
      if line.find('inet') != -1:
         ethIp = line.split('inet ')[1].split('/')[0]
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
   output = '<span color="red"><span font="FontAwesome">\uf00d</span>NOT CONNECTED</span>'
if wifiState == 'up':
   output += '<span font="FontAwesome">\uf1eb</span> {} (<span color="{}">{}%</span>) {}'.format(wifiSsid, color(wifiSignal), wifiSignal, wifiIp)
if ethState == 'up':
   output += '<span font="FontAwesome">\uf0ec</span> {}'.format(ethIp)

print(output)
