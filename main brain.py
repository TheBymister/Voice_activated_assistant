import os
import time
import re
import winsound
import time
from time import sleep
from subprocess import call
import sys
import psutil
import os.path
from selenium import webdriver
import clipboard
import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import threading
import multiprocessing
import webbrowser

def stop():
    while True:
        listen_stop()
        print("Checking")
        if "stop" in voice_data:
            winsound.PlaySound(None, winsound.SND_PURGE)
            print("Stopping")
            break
        else:
            print("Continue")
            #print(OF)
            pass

def clipboard_paste():
    global clipboard
    clipboard = clipboard.paste()

def last_said():
    OF = open("current speech.txt","r+").read()
    file = open("Lastsaid.txt","w")
    file.write(OF)
    file.close

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en-uk')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def activation():
    global source
    with sr.Microphone() as source:
        global voice_data
        global audio
        r.energy_threshold = 4000
        audio = r.adjust_for_ambient_noise(source)
        print("Say the activation word")
        audio = r.listen(source)
        voice_data = ''
        print("Analysing voice")
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            activation()
        except sr.RequestError:
            speak("Sorry, my speech service is currently down")
            activation()
        except Exception as e:
            speak("You have no internet connection")
            activation()
        print(voice_data)

def listen():
    global source
    with sr.Microphone() as source:
        global voice_data
        global audio
        r.energy_threshold = 4000
        audio = r.adjust_for_ambient_noise(source)
        print("Say something")
        audio = r.listen(source)
        voice_data = ''
        print("Analysing voice")
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry i didn't catch that")
            activation()
        except sr.RequestError:
            speak("Sorry, my speech service is currently down")
            activation()
        except Exception as e:
            speak("You have no internet connection")
            activation()
        print(voice_data)

def listen_stop():
    global source
    with sr.Microphone() as source:
        global voice_data
        global audio
        r.energy_threshold = 6000
        audio = r.adjust_for_ambient_noise(source)
        print("Say something")
        audio = r.listen(source)
        voice_data = ''
        print("Analysing voice")
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            activation()
        except sr.RequestError:
            speak("Sorry, my speech service is currently down")
            activation()
        except Exception as e:
            speak("You have no internet connection")
            activation()
        print(voice_data)

def Bpaint():
    os.system("python Bpaint.py")

def tracker():
    os.system("python tracker.py")

def face_rec():
    os.system("python .\\face_recognition\\face_rec.py")

