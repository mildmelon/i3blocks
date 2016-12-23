#!/usr/bin/env python
import time
import locale
locale.setlocale(locale.LC_TIME, 'es_ES')
currentDate = time.strftime('%a %d de %b')
currentTime = time.strftime('%H:%M')
pattern ='<span font="Font Awesome">\uf073</span> {} <span font="Font Awesome">\uf017</span> {}'
print(pattern.format(currentDate, currentTime))