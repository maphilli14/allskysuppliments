#!/usr/bin/python

import os, shutil, sys, subprocess,datetime,time

#user vars
qty=25
DIR='/home/pi/allsky/'

#clean up tempanim
try:
	shutil.rmtree(os.path.join(DIR,'TEMP'))
	os.mkdir(os.path.join(DIR,'TEMP'))
except:
	pass


def COPY():
	try:
		if len(os.listdir(os.path.join(DIR,'TEMP'))) > qty:
			print 'cleaning up olds'
			LIST= sorted(os.listdir(os.path.join(DIR,'TEMP')))
			for position, item in enumerate(LIST):
				if item == 'CURRENTANI.gif':
					LIST.pop(position)
			os.remove(os.path.join(DIR,'TEMP',LIST[0]))
		else:
			print 'taking new photos'
			pass
	except:
               	print 'PROBLEM'
                e = sys.exc_info()
                print e
                print
                pass
	try:
		print 'Copying latest '
		TIME=str(datetime.datetime.now().time())[0:8].replace(':','')
		shutil.copy(os.path.join(DIR+'liveview-image.jpg'),os.path.join(DIR,'TEMP','image-'+TIME+'.jpg'))
		print
		print 'File '+TIME+' copied'
		print
	except:
		print 'Files NOT copied'
          	e = sys.exc_info()
          	print e
		print
		pass

def GIFMAKER():
	try:
		subprocess.Popen(['/Scripts/makegifdaynight.sh'])
          	e = sys.exc_info()
          	print e
	except:
		print 'couldn\'t make new gif'
          	e = sys.exc_info()
		print e
		pass

while True:
	COPY()
	time.sleep(60)
	GIFMAKER()
