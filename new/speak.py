def speak(y):
    import pyttsx3
    x=pyttsx3.init()
    x.setProperty("rate",125)
    x.say(y)
    x.runAndWait()
