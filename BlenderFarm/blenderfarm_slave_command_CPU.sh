#!/bin/bash

export BLENDER_EXE=~/Documenti/blender-2.72b-linux-glibc211-x86_64/blender

/usr/bin/nice -20 $BLENDER_EXE -b ./slave_CPU.blend -a --addons netrender -noaudio -nojoystick > log_CPU.txt 2>&1 
