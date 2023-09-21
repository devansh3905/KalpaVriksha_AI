import pyttsx3 as pyt
import pyaudio
import speech_recognition as sr
from gingerit.gingerit import GingerIt

listener = sr.Recognizer()
engine = pyt.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def __main__():
    try:
        with sr.Microphone() as source:

            #greet()
            engine.say("Hey, I am your A I assistant..")
            engine.say("Say something")
            engine.runAndWait()


            print("Say something...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            engine.say(command)
            engine.runAndWait()
            parser = GingerIt()

            #correction()
            if command == '':
                print("You didn't say anything.")
            else:
                result_dict = parser.parse(command)
                print("correct sentence is - " + str(result_dict["result"]))
                right_sent = str(result_dict["result"])
                if right_sent == command:
                    print("This is right")
                    engine.say("this is right")
                    engine.runAndWait()
                else:
                    engine.say("Correct sentence is - " + str(result_dict["result"]))
                    engine.runAndWait()
    except:
        pass