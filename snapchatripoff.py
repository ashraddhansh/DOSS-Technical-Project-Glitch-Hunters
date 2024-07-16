from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np

class LiveCameraApp:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(self.parent, bg="#FFFF00")
        self.frame.pack(side=LEFT, padx=20, pady=20)  # Adding padding
        
        self.video_source = 0  # default camera
        
        self.vid = cv2.VideoCapture(self.video_source)
        
        self.canvas = Canvas(self.frame, width=640, height=480)  # Set the canvas size
        self.canvas.pack()
        
        self.update()
        
    def update(self):
        ret, frame = self.vid.read()
        if ret:
            # Apply selected filter to the frame
            frame = self.apply_filter(frame)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            # Position the image in the center with padding
            x = (self.canvas.winfo_width() - self.photo.width()) / 2
            y = (self.canvas.winfo_height() - self.photo.height()) / 2
            self.canvas.create_image(x, y, image=self.photo, anchor=NW)
        self.parent.after(10, self.update)
        
    def apply_filter(self, frame):
        return frame  # Default filter is "normal"
        
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

def button1_click(camera_frame):
    def filter_normal(frame):
        return frame
    camera_frame.apply_filter = filter_normal

def button2_click(camera_frame):
    def filter_grayscale(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    camera_frame.apply_filter = filter_grayscale

def button3_click(camera_frame):
    def filter_invert(frame):
        return cv2.bitwise_not(frame)
    camera_frame.apply_filter = filter_invert

def button4_click(camera_frame):
    def filter_blur(frame):
        return cv2.GaussianBlur(frame, (15, 15), 0)
    camera_frame.apply_filter = filter_blur

def button5_click(camera_frame):
    def filter_edge_detection(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    camera_frame.apply_filter = filter_edge_detection

    
    
root = Tk()
root.title("Snapchat on Steroids")
root.geometry('1200x800')
root.configure(background="#FFFF00")

text_label = Label(root, text="Camera Filters", fg='black', bg='#FFFF00')
text_label.pack(pady=(10, 10))
text_label.config(font=("Vandana", 25))

# Add live camera feed to the left side of the GUI
camera_frame = LiveCameraApp(root)

# Frame for buttons
button_frame = Frame(root, bg="#FFFF00")
button_frame.pack(side=RIGHT, padx=20, pady=20)

# Add buttons
button1 = Button(button_frame, text="Normal", command=lambda: button1_click(camera_frame), bg="red", width=15, height=3)
button1.grid(row=0, column=0, pady=10)

button2 = Button(button_frame, text="Grayscale", command=lambda: button2_click(camera_frame), bg="red", width=15, height=3)
button2.grid(row=1, column=0, pady=10)

button3 = Button(button_frame, text="Invert", command=lambda: button3_click(camera_frame), bg="red", width=15, height=3)
button3.grid(row=2, column=0, pady=10)

button4 = Button(button_frame, text="Blur", command=lambda: button4_click(camera_frame), bg="red", width=15, height=3)
button4.grid(row=3, column=0, pady=10)

button5 = Button(button_frame, text="Edge Detection", command=lambda: button5_click(camera_frame), bg="red", width=15, height=3)
button5.grid(row=4, column=0, pady=10)


'''
# Add five more buttons
button6 = Button(button_frame, text="Filter 6", command=lambda: button6_click(camera_frame), bg="red", width=15, height=3)
button6.grid(row=0, column=1, pady=10)

button7 = Button(button_frame, text="Filter 7", command=lambda: button7_click(camera_frame), bg="red", width=15, height=3)
button7.grid(row=1, column=1, pady=10)

button8 = Button(button_frame, text="Filter 8", command=lambda: button8_click(camera_frame), bg="red", width=15, height=3)
button8.grid(row=2, column=1, pady=10)

button9 = Button(button_frame, text="Filter 9", command=lambda: button9_click(camera_frame), bg="red", width=15, height=3)
button9.grid(row=3, column=1, pady=10)

button10 = Button(button_frame, text="Filter 10", command=lambda: button10_click(camera_frame), bg="red", width=15, height=3)
button10.grid(row=4, column=1, pady=10)

'''
root.mainloop()
