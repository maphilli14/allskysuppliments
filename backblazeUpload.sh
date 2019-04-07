#!/bin/bash

/usr/local/bin/rclone copy /home/pi/allsky/liveview-image.jpg b:allsky >/dev/null 2>&1
/usr/local/bin/rclone copy /home/pi/allsky/TEMP/CURRENTANI.gif b:allsky >/dev/null 2>&1
