import speech_recognition as sr

def detect_language(audio):
    r = sr.Recognizer()
    text = r.recognize_google(audio, show_all=True)

    if "alternative" in text:
        for t in text["alternative"]:
            if t["language"] == "en":
                return "en"
    return None

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)
    lang = detect_language(audio)

    if lang == "en":
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
            print("Language not detected")

