import time
import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import pyautogui
import pyjokes






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[2].id)



#text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice to txt
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit = 5)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio,language='en-in')
        print(f'user said : {query}')
    except Exception as e:
        speak("Say that again please....")
        return 'none'
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime('%H:%M %p')
    if 'get up' in query:
        speak('bishmillah')
        if hour>0 and hour<=12:
            speak(f'Good Morning Harun, its: {tt}')
        elif hour>12 and hour<18:
            speak(f'Good Afternoon Harun, its: {tt}')
        else:
            speak(f'Good Evening Harun, its: {tt}')
        speak("Hi Harun. I am chinnu  ,  please tell me what can i do for you ")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://youtube.com/playlist?list=RD3wU2Neyf7q0&playnext=1" + query
        webbrowser.open(web)
        kit.playonyt(query)
        speak("Done, Sir")

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=5e7258b1d59140daa877107c26c12c97'
    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page['articles']
    #print(articles)
    head = []
    days = ["first","second","third","fourth","fifth","sixth","seventh","eightth","nineth","tenth"]
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(days)):
        speak(f"today's {days[i]} news is : {head[i]}")


if __name__=="__main__":
    query = takecommand().lower()
    wish()
    while True:
        query = takecommand().lower()

        #logic builkding for task

        if 'open chrome' in query:
            cpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)
        elif 'hello' in query:
            speak("hello harun , how are you ")
        elif 'doing well' in query:
            speak("that's great harun")
        elif 'what about you' in query:
            speak("perfect harun ")
        elif 'what did last night' in query:
            speak('''harun last night done one project on python 
functions are worked good manner, 
finally performed well. ''')
        elif "great" in query:
            speak("you are doing well harun, keep it up sir, performance great harun.")
        elif 'today task' in query:
            speak('you must prepare for Software testing exam harun. For tomorrow purpose ')
        elif 'any schedule afternoon' in query:
            speak("yes harun, you have to play cricket with your friends harun ")
        elif 'breakfast' in query:
            speak('''sure harun ! you  will go for break fast.
                 can i perform any work sir during your breakfast ?''')
        elif 'have any exam today' in query:
            speak('yes harun, you have exam on flipkart grid 5.0')
        elif 'just sleep' in query:
            speak('thank you harun, after breakfast you can call me. bye harun')
            sys.exit()



        elif 'open telegram' in query:
            tpath ="E:\\Telegram Desktop\\Telegram.exe"
            os.startfile(tpath)

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'open notepad' in query:
            speak('ok sir ,opening notepad++....')
            npath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(npath)
        elif 'close notepad' in query:
            speak('Ok sir, closing notepad++...')
            os.system('taskkill /f /im notepad++.exe')

        elif 'set alaram' in query:
            nn= int(datetime.datetime.now().hour)
            if nn==22:
                surah_dir = 'D:\\surah'
                surah = os.listdir(surah_dir)
                os.startfile(os.path.join(surah_dir, surah[0]))


        elif 'open vlc' in query:
            vpath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vpath)
        elif 'open gta' in query:
            gpath = "D:\\Games\\Grand Theft Auto V\\PlayGTAV.exe"
            os.startfile(gpath)

        elif 'play surah' in query:
            surah_dir = 'D:\\surah'
            surah = os.listdir(surah_dir)
            rd = random.choice(surah)
            os.startfile(os.path.join(surah_dir, rd))

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your ip address is : {ip}')

        elif 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'tell me a joke' in query: 
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 5")
        elif 'restart the system' in query:
            os.system("restart /r /t 5")
        elif 'sleep the system' in query:
            os.system("round1132.exe powerprof.dll,SetSuspendState 0,1,0")

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "switch to window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'latest news' in query:
            speak("please wait sir, fetching the latest news")
            news()
        elif 'wonder news' in query:
            speak('yes,sir')
        elif 'youtube' in query:
            searchYoutube(query)


        elif 'play on youtube' in query:
            kit.playonyt("surah fathiha")


        elif 'thank you' in query:
            speak('jazakalla kkhair for talking me harun , have a nice day , allah bless you....')
            sys.exit()
        speak("........")



