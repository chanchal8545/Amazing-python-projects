import speech_recognition as sr
import pyttsx3
 
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('I am alexa')
engine.say('What can i help you ')
engine.runAndWait()

try:
   with sr.Microphone() as source:
    print('listening.....')
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower()
    if 'alexa' in command:
        print(command)

except:
      pass         

