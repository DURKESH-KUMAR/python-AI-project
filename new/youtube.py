def youtube():
    import speak
    import pywhatkit
    speak.speak("enter the data you like to play")
    x=input("ENTER WHICH VIDEO YOU LIKE :")
    try:
        speak.speak("the video will start soon")
        pywhatkit.playonyt(x)
    except:
        speak.speak("failed to play")
        print("failed to play")
