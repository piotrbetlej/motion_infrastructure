import subprocess
import time

def get_current_profile(filePath="/lib/init/rw/",fileName="configured_interface"):
	networkName = ""
	try:
		file = open(filePath+fileName,"r")
		line = file.readline()
		networkName=line.rstrip()
		file.close()
	except Exception as e:
		# print "Exception",e
		pass
	finally:
		return networkName

def switch_profile(profile,debug=None):
	process = subprocess.Popen('/sbin/ifdown wlan0', shell=True, stdout=subprocess.PIPE, 
						stderr=subprocess.STDOUT)
	process.wait()
	str = process.communicate()[0]
	
	if debug is not None:
		print str
		
	process = subprocess.Popen('/sbin/ifup wlan0='+profile, shell=True, stdout=subprocess.PIPE, 
						stderr=subprocess.STDOUT)
	process.wait()
	str = process.communicate()[0]

	if debug is not None:
		print str


def check_essid(iDs, retriesNum, retriesSleep, debug=None):
	for x in range(0, retriesNum):
		process = subprocess.Popen('/sbin/iwlist scan', shell=True, stdout=subprocess.PIPE, 
						stderr=subprocess.STDOUT)
		process.wait()
		str = process.communicate()[0]

		if str.find('busy') == -1:
			break
		if debug is not None:
			print 'Was busy...'
			print time.time()

		time.sleep(retriesSleep)

		if x == retriesNum - 1 and debug is not None:
			print 'Finally failed'
			continue

	if debug is not None:
		print 'Raw listing: ',str
	#if debug is not None:
	#	print wlanId,' :','First character number: ',str.find(wlanId)
	#	print apId,' :','First character number: ',str.find(apId)

	ret = {}

	for id in iDs:
		if str.find(id) == -1:
			ret[id] = False
		else:
			ret[id] = True
	return ret
