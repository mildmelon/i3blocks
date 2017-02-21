#!/usr/bin/env python
# Custom i3blocks python script for displaying volume, mute status
# and if headphones are plugged with a FontAwesome icon and a 
# volume percentage using amixer
from subprocess import check_output
import re
# Get amixer output 
aux = check_output(['amixer', 'get', 'Master'], universal_newlines=True)
output = re.search('Front Left:[A-z,0-9,\s]*\[([0-9]*)%\] \[([a-z]*)\]\n\s*Front Right:[A-z,0-9,\s]*\[([0-9]*)%\] \[([a-z]*)\]', aux)
# Set default values in case of something fails
leftStatus = 'on'
rightStatus = 'on'
leftVol = 33
rightVol = 33
# Get volumes and status of speakers from amixer output with regexps
if output:
   leftStatus = output.group(2)
   rightStatus = output.group(4)
   leftVol = int(output.group(1))
   rightVol = int(output.group(3))

# Regexp that returns if headphones are plugged
aux = check_output(['amixer', '-c', '0', 'contents'], universal_newlines=True)
headphones = re.search('numid=19.*\n.*\n\s*\:\svalues=(.*)', aux).group(1)
#Calculate average volume of right and left speakers
vol = int((leftVol + rightVol) / 2)

# Defines status as muted, headphones plugged or normal status
if (leftStatus == 'off') & (rightStatus == 'off'):
   mute = 'on'
else:
   mute = 'off'
if headphones == 'on':
   device = 'headphones'
else:
   device='speakers'

# Returns propper FontAwesome icon depending on current status
def icon(device):
   if device == 'speakers':
      return '\uf028'
   if device == 'headphones':
      return '\uf025'
   return '\uf128'
def color(mute):
   if mute == 'on':
      return '#FF0000'
   else:
      return '#FFFFFF'


print('<span font="FontAwesome" color="{}">{}</span>{:>3}%'.format(color(mute), icon(device), vol))