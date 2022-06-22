# Importing Modules
import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import keyboard

# Initializing The Webcam
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
vid.set(cv2.CAP_PROP_FPS, 60)

# Initializing The SelfiSegmentation Module
segmentor = SelfiSegmentation()

# You Can Manually Change The Pictures Of The Background
# The Picture Resolution Must Be 1280*720
bg_img = cv2.imread("9.jpg")

# Making The Count
counter = 0

# Starting The Webcam
while True:
    # Reading The Video
    ret, video = vid.read()

    # Removing The Background And Replacing It With The New One
    rembg = segmentor.removeBG(video, bg_img, threshold=0.9)

    # Displaying The Output
    cv2.imshow("Output", rembg)
    cv2.waitKey(1)

    # Capturing The Picture
    if keyboard.is_pressed('s'):
        cv2.imwrite(f"New Image {counter} .jpg", rembg)
        counter = counter + 1
    
    # Breaking The Code
    elif keyboard.is_pressed('q'):
        break
