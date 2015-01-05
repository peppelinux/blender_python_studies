#!/bin/bash

set -x 

/bin/ps -ax | grep blender

/bin/kill -TERM $(pidof blender)

printf "\n\nTerminato $(date)\n\n" >> log_GPU.txt
printf "\n\nTerminato $(date)\n\n" >> log_CPU.txt

#sleep 5
read ciao
