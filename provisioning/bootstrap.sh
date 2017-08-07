#!/usr/bin/env bash

sudo add-apt-repository ppa:fkrull/deadsnakes -y
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3.5 -y
# Required dependencies
sudo apt-get install build-essential -y
sudo apt-get install cmake -y
sudo apt-get install git -y
sudo apt-get install libgtk2.0-dev -y
sudo apt-get install pkg-config -y
sudo apt-get install libavcodec-dev -y
sudo apt-get install libavformat-dev -y
sudo apt-get install libswscale-dev -y
# If you use a non-system copy of Python (eg. with pyenv or virtualenv), then you probably don't need to do this part
sudo apt-get install python3.5-dev -y
sudo apt-get install libpython3-dev -y
sudo apt-get install python3-numpy -y
# Optional, but installing these will ensure you have the latest versions compiled with OpenCV
sudo apt install libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev
libdc1394-22-dev
