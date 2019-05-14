#!/usr/bin/env python
import psutil
perc=int(psutil.virtual_memory().percent)
print('<span font="Font Awesome">\uf2db</span>{:>3}%'.format(perc))
