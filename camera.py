#!/usr/bin/env python
import subprocess

count=input('Enter the number of counts:')
count=int(count)
i=0
while(i<count):
    subprocess.call(['/home/pi/camera.sh'])
    i+=1
