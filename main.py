import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'hello' in command:
        talk('hello my name is alexa i am your personal assistant')
        print('hello my name is alexa  i am your personal assistant')
    elif 'how are you' in command:
        talk('i am fine tell me about your self')
        print('i am fine tell me about your self')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'who ' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what' in command:
        person = command.replace('what', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'when' in command:
        person = command.replace('what', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
        print('sorry, I have a headache')
        print(date)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        jok = pyjokes.get_joke()
        print(jok)
        talk(jok)
    elif 'bye' in command:
        talk('bye')
        print("bye")
    elif 'thank' in command:
        talk('most welcome')
        print("most welcome")
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
