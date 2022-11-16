def marks():
    import speak
    speak.speak("system performance will been display sooner")
    import matplotlib.pyplot as a
    x=[98,97,98,93,96,100]
    y=["CPU","GPU","RAM","ROM","CHARGE","BRIGHTNESS"]
    
    a.pie(x,labels=y)
    a.title("TOTAL PERFORMANCE OF YOUR JARVISE")
    a.show()
marks()
