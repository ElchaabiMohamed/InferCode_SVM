import subprocess
pl = subprocess.Popen(['kill','-SIGKILL' '816'], stdout=subprocess.PIPE).communicate()[0]
print (pl)