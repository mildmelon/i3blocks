#!/usr/bin/env python
# Custom i3blocks python script for displaying volume, mute status
# and if headphones are plugged with a FontAwesome icon and a 
# volume percentage using amixer
from subprocess import check_output
# Get amixer output 
output = check_output(['amixer', 'get', 'Master'], universal_newlines=True).split('\n')
# Set default values in case of something fails
leftStatus = 'on'
rightStatus = 'on'
leftVol = 33
rightVol = 33
# Get volumes and status of speakers from amixer output
for line in output:
   if line.find('Front Left:') != -1:
      leftStatus = line.split('[')[2].split(']')[0]
      leftVol = int(line.split('[')[1].split('%')[0])
   if line.find('Front Right:') != -1:
      rightStatus = line.split('[')[2].split(']')[0]
      rightVol = int(line.split('[')[1].split('%')[0])
# Ugly way of knowing if headphones are plugged
# (yup, i hate regexp)
headphones = check_output(['amixer', '-c', '0', 'contents'], universal_newlines=True).split('numid=19')[1].split('\n')[2].split('=')[1]

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