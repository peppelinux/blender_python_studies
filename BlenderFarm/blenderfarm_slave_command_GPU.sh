#!/bin/bash

set -x 

export BLENDER_EXE=~/Documenti/blender-2.72b-linux-glibc211-x86_64/blender

/usr/bin/nice -20 $BLENDER_EXE -P ./bfarm_cuda_settings.py -b ./slave_GPU.blend -a --addons netrender -noaudio -nojoystick > log_GPU.txt 2>&1 
