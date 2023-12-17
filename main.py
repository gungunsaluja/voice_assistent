import time
import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import ctypes
import winshell
import subprocess
import pyjokes
import smtplib
import requests
import json
import wolframalpha
import time
warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: "+data)

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")

    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition"+ex)

    return data


def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "assistant"

    text = text.lower()

    if action_call in text:
        return True

    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "january",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]
    return f'Today is {week_now}, {months[month_now-1]} the {ordinals[day_now-1]}.'


def say_hello(text):
    greet = ["hi", "hello", "hola", "greetings", "howdy", "hey there"]

    response = ["hi", "hello", "hola", "greetings", "howdy", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

        return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki)-1 and list_wiki[i].lower() == "who" and list_wiki[i+1].lower() == "is":
            return list_wiki[i+2] + " "+list_wiki[i+3]


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe"], file_name)


def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.startls()

    server.login("salujagungun03@gmail.com", "vamika@11")
    server.close()


while True:

    try:

        text = rec_audio()
        speak = " "

        if call(text):

            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                    speak = speak + " " + "It is "+str(hour) + ":"+minute + " "+meridiem + " ."

            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki

            elif "who are you " in text or "define yourself" in text:
                speak = speak + """Hello, I am your voice assistant. I am here to make your life easier."""

            elif "Your name" in text:
                speak = speak + "my name is assistant"

            elif "How are you" in text:
                speak = speak + "I am fine, thank you"
                speak = speak + "\n how are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "It is good to know that you are fine"

            elif "open" in text.lower():

                if "youtube" in text.lower():
                    speak = speak + "Opening youtube"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = speak + "Opening Google"
                    webbrowser.open("https://google.com")

                elif "stackoverflow" in text.lower():
                    speak = speak + "Opening Stackoverflow"
                    webbrowser.open("https://stackoverflow.com/")
                else:
                    speak = speak + "Application not avalibale"

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=+" +
                    "+".join(search)
                )
                speak = speak + "opening " + str(search) + "on youtube"
            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?=" + "+".join(search)
                )
                speak = speak + "Searching " + str(search) + "on google"

            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https:///www.google.com/search?=" + "+".join(search)
                )
                speak = speak + "Searching" + str(search) + "on google"

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "recycle bin emptied"


            elif "note" in text or "remember this" in text:
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that"

            elif "where is" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + " this is where " + str(location) + " is."
                webbrowser.open(url)

            elif "joke" in text or "jokes" in text:
                speak = speak + pyjokes.get_joke()

            elif "email to computer " in text or "gmail to computer " in text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    to = "gungunsaluja16@gmail.com"
                    send_email(to, content)
                    speak = speak + "Email has been sent!"
                except Exception as e:
                    print(e)
                talk("I am not able to send this email")

            elif "mail" in text or "email" in text or "gmail" in text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    talk("whom should I send")
                    to = input("Enter to address: ")
                    send_email(to, content)
                    speak = speak + "Email has been sent!"
                except Exception as e:
                    print(e)
                speak = speak + " I am not able to send email"
            elif "news" in text:
                url = ('https://newsapi.org/v2/top-headlines?'
                        'country=us&'
                        'apiKey=e8c0663b870e4bc68cbb8053624c9946')

                try:
                    response = requests.get(url)
                except:
                    talk("please check your connection")

                news = json.loads(response.text)

                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    talk(str(new["title"]))
                    engine.runAndWait()

                print(str(new["description"]), "\n")
                talk(str(new["description"]))

            elif "calculate" in text:
                app_id = " 74E5LA-XQEWG7TLEW"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("calculate")
                text = text.split()[ind + 1:]
                res = client.query(" ".json(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer

            elif "what is" in text or "who is" in text:
                app_id = "74E5LA-XQEWG7TLEW"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("calculate")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer

            elif "don't listen " in text or "stop listening " in text or "do not listen" in text:
                talk("for how many seconds do you want me to sleep")
                a = int(rec_audio())
                time.sleep(a)
                speak = speak + str(a) + "seconds completed.Now you can ask me anything"

            elif "exit" in text or "quit" in text:
                exit()


            response(speak)

    except:
        talk("I don't know that")

