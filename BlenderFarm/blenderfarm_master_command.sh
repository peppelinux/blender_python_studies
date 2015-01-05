#!/bin/bash

#export BLENDER_EXE=~/Documenti/blender-2.72b-linux-glibc211-x86_64/blender
export  BLENDER_EXE=/usr/bin/blender

/usr/bin/nice -20 $BLENDER_EXE -b ./blends/master.blend -a --addons netrender -noaudio -nojoystick > logs/log_master.txt 2>&1 
