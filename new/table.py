def table():
    from tabulate import tabulate
    import speak
    speak.speak("this is jarvis select any one of the data from the above list")
    print("select data :=")
    x=[["1.SEARCH","2.INFO","3.MESSAGE","4.PLAY VIDEO"],["5.TRANSLATOR","6.YOUTUBE","7.CHROME","8.TWITTER"],["9.WHATSAPP","10.INSTAGRAM","11.FACEBOOK","12.CALENDER"],["13.DISPLAY SYSTEM","14.TIME","15.RINGTONE","16.3D-GRAPHICS"],["17.GPU MINING","18.PLAYAUDIO","19.KILL CODE","20.SHUTDOWN"]]
    print(tabulate(x))
