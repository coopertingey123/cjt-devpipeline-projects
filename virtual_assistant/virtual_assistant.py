import os
import pyttsx3
import speech_recognition  as sr
import datetime as dt
import subprocess 



engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voices = engine.getProperty('voices')

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voices = engine.getProperty('voices')

engine.setProperty('rate', 125)
engine.setProperty('volume', 0.75)
engine.setProperty('voice', voices[0].id)

r=sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def takecmd():
    with sr.Microphone() as source:
        print("Any last requests Mr. Bond? ")
        audio  = r.listen(source)
    return audio

def hearing():
    try:
        return (r.recognize_google(takecmd())).lower()
    except sr.UnknownValueError:
        print('I could not understand you')
    except sr.RequestError as e:
        print('error; {0}'.format(e))
        
def date():
    today = dt.date.today().strftime('%m-%d-%Y')
    speak(f' the day of your death is {today}')
    return today
    

# def date():
#     # master_list ='today'or 'date' or 'month' or 'today\'s' or 'time' or 'hour'
#     # # date_key_words = 'today' or 'date' or 'month' or 'today\'s'
#     # time_key_words = 'time' or 'hour'
#     today = dt.date.today().strftime('%m-%d-%Y')
#     time = dt.datetime.now().strftime('%H:%M')
#     # 
#     # speak(f' the day of your death is {today}')
#             #     return today
#             if time_key_words in hearing_str:
#                 speak(f'estimated time of death {time}')
#                 return time

def time():
    time = dt.datetime.now().strftime('%H:%M')
    speak(f'estimated time of death {time}')
    return time

def notepad():
    hearing_str = hearing()
    commands_list = 'open notepad' or 'open writing tool' or 'notepad' or 'writing tool'
    path_to_notepad = 'C:\\Windows\\System32\\notepad.exe'
    # path_to_file = 'C:\\Users\\ammon\\OneDrive\\Desktop\\hello.txt'

    if commands_list in hearing_str:

        speak('notepad is open.')
        subprocess.call([path_to_notepad])

def open_new_notepad():
    speak('What is the name of your new file?')
    hearing_str = hearing()
    try:    
        with open(f'{hearing_str}.txt', 'w') as new_file:
            pass
        path_to_notepad = 'C:\\Windows\\System32\\notepad.exe'
        path_to_file = f'C:\\Users\\ammon\\devpipline\\virtual_assistant\\{hearing_str}.txt'
        subprocess.call([path_to_notepad, path_to_file])
    except:
        with open('hitlist.txt', 'w') as hit_list:
            hit_list.write('''Welcome Mr. Bond Please type your name: ''')


def calculator():

    try: 
        math_equations()
    except:
        speak('Sorry my brain exploded. Here is the calculator.')
        path_to_calc = 'C:\Windows\System32\calc.exe'
        subprocess.call([path_to_calc])


def math_equations():
    my_string = hearing()
    print(f'{my_string} = {eval(my_string)}')
    speak(f' {my_string} equals {eval(my_string)}')

    
# calculator()


def main(hearing_str):
    # speak('Welcome to the command center!')
    # hearing_str = hearing()
    print('\033[92m' + "Choose your poison!")
    print(
'''Say Quit to die Mr. Bond!
Date of death
Time of death
Notes of those marked for death
Calculator to find out how many James Bond movies there are''')
    return hearing_str

hearing_str = main(hearing())
while True:
    hearing_str = main(hearing())
    if 'quit' or 'exit' in hearing_str:
        speak('Good riddance Mr. Bond...')
        break
    elif hearing_str == 'time' or 'hour':
        time()
    elif hearing_str == 'today' or 'date':
        date()
    elif hearing_str == 'notepad':
        pass
    elif hearing_str == 'calculator':
        calculator()
    else:
        continue

   

    # today's date
    # The time of day
    # Open and save new notepad
    # Calculator