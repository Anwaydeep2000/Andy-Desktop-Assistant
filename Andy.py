import speech_recognition as sr #pip install  SpeechRecognition
import pywhatkit                #pip install pywhatkit
from requests import get        #pip install requests
import cv2          #pip install opencv-python
import random
import webbrowser        #pip install webrowser
import datetime
import os
import wikipedia      #pip install wikipedia
import pyttsx3      #pip install pyttsx3




engn = pyttsx3.init('sapi5')
voices = engn.getProperty('voices')

engn.setProperty('voice', voices[1].id)

#string to speech
def say_it(audio):
    engn.say(audio)
    engn.runAndWait()


#speech to string
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        #Performs speech recognition on an AudioData instance using the Google Speech Recognition API.
        mycommand = r.recognize_google(audio, language='en-in')
        print(f"User said: {mycommand}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return mycommand


#gtreetings
def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say_it("Good Morning!")

    elif hour>=12 and hour<18:
        say_it("Good Afternoon!")

    else:
        say_it("Good Evening!")

    say_it("I am Andy. Please tell me how may I help you")



if __name__ == "__main__":
    welcome()
    while True:

        mycommand = takeCommand().lower()

    #Offline tasks

        if 'open camera' in mycommand or 'webcam'  in mycommand:

            # defining a video capture object
            vid = cv2.VideoCapture(0)
            while(True):
                # Capture the video frame by frame
                ret, frame = vid.read()

                # Display the resulting frame
                cv2.imshow('frame', frame)

                # quitting button 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            # After the loop release the cap object
            vid.release()
            cv2.destroyAllWindows()


        elif 'command prompt' in mycommand:
            say_it("Okay")
            os.system('start cmd')
            


        elif 'the time' in mycommand:
            strtime = datetime.datetime.now().strftime("%H:%M:&S")
            say_it(f"yea ,The time is {strtime}")

        elif 'music' in mycommand :
            say_it("just a second, playing a good music from your device")
            musicdir = 'D:\Music\English Songs'
            songs = os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,random.choice(songs)))


        elif 'open vs code' in mycommand:
            cpath = "C:\\Users\\natha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cpath)

    #CHATBOT

        elif 'thank you' in mycommand:
            say_it("you're welcome:)")
            say_it("can i do anything else for you?")


        elif 'love you' in mycommand:
            say_it("Sorry!\nI have a boyfriend")

        elif 'about yourself' in mycommand or 'who are you' in mycommand or 'what is your name' in mycommand:
            say_it("my name is Andy")
            say_it("I am an intelligent bot just like siri or google assistant\nI was developed by mr. Anwaydeep Nath ")
            say_it("what can i do for you?")

        elif 'who made you' in mycommand or 'who built you' in mycommand or 'who developed you' in mycommand:

            say_it("I was developed by mr. Anwaydeep Nath ")




        elif 'what are you doing' in mycommand:
            say_it('Just doing my thing!')

        elif 'bixbi' in mycommand or 'siri' in mycommand or 'google assistant' in mycommand or 'alexa' in mycommand:
            say_it("Yeahh they all are good\n but I am also a sweat one like them")

        elif 'exit' in mycommand or 'quit' in mycommand:
            say_it('Okay quiting, have a nice day ahead')
            exit()
       

  #Online tasks
        elif 'IP address' in mycommand or 'ip address' in mycommand:
            
            ip = get("https://api.ipify.org").text
            say_it(f"your ip adress is {ip}")

        elif 'send message' in mycommand or 'whatsapp' in mycommand:
            say_it("Okay ,what message should i send")
            msg=takeCommand().lower()
            pywhatkit.sendwhatmsg("+91number",f"{msg}",00,00)        

        elif 'open google' in mycommand:
            say_it("Okay ,what should i search on google")
            srch=takeCommand().lower()
            webbrowser.open(f"{srch}")
            
        elif 'wikipedia' in mycommand:
            say_it('Searching Wikipedia...')
            try:
                query = mycommand.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                say_it("According to Wikipedia")
                print(results)
                say_it(results)
                say_it("do you want me to do anything else?")
            except Exception as e:
                say_it("sorry, i'm unable to search at this moment")

           

        elif 'open youtube' in mycommand:
            webbrowser.open("youtube.com")
            say_it("Okay , I am Opening Youtube")

        elif 'open facebook' in mycommand:
            webbrowser.open("facebook.com")
            say_it("Sure , I am Opening facebook")

        elif 'open linkedin' in mycommand:
            webbrowser.open("linkedin.com")
            say_it("Okay , I am Opening linkedin")


        elif 'open instagram' in mycommand:
            
            webbrowser.open("instagram.com")
            say_it("Yea!, Opening instagram")
            

        else:
            say_it("sorry,I did not get you!!")
