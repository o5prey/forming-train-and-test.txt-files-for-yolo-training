import shutil
import os
import time

source = 'C:/Users/EMRE/Desktop/ndbatchworkon/'
dest1 = 'C:/Users/EMRE/Desktop/teleported_ndbatchworkon/'

listed=os.listdir(source)
mount=len(listed)/2
print('%d file exist' %mount)

time.sleep(1)

files=[]
for i in range(int(mount)):
    files.append('%d.txt' %(i+1))
    print('%d. file appended' %(i+1))
print(files)

listed=os.listdir(source)
mount=len(listed)/2
print('%d file exist' %mount)

for f in files:
    shutil.move(source+f, dest1)
    print('%s is teleporting...' %f)
    
	
print('Done!')