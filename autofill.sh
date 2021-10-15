#!/bin/sh
pkill -f "Xvfb :99"
Xvfb :99 -screen 0 1280x720x16 &
export DISPLAY=:99
python3 ./main.py