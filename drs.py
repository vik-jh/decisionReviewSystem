import tkinter
from tkinter.constants import S
import cv2 #pip install opencv-python
import PIL.Image, PIL.ImageTk #pip install pillow
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture("clip.mp4")
flag = True


def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

        #play the video in reverse
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

          #play the video in forward mode
    grabbed, frame = stream.read()
    if not grabbed:
        exit()

    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
    if flag: 
    
        canvas.create_text(134, 26, fill = "black", font = "Times 26 italic bold", text = "Decision Pending")
    flag = not flag


def pending(decision):

    # 1. Display Decision Pending Image
    frame = cv2.cvtColor(cv2.imread(""), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)

    #2. Wait for 1 second
    time.sleep(1)
    
    #3. Display sponsor image

    frame = cv2.cvtColor(cv2.imread(""), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)

    #4. wait for 1.5 second
    time.sleep(1.5)
    #5. Display  Out or Not out
    if decision == 'out':
        decisionImg = "out.png"
    else:
        decisionImg = "not_out.png"


    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out", ))
    thread.daemon = 1
    thread.start()
    print("Player is Out!")


def Not_out():
    thread = threading.Thread(target=pending, args=("not out", ))
    thread.daemon = 1
    thread.start()

    print("Player is Not Out!!")






#Width and Height of our main screen 
SET_WIDTH = 650
SET_HEIGHT = 368
#Tkinter gui starts here
Window = tkinter.Tk()
Window.title ("CodeWithVikash Third Umpire Decision Review")
#cv_img = cv2.cvtColor(cv2.imread(""), cv2.COLOR_BGR2RGB)

canvas =tkinter.Canvas(Window, width = SET_WIDTH, height= SET_HEIGHT)
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

#image_on_canvas = canvas.create_image(0, 0, ancho = tkinter.NW, image = photo)

canvas.pack()


#Buttons to control playback
btn = tkinter.Button(Window, text = "<< Previous (fast)", width=50, command = partial
(play, -25))
btn.pack()

btn = tkinter.Button(Window, text = "<< Previous (slow)", width=50, command = partial
(play, -2))
btn.pack()

btn = tkinter.Button(Window, text = "Next (slow) >>", width=50, command = partial
(play, 2))
btn.pack()

btn = tkinter.Button(Window, text = "Next (fast)  >>", width=50, command = partial
(play, 25))
btn.pack()

btn = tkinter.Button(Window, text = "Give Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(Window, text = "Give Not Out", width=50, command=Not_out)
btn.pack()

Window.mainloop()
