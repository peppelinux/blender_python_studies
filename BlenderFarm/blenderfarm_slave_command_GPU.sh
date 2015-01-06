#!/bin/bash

set -x 

#export BLENDER_EXE=~/Documenti/blender-2.72b-linux-glibc211-x86_64/blender
export  BLENDER_EXE=/usr/bin/blender

/usr/bin/nice -20 $BLENDER_EXE   -b ./blends/slave_GPU.blend -P ./conf/slave_master_address.py  -P ./python/bfarm_cuda_settings.py -a --addons netrender -noaudio -nojoystick > ./logs/log_GPU.txt 2>&1 
