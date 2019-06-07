#jpg sorter

import os
import glob
import sys
path='C:/Users/EMRE/Desktop/uav_dataset/'  # resimlerin bulunduğu klasörün yolu, burayı değiştir C:/Users/EMRE/Desktop/pytorch-yolo-v3-master_env/imgs/
print(path)
files=os.listdir("C:/Users/EMRE/Desktop/uav_dataset/") # resimlerin bulunduğu klasörün yolu,burayı değiştir C:/Users/EMRE/Desktop/pytorch-yolo-v3-master_env/imgs/

print(len(files))
i=0
for filename in files:

    src=path+files[i-0]
    print(src)
    dst=path+str(i+1)+'.jpg'
    print(dst)
    os.rename(src,dst)
    i=i+1
	
	
	

#import os 
  

#def main(): 
    #i = 0
      
    #for filename in os.listdir("xyz"): 
      #  dst ="Hostel" + str(i) + ".jpg"
       # src ='xyz'+ filename 
       # dst ='xyz'+ dst 
         
       # os.rename(src, dst) 
       # i += 1
  

#if __name__ == '__main__': 
   # main() 
