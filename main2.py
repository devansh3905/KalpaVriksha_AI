import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

while True:
    print("Say something!")
    with sr.Microphone() as source:
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language='en-IN')
        print("You said: " + text)
        break
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))