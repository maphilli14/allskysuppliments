#!/bin/sh

ffmpeg -framerate 20 -pattern_type glob -i '/home/pi/allsky/TEMP/*.jpg' /home/pi/allsky/TEMP/CURRENTANI2.gif
cp -f /home/pi/allsky/TEMP/CURRENTANI2.gif /home/pi/allsky/images/CURRENTANI.gif
cp -f /home/pi/allsky/liveview-image.jpg /home/pi/allsky/images/liveview-image.jpg
mv -f /home/pi/allsky/TEMP/CURRENTANI2.gif /home/pi/allsky/TEMP/CURRENTANI.gif
