import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb 
import psutil
import pyjokes
import os
import pyautogui


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The Current time is")
    speak(time)

def date():
    year =datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Saurav!")
    hour =datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour >=18 and hour<24:
        speak("Good Evening")
    else :
        speak("Good night")
    speak("Soul at your Service,  Please Tell how can i help you today?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("please say that again")
        return "None"
    return query



def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def joke():
    jk = pyjokes.get_joke()
    print(jk)
    speak(jk)

def screenshot():
    img = pyautogui.screenshot()
    img.save("c:/Users/sir/Desktop/soul/screenshot.png")
    speak("Screenshot taken sir")




if __name__ == "__main__":
    wishme()
    while True:
        query = TakeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching")
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences=3)
            speak("According to the wikipedia")
            print(result)
            speak(result)
       
        elif 'search in chrome' in query:
            speak("What Do you want to search in google?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'search in youtube' in query:
            speak("What do you want to seach in youtube")
            searchterm=TakeCommand().lower()
            speak("here we go to youtube")
            wb.open('https://www.youtube.com/results?search_query='+searchterm)
        elif 'google' in query:
            speak("What should in google?")
            searchterm=TakeCommand().lower()
            speak("Searchin")
            wb.open('https://www.google.com/search?q='+searchterm)
        elif "cpu" in query:
            cpu()
        elif 'thank you' in query:
            speak("Glad to help you sir , Have a nice day!")
        elif 'how are you' in query:
            speak("Thanks for asking, I am always fine  ,as my creator Saurav always keep me up to date")
        elif 'joke' in query:
            joke()
        elif 'relax' in query:
            speak("Going offline sir!")
            quit()
        elif 'write a note' in query:
            speak("What should i write sir?")
            notes = TakeCommand().lower()
            print(notes)
            file = open("notes.txt",'w')
            speak("Sir should i include date and time?!")
            ans = TakeCommand().lower()
            if 'yes' in  ans or 'sure' in ans:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strtime)
                file.write(";-")
                file.write(notes)
                speak("Done sir!")
            elif 'no' in query:
                file.write(notes)
                speak("Done Sir!")
        elif 'show notes' in query:
                speak("Showing notes")
                file = open("notes.txt","r")
                notes = file.read()
                print(notes)
                speak(notes)
        elif 'screenshot' in query:
            screenshot()
        elif 'remember that' in query:
            speak("What should i remember sir")
            memory = TakeCommand().lower()
            speak("You asked me to remember that"+memory)
            remember = open("memory.txt",'w')
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in query:
            command = open("memory.txt","r")
            s = command.read()
            speak("You told to remember")
            print(s)
            speak(s)
            
            
        
        

                
        

        

            

    
            


        



