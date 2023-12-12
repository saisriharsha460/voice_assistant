from random import randint
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
import ecapture
import os
from ML import train_music_classifier,train_browser_classifier,train_sentiment_classifier


listener = sr.Recognizer()

Mithra = pyttsx3.init()

voices = Mithra.getProperty('voices')
Mithra.setProperty('voice', voices[1].id)

def talk(text):
    Mithra.say(text)
    Mithra.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        talk("Good morning!")

    elif 12 <= hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    talk('My name is Mithra, How can I help you')

def take_command():
    try:
        with sr.Microphone() as source:
            print('Mithra is listening... Please speak...')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Mithra' in command:
                command = command.replace('Mithra', '')

    except:
        pass
    return command


def run_Mithra():
    wishme()
    command = take_command()
    

    music_vectorizer, music_classifier = train_music_classifier()
    music_command_vectorized = music_vectorizer.transform([command])
    music_prediction = music_classifier.predict(music_command_vectorized)

    browser_vectorizer, browser_classifier = train_browser_classifier()
    browser_command_vectorized = browser_vectorizer.transform([command])
    browser_prediction = browser_classifier.predict(browser_command_vectorized)

    senti_vectorizer, senti_classifier = train_sentiment_classifier()
    senti_command_vectorized = senti_vectorizer.transform([command])
    prediction = senti_classifier.predict(senti_command_vectorized)
   

    if prediction[0] == "positive":
        talk("It sounds like you're feeling positive.")
    elif prediction[0] == "negative":
        talk("It sounds like you're feeling negative.")
    else:
        talk("It sounds like you're feeling neutral.")

    if music_prediction[0] == 1:
        music_dir = "C:\\D\\Songs"
        talk('playing music')
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[randint(0, 43)]))

    elif browser_prediction[0] == 1:
        webbrowser.open("https://www.google.com")  # You can change the URL to your preferred website


    elif 'time' in command:
        tm = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is' + tm)
        talk('Current time is' + tm)

    elif 'who is' in command:
        wiki = command.replace('who is', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)

    elif 'what is' in command:
        wiki = command.replace('what is', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)

    elif 'where is' in command:
        wiki = command.replace('where is', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)

    elif 'when is' in command:
        wiki = command.replace('when is', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)

    elif 'why is' in command:
        wiki = command.replace('why is', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)

    elif 'tell me about' in command:
        wiki = command.replace('tell me about', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)

    elif 'Define' in command:
        wiki = command.replace('Define', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)

    elif 'search' in command:
        text = command.replace('search', '')
        pywhatkit.search(text)

    elif 'youtube' in command:
        song = command.replace('youtube', '')
        print('playing ')
        talk('playing ')
        pywhatkit.playonyt(song)

    elif 'send message' in command:
        talk('sending')
        pywhatkit.sendwhatmsg("+918309562541", "Hi how are you", 15, 24)

    elif 'open pycharm' in command:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2023.1.lnk"
        talk('opening')
        os.startfile(path)


    elif "open microsoft edge" in command:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
        talk('opening')
        os.startfile(path)

    elif "open jupyter notebook" in command:
        path = "C:\\Users\\srini\\AppData\\Roaming\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Jupyter Notebook.lnk"
        talk('opening')
        os.startfile(path)

    elif "open chrome" in command:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
        talk('opening')
        os.startfile(path)

    elif "open this pc" in command:
        path = "C:\\Users\\srini\\OneDrive\\Desktop\\This PC - Shortcut.lnk"
        talk('opening')
        os.startfile(path)

    elif "open file manager" in command:
        path = "C:\\Users\\srini\\OneDrive\\Desktop\\This PC - Shortcut.lnk"
        talk('opening')
        os.startfile(path)

    elif "open spyder" in command:
        path = "C:\\Users\\srini\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Spyder.lnk"
        talk('opening')
        os.startfile(path)

    elif "open oracle" in command:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Oracle Database 10g Express Edition\\Run SQL Command Line.lnk"
        talk('opening')
        os.startfile(path)

    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com/")

    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com/")

    elif "open office" in command:
        webbrowser.open("https://www.office.com/apps?auth=2")

    elif "open word" in command:
        word_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
        talk('opening')
        os.startfile(word_path)

    elif "open ppt" in command:
        ppt_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
        talk('opening')
        os.startfile(ppt_path)

    elif "open power point" in command:
        power_point_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
        talk('opening')
        os.startfile(power_point_path)

    elif "player" in command:
        msi_app_player_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\MSI App Player.lnk"
        talk('opening')
        os.startfile(msi_app_player_path)

    elif "open access" in command:
        access_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Access.lnk"
        talk('opening')
        os.startfile(access_path)

    elif "open excel" in command:
        excel_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
        talk('opening')
        os.startfile(excel_path)

    elif "camera" in command or "take a photo" in command:
        ecapture.capture(0, "Aditya camera", "img.jpg")

    else:
        talk('Sorry I cannot understand you , You can search it from google')
        pywhatkit.search(command)
        pass

if __name__ == "__main__":
    run_Mithra()