import wlan_check

wlanId="Netxxx"
apId="hostapd1"
retriesNum=5
retriesSleep=1

apProfile="wlan_static"
wlanProfile="wlan_dynamic"

def reconnect():
# Check if prioritized ESSID present
	networks = {}
	networks=wlan_check.check_essid([wlanId,apId],retriesNum,retriesSleep,debug=None)
	storedProfileName=""
	storedProfileName=wlan_check.get_current_profile()
#	print storedProfileName
	
	# In case stored profile name is corrupted.
	if storedProfileName != wlanProfile and storedProfileName != apProfile:
		wlan_check.switch_profile(wlanProfile)
#		print "Switched to ESSID by default"

	# ESSID not present.
	if networks[wlanId] is False:
		# Check if switch to AP needed.
		if storedProfileName == wlanProfile:
			# Put interface down.
			# Connect to AP.
			wlan_check.switch_profile(apProfile)
#			print "ESSID switched"
	# ESSID present.
	if networks[wlanId] is True:
		# Check if switch to ESSID needed.
		if storedProfileName == apProfile:
			# Put interface down.
			# Connect to ESSID.
			wlan_check.switch_profile(wlanProfile)
#			print "AP switched"


if __name__=="__main__":
	# print wlan_check.check_essid([wlanId,apId,"FRITZ"],retriesNum,retriesSleep)
	# print wlan_check.get_current_profile()
	reconnect()
