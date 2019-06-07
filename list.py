import glob
import os

WD = 'C:/Users/EMRE/Desktop/real_universe/'
files = glob.glob(os.path.join(WD,'*.jpg'))
with open('infiles.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in files)
	
	
	
#import os
#filee = open('all_names.txt','w')
#given_dir = 'C:/Users/EMRE/Desktop/real_universe/'
#[filee.write(os.path.join(os.path.dirname(os.path.abspath(__file__)),given_dir,i)+'\n') for i in os.listdir(given_dir,'*.jpg')]