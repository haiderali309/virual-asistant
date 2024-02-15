#pip install pyttsx3
import pyttsx3
import datetime
#available
import pyaudio
import speech_recognition as sr
#pip install SpeechRecognition
import wikipedia
#pip install wikipedia-api
import webbrowser
#available
import sys
#available
from PIL import Image
#pip install Pillow
import os
#available
import numpy as py
# pip install numpy
import cv2
#pip install opencv-python
from tkinter import Tk, filedialog
from ffpyplayer.player import MediaPlayer
#pip install ffpyplayer
import phonenumbers
#pip install phonenumber
from phonenumbers import carrier
#pip isntall openai


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good evening sir")
    speak("I am Jerry. How may I help you ")

def takcom():
    r = sr.Recognizer()
    with sr.Microphone() as sour:
        print("Sir I am listening...") 
        r.pause_threshold = 1
        audio = r.listen(sour)

    try:
        print("Analyzing....")
        query = r.recognize_google(audio, language= 'em-in')
        print( f"You said: {query}\n")

    except Exception as E:
        print("Say it again sir, I did not understand it")
        return "None"
    return query

def pv():
       # Ask the user to select a folder
    root = Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(title="Select Folder with Videos")

    if not folder_path:
        print("No folder selected. Exiting.")
        return

    # List all video files in the selected folder
    video_files = [f for f in os.listdir(folder_path) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the selected folder. Exiting.")
        return

    print("Available videos:")
    for i, video_file in enumerate(video_files, start=1):
        print(f"{i}. {video_file}")

    # Ask the user to select a video
    while True:
        try:
            choice = int(input("Select a video (enter the number): "))
            if 1 <= choice <= len(video_files):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_video = os.path.join(folder_path, video_files[choice - 1])

    # Play the selected video
    video = cv2.VideoCapture(selected_video)
    player = MediaPlayer(selected_video)

    while True:
        ret, frame = video.read()
        audio_frame, val = player.get_frame()

        if not ret:
            print("End of video.")
            break

        cv2.imshow("Video", frame)

        stoper=int(input("Enter 0 to stop (Enter the number): "))

        if(cv2.waitKey(1)& stoper == 0):
            video.release()
            cv2.destroyAllWindows()
            return

def you_search():
    speak('do you search anything on youtube')
    ans=takcom()
    if(ans=="no"):
        webbrowser.open("youtube.com")
    else:
        speak('what you want to search')
        que=takcom()
        search_url = f"https://www.youtube.com/results?search_query={que}"
        webbrowser.open(search_url)
        return

def goog():
    speak('do you search any thing on google')
    ans=takcom()
    if(ans=="no"):
        webbrowser.open("google.com")
    else:
        speak('what you want to search')
        que=takcom()  
        search_url =  f"https://www.google.com/search?q={que}"
        webbrowser.open(search_url)
        return

def oner():
    speak("Sure, sir.")  
    webbrowser.open("https://www.facebook.com/photo/?fbid=3184971348386048&set=a.1533259406890592")
    speak("I am created by Muhammad Haider Ali. He is a student of Software Engineering at the University of Lahore")

def wfile(filename="output.txt"):
    with open(filename, "a") as file:
        while True:
            input("Press Enter to start recording or 'q' to quit...")
            text = takcom()
            if text:
                print(f"Text: {text}")
                file.write(text + "\n")
            choice = input("Do you want to continue recording? (y/n): ")
            if choice.lower() != 'y':
                break

def get_phone_number_details(phone_number):
    try:
        # Parse the phone number with default region (change 'XX' to the appropriate default region)
        parsed_number = phonenumbers.parse(phone_number, 'XX')

        # Check if the phone number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            print("Invalid phone number.")
            return

        # Get details
        region = phonenumbers.region_code_for_number(parsed_number)
        national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        service = carrier.name_for_number(parsed_number, "en")   
        
        print("Phone Number Details:")
        print("Country Code:", parsed_number.country_code)
        print("National Format:", national_format)
        print("International Format:", international_format)
        print("Name:", __name__)
        print("Region:", region)
        print("Service:", service)

    except phonenumbers.NumberParseException as e:
        print(f"Invalid phone number format: {e}")



if __name__ == "__main__":
    wish()
    while True:
        query = takcom().lower()
        if 'hello jerry' == query:
            speak("How may i help you sir.")
        if 'wikipedia' in query :
            speak('Searching Wikipidia..')
            query=query.replace("wikipidia","")
            result=wikipedia.summary(query, sentences=3)
            speak("According to wikipidia")
            print(result)
            speak(result)
        elif 'open youtube' in query :
            you_search()

        elif 'open google' in query :
            goog()
    
        elif 'who is your creator' in query or 'who creates you' in query or 'who created you' in query:
            oner()

        elif 'open image' in query:
            speak("Sure, sir.")
            image_path = "G:\\virual asistant\\2023_08_27_15_35_IMG_4229.JPEG"
            img = Image.open(image_path)
            img.show()

        elif 'open this pc' in query or 'open my computer' in query:
            speak("Sure, sir.")
            os.system("explorer /select, D:")

        elif 'play music' in query:
            pv()

        elif 'search number' in query:
            speak("Enter phone number")
            phone_number_to_lookup = input("enter number: ")
            get_phone_number_details(phone_number_to_lookup)

        elif 'add content to file' in query:
            wfile()

    
        elif'goodbye jerry' in query:  
            speak("nice meeting you Sir Thanks for using me")
            sys.exit()