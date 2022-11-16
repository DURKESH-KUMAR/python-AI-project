def search():
    import speak
    import pywhatkit
    speak.speak("ENTER THE INFO WHAT YOU NEED TO SEARCH")
    x=input("ENTER THE INFO WHAT YOU NEED TO SEARCH :")
    speak.speak("how much lines you need")
    y=int(input("ENTER LINES YOU NEED :"))
    try:
        speak.speak("are you searching about"+x)
        pywhatkit.info("{}".format(x),lines=4)
    except:
        speak.speak("invalid data was given to search engine")
        print("failed to search")
