def shutdown():
    import os 
    import speak
    speak.speak("your jarvis will shutdown soon please wait")
    os.system("shutdown /s /t 1")