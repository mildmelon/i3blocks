#!/usr/bin/env python3

import psutil

print(f'<span font="Font Awesome">\uf2db</span> {int(psutil.cpu_percent(interval=1))}%')
