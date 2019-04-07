#!/bin/sh

/usr/bin/ffmpeg -framerate 20 -pattern_type glob -i \'/Lexar/allsky/images/TEMP/*.jpg\' /Lexar/allsky/images/TEMP/CURRENTANI.gif