r = sr.Recognizer()

    
while True:
    while True:
        activation()
        if "thank" in voice_data and "you" in voice_data:
            speak("You are very welcome sir!")
        if "Sam" in voice_data:
            print ("Sam")
            ran = random.randint(1, 4)
            print(ran)
            global text
            if ran == 1:
                text = "Yes sir?"
            elif ran == 2:
                text = "At your service sir"
            elif ran == 3:
                text = "Here sir"
            elif ran == 4:
                text = "Yes boss"
            speak(text)
            break # Breaks loop
        else:
            print("Not Jarvis")
            
    while True:
        listen()

        if "login" in voice_data or "LogMeIn" in voice_data or "sign me in" in voice_data:
            speak("Which account would you like me to log you into?")

        
        if "launch" in voice_data:
            print("We have launch at 0256 GMT hours")
            query = voice_data
            stopwords = {'launch'}
            resultwords  = [word for word in re.split("\W+",query) if word.lower() not in stopwords]
            comm = ' '.join(resultwords)
            print(comm)
            if "paint" in voice_data:
                Bpaint = threading.Thread(target=Bpaint)
                Bpaint.start()
                break
            elif "international" in voice_data or "space staion" in voice_data and "tracker" in voice_data:
                tracker = threading.Thread(target=tracker)
                tracker.start()
                break
            elif "face recognition" in voice_data:
                face_rec = threading.Thread(target=face_rec)
                face_rec.start()
                break
            else:
                pass
            os.system(comm)
            break
        else:
            print("No go for launch")
            
        if "play" in voice_data:
            print("We have a play")
            query = voice_data
            stopwords = {'play'}
            resultwords  = [word for word in re.split("\W+",query) if word.lower() not in stopwords]
            comm = ' '.join(resultwords)
            print(comm)
            #hello = (".\\Songs\\"+comm+".wav")
            #print(hello)
            if os.path.isfile(".\\Songs\\"+comm+".wav"):
                winsound.PlaySound(".\\Songs\\"+comm+".wav", winsound.SND_ASYNC)
                stop()
                break
            else:
                speak("This song does not exist in my library. Would you like me to search for it on Youtube?")
                while True:
                    time.sleep(1)
                    listen()
                    if "yes" in voice_data or "yeah" in voice_data:
                        browser = webdriver.Chrome(".\\Chrome_driver\\chromedriver.exe")
                        browser.get("https://www.youtube.com/")
                        search = browser.find_element_by_name("search_query")
                        search.send_keys(comm)
                        click = browser.find_element_by_id("search-icon-legacy")
                        click.submit()
                        time.sleep(5)
                        break
                    elif "no" in voice_data:
                        break
                    else:
                        pass

                break
        else:
            print("No play time")
            pass

        if "made" in voice_data and "you" in voice_data or "created" in voice_data and "you" in voice_data or "designer" in voice_data or "designed" in voice_data and "you" in voice_data:
            speak("I was created by Byron Markey and Jakub Rychlinski in python")
            break
        else:
            pass

        if "time" in voice_data:
            t = time.localtime()
            hour = time.strftime("%H", t)
            minutes = time.strftime("%M", t)
            if int(hour) > 12:
                hour = int(hour)-12
            else:
                pass
            time = (str(hour)+":"+minutes)
            print(time)
            speak("The time is currently"+time)
            break
        else:
            print("Time is but a window")
            pass

        if "battery" in voice_data:
            battery = psutil.sensors_battery()
            try:
                global plugged
                global percent
                plugged = battery.power_plugged
                percent = str(battery.percent)
            except AttributeError:
                speak('You are on a desktop computer so this feature does not work')
                break
            if plugged == False:
                plugged="not plugged in"
            else:
                plugged = "plugged in"
            print("Your battery percentaged is ",percent+"% and your computer is "+plugged)
            break
        else:
            pass

        if "help" in voice_data:
            print("""           Showing all commands

[Launch] - Launch will launch windows built in programs such as notepad or command propmt or custom files such as Bpaint
         - Notepad
         - CMD
         - Bpaint
         
[Play]   - Play will play music from the songs directory or will search for the song on youtube

[Creator]- Will tell you who made this system

[Time]   - Tells you the time

[Battery]- Will tell you the battery of your laptop
         - NOTE: Does not work on Desktop computers!
         
[Help]   - Shows you this help menu

[Repeat] - Will repeat your last command

[Exit]   - Exits the program

""")
            break
        else:
            pass

        if "repeat" in voice_data:
            print("Not yet working")
            #OF = open("current speech.txt","r+").read()
            #file = open("Lastsaid.txt","r+").read()
            #OF == file
            #print(OF)

        if "close" in voice_data or "kill" in voice_data:
            os.system("taskkill /F /IM  python.exe /T tk.py")
            print("closing Bpaint")
            break
        else:
            pass

        if "thank" in voice_data and "you" in voice_data:
            speak("your very welcome sir")
            break
        else:
            pass

        if "search" in voice_data:
            query = voice_data
            stopwords = {'search'}
            resultwords  = [word for word in re.split("\W+",query) if word.lower() not in stopwords]
            comm = ' '.join(resultwords)
            print(comm)
            ran = random.randint(1, 2)
            print(ran)
            if ran == 1:
                text = "Absolutely sir"
            elif ran == 2:
                text = "Right away sir"
            elif ran == 3:
                text = "Here sir"
            speak(text)
            webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % comm)
            break
        else:
            pass

        if "introduce" in voice_data and "yourself" in voice_data:
            speak("Hello, my name is sam i'm a voice activated assistant. I have many basic functions such as telling you the time, playing music or searching things. I also contain more advanced features such as a built in international space station tracker and a face recognition feature which is currently being worked on. How may i help you today?")
            break
        else:
            pass
            
                
        if "exit" in voice_data or "quit" in voice_data:
            print("Exiting")
            exit()
        else:
            pass

