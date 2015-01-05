#!/bin/bash

set -x 

#export BLENDER_EXE=~/Documenti/blender-2.72b-linux-glibc211-x86_64/blender
export  BLENDER_EXE=/usr/bin/blender

/usr/bin/nice -20 $BLENDER_EXE -P ./python/bfarm_cuda_settings.py -b ./blends/slave_GPU.blend -a --addons netrender -noaudio -nojoystick > ./logs/log_GPU.txt 2>&1 
