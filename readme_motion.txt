Create script looking for ESSID and switching to it if available.

Motion station shall choose between router and AP.Router has priority 1.

Backup station shall check for ESSID periodically while being in AP mode and
switch to ESSID if available. If no ESSID for N number of checks,switch to AP.

Cron jobs motion station:
- delete stored files to keep X% disk space
- rsync to backup station
- reconnect to available WLAN network prioritized for router

- motion .deb installed uinit.d script, needed to be activated
- motion deamon should have been activated according to manual

- using inotify tools for profiling file accesses 
- implement GPIO monitoring for safe shutdown
- backup image via dd
- rsync ssh id file sent to backup server for passwordless transfer
