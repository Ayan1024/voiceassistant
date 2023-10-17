import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib
import openai
from config import apikey
import random
import numpy as np


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Ayan!')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Ayan!')
    elif hour >= 18 and hour < 21:
        speak('Good Evening Ayan!')
    else:
        speak('Good Night Ayan!')


def takecommand():
    # Input via microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again, please.")
        speak("Say that again, please.")
        return "None"
    return query

# def ai(prompt):
    
#  openai.api_key = apikey

# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {
#       "role": "user",
#       "content": ""
#     }
#   ],
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
# print(response['choices'][0]['text'])

# def sendEmail(to,content):
#     to = "reciveremail@gmail.com"
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('yourmail@gmail.com', to , content)
#     server.close()


if __name__ == "__main__":
     wishMe()
     speak('I am Nancy,  !!! How can I help you?? ')
     sites = [
        ('youtube', "https://www.youtube.com"),
        ('google', "https://www.google.com"),
        ('facebook', "https://www.facebook.com"),
        ('instagram', "https://www.instagram.com"),
        ('wikipedia', "https://www.wikipedia.org"),
        ('any watch', "https://www.aniwatch.com"),
        ('geet', "https://www.github.com"),
        ('chatgpt',"https://www.chat.openai.com"),
        ('whatsapp', "https://web.whatsapp.com/")
    ]
    
     while True:
        query = takecommand().lower()  # Converting user query into lower case

        for site in sites:
            if f"open {site[0]}".lower() in query:
                speak(f"Opening {site[0]}......")
                webbrowser.open(site[1])

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        

        
        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0])
        # 
        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Jaaaanuuu, the time is {strTime}")

        elif'open code' in query:
            codepath = "C:\\Users\\mraya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening visual studio code....")
            os.startfile(codepath)
        
        
        # elif ' email to Ayan' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takecommand()
        #         sendEmail(to=content)
        #         speak('Email has been send!')
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry Ayan . I couldn't send this email")

        if "openai".lower() in query.lower():
            prompt = (query)



        if "exit" in query:
                    print("Exiting...")
                    speak("Good Bye sir !! See you again")
                    break