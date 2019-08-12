#!/usr/bin/env python
''' 'PLEASE BE ROOT for the SCAPY library traceroutes!' This is the main file for finding addtional 
information about unpatched systems via networking tracing This script does NOT auto accept ssh keys and you 
may need to use this method:
 ~/.ssh/config
 Host *
    StrictHostKeyChecking no
per http://xmodulo.com/how-to-accept-ssh-host-keys-automatically-on-linux.html '''

import paramiko, sys, os, socket, time, sys, datetime, re, getpass, shutil, ephem

MAXTEMP=60
username='maphilli14'
ssopass='Dvacation'
HOST='kramer.sm.sm'
cr='\n'
#time in min used to delay power off = offset
offset=5
TIMEDELTA=datetime.timedelta(minutes=offset)
#Pi's Lat and Long
LAT='35'
LONG='-78'

o=ephem.Observer()
o.lat=LAT
o.long=LONG
s=ephem.Sun()
s.compute()
SUNSET=ephem.localtime(o.next_setting(s))
SUNSETHR=SUNSET.hour
SUNSETMIN=SUNSET.minute


def TimeCalc():
        global TIME,nHR,nMIN
        TIME=datetime.datetime.now()
        nHR=(TIME+TIMEDELTA).hour
        nMIN=(TIME+TIMEDELTA).minute
        return TIME,nHR,nMIN


def COMPARETEMP(MAXTEMP):
        READOUT = os.popen('vcgencmd measure_temp').readline()
        CPU=float(filter(str.isdigit, READOUT))/10
        print str(CPU)
        if CPU < MAXTEMP:
                print 'temp is ok'
        else:
                print 'TEMP IS HIGH, shutting down'
		TimeCalc()
		shell(HOST)
                os.popen('sudo halt')


#This cust def logs into the last hop device and pulls information
ToRemove=[]

def shell(host):
	global HOSTNAME,INT,INToutput
	remote_conn_pre=paramiko.SSHClient()
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(host, username=username, password=ssopass, look_for_keys=False, allow_agent=False)
	remote_conn = remote_conn_pre.invoke_shell()
	print
	time.sleep(1)
	remote_conn.send('term len 0'+cr)
	time.sleep(1)
	#Hostname
	try:
		remote_conn.send(cr+cr+cr)
		time.sleep(1)
		HOSTNAMEoutput=remote_conn.recv(5000)
		#uncomment next line for help finding index positions in output print HOSTNAMEoutput.split()
		HOSTNAME=str(HOSTNAMEoutput.split()[-1].strip('#'))
	except:
		HOSTNAME='This device did not respond to a hostname query'
		pass
	#Read Interface
	try:
		remote_conn.send('sh run int gi1/0/5'+cr)
		time.sleep(1)
		INToutput=remote_conn.recv(5000)
		#uncomment next line for help finding index positions in output print HOSTNAMEoutput.split()
		for i in INToutput.split('\r\n'):
			if 'energywise' in i:
				ToRemove.append(i)
			else:
				pass
	except:
		INT='This device did not respond to a INT query'
		pass
	#Unset interface command
	try:
		remote_conn.send('conf t'+cr)
		time.sleep(1)
		remote_conn.send('int gi1/0/5'+cr)
		time.sleep(1)
		for i in ToRemove:
			remote_conn.send('no '+i+cr)
			time.sleep(1)
		removeINToutput=remote_conn.recv(5000)
	except:
		pass
	print removeINToutput

        #Set interface command
        try:
                remote_conn.send('conf t'+cr)
                time.sleep(1)
                remote_conn.send('int gi1/0/5'+cr)
                time.sleep(1)
		remote_conn.send('energywise level 10 recurrence importance 90 at %d %d * * 1-7' % (SUNSETMIN, SUNSETHR)+cr)
		remote_conn.send('energywise level 0 recurrence importance 90 at %d %d * * 1-7' % (nMIN, nHR)+cr)
                time.sleep(1)
                setINToutput=remote_conn.recv(5000)
        except:
                pass
        print setINToutput

while True:
        COMPARETEMP(MAXTEMP)
        time.sleep(60)

