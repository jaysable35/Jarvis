#creating the voice for jarvis
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import webbrowser as web
import os

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
#cammand to wish to the user
def wishme():
    
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("Good Morning! ")
    
    elif hour>12 and hour<=18:
        speak("Good Afternoon! ")
    
    else:
        speak("Good evening! ")
        
    speak("I am Jarvis sir! how may I help you?")
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takecammand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognising...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("Say that agian please...")
        return "none"
    return query
if __name__ == "__main__":
    wishme()
    
    while True:
            
            query=takecammand().lower()
            
            
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query=query.replace("wikipedia"," ")
                result= wiki.summary(query,sentences=2)
                speak('According to Wikipedia')
                print(result)
                speak(result)
            
            elif 'stop' in query:
                
                break
            
            elif 'open google' in query:
                speak("opening google")
                web.open("google.com")
                
            elif 'open youtube' in query:
                speak("opening youtube")
                web.open("youtube.com")
                
            elif 'open linkedin' in query:
                speak("opening linkedin")
                web.open("linkedin.com")
                
            elif 'open twitter' in query:
                speak("opening twitter")
                web.open("twitter.com")
                
            elif 'open instagram' in query:
                speak("opening instagram")
                web.open("instagram.com")
            elif 'the time' in query:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir the time is{strtime}")
            elif 'spotify' in query:
                speak("opening spotify")
                codepath="C:\\Users\\jaysa\\Downloads\\SpotifySetup.exe"
                os.startfile(codepath)
            elif 'vs code' in query:
                speak("opening vs code")
                codepath="C:\\Users\\jaysa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
            elif 'udemy' in query:
                speak("opening udemy")
                web.open("udmey.com")
            elif 'google in collab' in query:
                speak("opening google colab")
                web.open("https://colab.research.google.com/")
                
                
                
                
                
                
                