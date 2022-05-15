# Gif maker code

import imageio
#load images
frames =[]
for i in range (833,5000,833):
    filename = "1delta" + str(i) + ".png"
    
frames.append(imageio.imread(filename))
imageio.mimwrite("saltmarshes_75flood_025bedload.gif", frames, format = ".gif", fps = 1)