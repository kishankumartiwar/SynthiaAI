import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12 :
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    
    speak("i am Synthia . please tell me how may i help you")

def takecommand():
    #it take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        print("say that again please ....")
        return "none"
    return query

if __name__ ==  "__main__":
    wishme()
    if 1 :
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open w3schools' in query:
            webbrowser.open("https://www.w3schools.com/")
            
        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            os.startfile(os.path.john(music_dir,songs[0]))
     
        elif 'the time' in query:
          strtime = datetime.datetime.now().strftime("%H:%M:%S") 
          speak(f" sir the time is {strtime}")
          print(strtime)

        elif 'open code' in query:
            codepath = "C:\\Users\\tiwar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile
