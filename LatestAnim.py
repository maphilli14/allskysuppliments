#!/usr/bin/python

import os, shutil, sys, subprocess

#user vars
qty=25
DIR='/Lexar/allsky/images'

try:
	TODAY=os.listdir(DIR)[-1]
	TODAYsFiles=os.listdir(os.path.join(DIR,TODAY))
	LATEST=sorted(TODAYsFiles)[-qty:]
	#remove thumbnails
	LATEST.pop(-1)
except:
	pass

def COPY():
	try:
		print 'Removing old TEMPs from '+os.path.join(DIR)
		shutil.rmtree(os.path.join(DIR,'TEMP'))
        except:
                e = sys.exc_info()
                print e
		print
                pass
	try:
		print 'Creating new TEMP folder'
		os.mkdir(os.path.join(DIR,'TEMP'))
        except:
                e = sys.exc_info()
                print e
		print
                pass
	try:
		print 'Copying latest '+str(qty)+' from '+TODAY
		for F in LATEST:
			if 'jpg' in F:
				print F
				shutil.copy(os.path.join(DIR,TODAY,F),os.path.join(DIR,'TEMP',F))
			else:
				pass
		print
		print 'Files copied'
		print
	except:
		print 'Files NOT copied'
          	e = sys.exc_info()
          	print e
		print
		pass

def GIFMAKER():
	try:
		subprocess.Popen(['/Lexar/Scripts/makegif.sh'])
          	e = sys.exc_info()
          	print e
	except:
		print 'couldn\'t make new gif, perhaps daytime?'
          	e = sys.exc_info()
		print e
		pass

COPY()
GIFMAKER()
