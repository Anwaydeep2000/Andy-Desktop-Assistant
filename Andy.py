import speech_recognition as sr
import random
import webbrowser
import datetime
import wikipedia
import pyttsx3
import os


engn = pyttsx3.init('sapi5')
voices = engn.getProperty('voices')

engn.setProperty('voice', voices[1].id)


def say_it(audio):
    engn.say(audio)
    engn.runAndWait()


def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say_it("Good Morning!")

    elif hour>=12 and hour<18:
        say_it("Good Afternoon!")

    else:
        say_it("Good Evening!")

    say_it("I am Andy. Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        mycommand = r.recognize_google(audio, language='en-in')
        print(f"User said: {mycommand}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return mycommand


if __name__ == "__main__":
    welcome()
    while True:

        mycommand = takeCommand().lower()

        # Logic for executing tasks based on the commands of the user
        if 'wikipedia' in mycommand:
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

        elif 'open google' in mycommand:
            webbrowser.open("google.com")
            say_it("Yea!, Opening Google")

        elif 'open instagram' in mycommand:
            webbrowser.open("instagram.com")
            say_it("Okay , I am Opening")

        elif 'the time' in mycommand:
            strtime = datetime.datetime.now().strftime("%H:%M:&S")
            say_it(f"yea ,The time is {strtime}")


        elif 'thank you' in mycommand:
            say_it("you're welcome:)")
            say_it("can i do anything else for you?")

        elif 'about yourself' in mycommand or 'who are you' in mycommand or 'what is your name' in mycommand:
            say_it("my name is Andy")
            say_it("I am an intelligent bot just like siri or google assistant\nI was developed by mr. Anwaydeep Nath ")
            say_it("what can i do for you?")

        elif 'open vs code' in mycommand:
            cpath = "C:\\Users\\natha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cpath)

        elif 'music' in mycommand :
            say_it("just a second, playing a good music from your device")
            musicdir = 'D:\\Music\\English'
            songs = os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,random.choice(songs)))


        elif 'what are you doing' in mycommand:
            say_it('Just doing my thing!')

        elif 'bixbi' in mycommand or 'siri' in mycommand or 'google assistant' in mycommand or 'alexa' in mycommand:
            say_it("Yeahh they all are good\n but I am also a sweat one like them")

        elif 'exit' in mycommand or 'quit' in mycommand:
            say_it('Thank you!!\nHave a great day ahead')
            exit()
        else:
            say_it("sorry,I did not get you!!")
            say_it('What else you want me to do?')
