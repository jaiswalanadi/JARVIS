import pyttsx3
import speech_recognition
import datetime
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import webbrowser
import random
from plyer import notification
import speedtest

for i in range(3):
    a = input("Enter Password to open Jarvis: ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME AJ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

from INTRO import play_gif
play_gif        

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)     # print(voices[0])
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 5)

    try:
        print("Understnding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said {query}\n")

    except Exception as e:
        print("Say that again")
        return "None"

    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("OK AJ, You may call me anytime")
                    break
                
                elif "how are you" in query:
                    speak("Perfect, Eveything Fine, What about you ?")
                elif "good" in query:
                    speak("That's Great")
                elif "thank you" in query:
                    speak("You are welcome")

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    url = f"https://www.google.com/search?q={query}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{query} is {temp}")
                elif "weather" in query:
                    url = f"https://www.google.com/search?q={query}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    weather = data.find("div", class_="BNeawe").text
                    speak(f"current{query} is {weather}")

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep, AJ")
                    exit()

                elif "search" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "pause" in query:
                    pyautogui.press("space")
                    speak("paused")
                elif "play" in query:
                    pyautogui.press("space")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("muted")
                elif "unmute" in query:
                    pyautogui.press("m")    

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me " + remember.read())

                elif "music" in query:
                    speak("Playing your favourite songs")
                    a = (1,2,3,4,5,6)  
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open(f'https://open.spotify.com/track/6ZLgnkQNj1CJldLocXd5Ul?si=068568dfbc1643d7')    
                    elif b == 2:
                        webbrowser.open(f'https://open.spotify.com/track/2ZD4aIEepqZsdxPxLSuUhm?si=b8897927d3064b9f')  
                    elif b == 3:
                        webbrowser.open(f'https://open.spotify.com/track/0NODNDsiY0sK5P0TnmDMSE?si=6dbb4f416a4541e1')
                    elif b == 4:
                        webbrowser.open(f'https://open.spotify.com/track/6EKY8rpjaBxxB0WbXJhedU?si=de0540dacc4b460f') 
                    elif b == 5:
                        webbrowser.open(f'https://open.spotify.com/track/7AhD1Yy6tzzm5WWqEWqnlm?si=0fe689afb6434018')           
                    else:
                        webbrowser.open(f'https://open.spotify.com/track/4wIJSFBXtoW3pAhvMvwfoX?si=69c4f9a21ab0436c')   

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()     

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)    

                elif "message" in query:
                    from Whatsapp import sendMessage
                    sendMessage()    

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
                    if shutdown == "yes":    
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break         

                elif "change password" in query:
                    speak("What is the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done")
                    speak(f"Your new password is {new_pw}")              

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks: "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task: "))
                            file = open("tasks.txt","a")
                            file.write(f"# {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks: "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task: "))
                            file = open("tasks.txt","a")
                            file.write(f"# {tasks[i]}\n")
                            file.close() 

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    notification.notify(
                    title = "My schedule:",
                    message = content,
                    timeout = 15
                    )     

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode [1 for YES / 2 for NO] : "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\jaisw\\Documents\\Anadi\\VS Studio\\JARVIS\\FocusMode.py")
                        exit()
                    else:
                        pass       

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()        

                elif "open" in query:   
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 

                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi Upload speed is {upload_net}")
                    speak(f"Wifi download speed is {download_net}")
                        

                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")  

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                    speak("SMILE")
                    pyautogui.sleep(4)
                    pyautogui.press("enter")   

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)        