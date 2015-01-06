#!/bin/bash

# change it if you're using a static compilation or not
#export BLENDER_EXE=~/Documenti/blender-2.72b-linux-glibc211-x86_64/blender
export  BLENDER_EXE=/usr/bin/blender

# if you want a UI blender remove -b option and add this:
#--window-geometry 0 0 320 200

/usr/bin/nice -20 $BLENDER_EXE -b ./blends/slave_CPU.blend -P ./conf/slave_master_address.py -a --addons netrender  -noaudio -nojoystick > logs/log_CPU.txt 2>&1 

