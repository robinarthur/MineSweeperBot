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
sudo apt-get install libtbb2 -y
sudo apt-get install libtbb-dev -y
sudo apt-get install libjpeg-dev -y
sudo apt-get install libpng-dev -y
sudo apt-get install libtiff-dev -y
sudo apt-get install ibjasper-dev -y
sudo apt-get install ibdc1394-22-dev -y

# Clone OpenCV somewhere
# I'll put it into $HOME/code/opencv
OPENCV_DIR="$HOME/code/opencv"
OPENCV_VER="3.1.0"
git clone https://github.com/opencv/opencv "$OPENCV_DIR"
# This'll take a while...

# Now lets checkout the specific version we want
cd "$OPENCV_DIR"
git checkout "$OPENCV_VER"

# First OpenCV will generate the files needed to do the actual build.
# We'll put them in an output directory, in this case "release"
mkdir release
cd release

# Note: This is where you'd add build options, like TBB support or custom Python versions. See above sections.
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local "$OPENCV_DIR" \
-D PYTHON_DEFAULT_EXECUTABLE=$HOME/.pyenv/versions/3.5.2/bin/python3.5 \
-D PYTHON_INCLUDE_DIRS=$HOME/.pyenv/versions/3.5.2/include/python3.5m \
-D PYTHON_EXECUTABLE=$HOME/.pyenv/versions/3.5.2/bin/python3.5 \
-D PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.5m.so.1 ..

# At this point, take a look at the console output.
# OpenCV will print a report of modules and features that it can and can't support based on your system and installed libraries.
# The key here is to make sure it's not missing anything you'll need!
# If something's missing, then you'll need to install those dependencies and rerun the cmake command.

# OK, lets actually build this thing!
# Note: You can use the "make -jN" command, which will run N parallel jobs to speed up your build. Set N to whatever your machine can handle (usually <= the number of concurrent threads your CPU can run).
make
# This will also take a while...

# Now install the binaries!
sudo make install
