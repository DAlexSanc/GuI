import cv2
from camera_pi import *
import sys, os
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk
import time



camera = Camera()

feed = camera.get_frame()
   
frame =  cv2.imread(feed)

#cv2.imshow(frame)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
canvas = tkinter.Canvas(root,width=w,height=h)
canvas.pack()
canvas.configure(background='black')
  
SetButton = Button(root,text="Settings", command=root.destroy)
SetButton.place(x=0,y=0)


def showPIL(pilImage):
    imgWidth, imgHeight = pilImage.size
 # resize photo to full screen 
    ratio = min(w/imgWidth, h/imgHeight)
    imgWidth = int(imgWidth*ratio)
    imgHeight = int(imgHeight*ratio)
    pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)   
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    imagesprite.lower()
    root.update_idletasks()
    root.update()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

try:
    showPIL(frame)

except KeyboardInterrupt:
    root.destroy