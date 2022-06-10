import subprocess
pl = subprocess.Popen(['kill', '816'], stdout=subprocess.PIPE).communicate()[0]
print (pl)