#!/usr/bin/env python3

import time
import locale

currentDate = time.strftime('%a, %b %d')
currentTime = time.strftime('%H:%M:%S')
pattern ='<span font="Font Awesome">\uf073</span> {} <span font="Font Awesome">\uf017</span> {}'

print(pattern.format(currentDate, currentTime))
