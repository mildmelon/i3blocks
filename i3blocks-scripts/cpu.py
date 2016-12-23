#!/usr/bin/env python
import psutil
perc=int(psutil.cpu_percent(interval=1))
print('<span font="Font Awesome">\uf0ae</span>{:>3}%'.format(perc))
