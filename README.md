# i3blocks scripts
Those are just a bunch of Python 3 scripts that I'm currently using on my laptop to replace i3blocks default ones. Feel free to use them, fork the project, ask something or submit some bugfixes.

As you can see, those scripts doesn't support a wide variety of hardware, and thats because it has only been tested on one laptop. If you want to use them, you'll probably need to modify some variable values on the first lines of each script as explained bellow.

I'll try to provide a more user friendly way to configure those scripts but I don't promise that it will be soon.

**Note: these scripts work for a Dell XPS 15 running Ubuntu 19+**

## i3blocks config file

Its just the default config file modified to use those scripts, don't forget to change properly the paths of every script if you use a diferent one. You can notice that there is a route to a battery script on this file, thats because i use a fork of rfx0 project which can be found on this repo too named as i3blocks-battery.

## network.py

This script uses the output of a couple of iproute2 and netctl commands to display if you are connected to a wired or wireless network aswell as your ip and ssid and wifi signal strength if needed.
To make it work on your computer you may need to change the device names on the first two lines of the script as you have configured it on udev rules during installation (if you are running arch like me), or if you are running a more user friendly distro you can just check what has your OS configured with a command like 'ip link'.

## cpu.py
This is a really tiny script cause it uses psutil lib (which you may need to install whith 'pip3 install psutil') and formats its output to be consisten with my others sripts aspect.

## cputemp.py
This script does only read a system file which provides the current cpu temp and formats its output making it display a color and icon depending on current temp. You may need to change the route of the file that it reads depending on your laptop manufacturer and model.

## mem.py
As cpu script this one also uses psutil lib and format its output properly to show current ram percent usage. Check how to install psutil on cpu.py section if needed.

## brightness.py
As the cputemp file this script just reads a couple of system files, change it's paths properly if needed.

## volume.py

This script uses amixer to display headphones or speaker volume aswell as if those are muted. I use alsa and pulseaudio and i'm not sure if it will work without pulse or will have troubles with jack. Again, as i've said, i don't have a wide variety of computers to test it properly.
