"""
Before this we train dataset by using teachable machine introduced by google and download model and save it.
By the help of training and modelling data we can predict sign and also it can convert to speech.
We also created a GUI for user to see the result.
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import pyttsx3
from tkinter import *                  #module used for gui(Graphical user interface)
from PIL import ImageTk, Image         #module used for inserting image
import speech_recognition as sr        #module used for recognizing speech
import image
# from PIL import Image


cap = cv2.VideoCapture(1)
detector = HandDetector(maxHands=3)

classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

counter = 0
file = open("C:\\Users\\ranji\\PycharmProjects\\Sign2\\Model\\\labels.txt")
read = file.readlines()

labels = ['A','B','C','D','E','F']


#predict sign that we created data

def sign():
    while True:
        success, img = cap.read()

        hands, img =detector.findHands(img)


        cv2.rectangle(img, (0, 20), (500, 600), (255, 255, 255), 2)
        prediction, index = classifier.getPrediction(img)

        if hands:   # checking condition is there hand or not


            print(prediction,index)

            engine = pyttsx3.init()     #converting text in label to speech
            engine.say(read[index])

            cv2.imshow("Image", img)
            engine.runAndWait()


            # cv2.waitKey(1)
            if cv2.waitKey(1) & 0XFF == ord("f"):
                break

def speech():

    r = sr.Recognizer()
    with sr.Microphone() as source:


        list = ['hello', 'thank you', 'goodbye', "yes","please","no"]

        for i in range(2):
            print("Two Chances")
            print("Speak Anything :")

            audio = r.listen(source)

            try:

                text = r.recognize_google(audio)


                print("You said : {}".format(text))



                if text in list:

                    path = f"Signs/{text}.jpg"
                    image = cv2.imread(path)
                    cv2.imshow("windows", image)
                    cv2.waitKey(0)


                else:
                    print("NO DATA")

            except:
                print("Sorry could not recognize what you said")

        print("Start again for Transilation")


# tkinter gui

root = Tk()


def tkin():
    global second

    second = Toplevel()
    second.title('INDIAN SIGN TO SPEECH')
    second.geometry('920x580')
    second.configure(background="Blue")
    MyText = StringVar()
    label = Label(second, text='WE HELP YOU TO COMMUNICATE WITH DEAF PEOPLE WITH INDIAN SIGN LANGUAGE TO VOICE & VOICE TO SIGN.', font=('Times New Roman', 12, 'bold'))
    label.pack()
    img = ImageTk.PhotoImage(Image.open("img.jpg"))
    panel = Label(second, image = img, height = 600,width = 600)
    panel.pack(side = "top", fill = "both", expand = "yes")
    button = Button(second, text='Sign_Speech',bg="Green" ,command=sign)
    button.place(x = 260, y = 520, width = 120, height = 50)
    button = Button(second, text="Exit",bg="red", command=second.destroy)
    button.place(x=800, y=520, width=120, height=50)
    button = Button(second, text='Speech_Sign',bg="Green" ,command=speech)
    button.place(x = 520, y = 520, width = 120, height = 50)

    root.mainloop()



root.title("Main Window")

# Set Geometry
root.geometry('300x200')

label = Label(root, text='Welcome', font=('Times New Roman', 12, 'bold'))
label.pack()
label = Label(root, text='We built a scope to Deaf and dump peoples', font=('Times New Roman', 12, 'bold'))
label.pack()
Button(root, text="launch Window", command=tkin).pack(pady=10)
exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()



