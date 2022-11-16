def search():
    import speak
    import pywhatkit
    speak.speak("ENTER THE DATA WHAT YOU NEED TO SEARCH")
    x=input("ENTER THE DATA WHAT YOU NEED TO SEARCH :")
    try:
        speak.speak("are you searching about"+x)
        pywhatkit.search(x)
    except:
        speak.speak("invalid data was given to search engine")
        print("failed to search")
    
