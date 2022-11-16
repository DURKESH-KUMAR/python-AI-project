
import speak
speak.speak("jarvis personal assistant was activated by end user")
import table
table.table()
speak.speak("enter the data")
x=int(input("ENTER THE DATA :"))
if(x==1):
    import search
    search.search()
elif(x==2):
    import info
    info.info()
elif(x==3):
    import message
    message.message()
elif(x==4):
    import youtube
    youtube.youtube()
elif(x==5):
    import translate
    translate.translate()
elif(x==6):
    import youtubeweb
    youtubeweb.youtubeweb()
elif(x==7):
    import googleweb
    googleweb.googleweb()
elif(x==8):
    import twitterweb
    twitterweb.twitterweb()
elif(x==9):
    import whatsappweb
    whatsappweb.whatsappweb()
if(x==10):
    import instagramweb
    instagramweb.instagramweb()
elif(x==11):
    import facebookweb
    facebookweb.facebookweb()
elif(x==12):
    import calender
    calender.calender()
elif(x==13):
    import marks
    marks.marks()
elif(x==14):
    import time
    time.time()
elif(x==15):
    speak.speak("their is no ringtone is inserted right now")
elif(x==16):
    speak.speak("it was not still developed ")
elif(x==17):
    import gpu
    gpu.gpu()
elif(x==18):
    speak("no audio file was inserted")
elif(x==19):
    import kill
    kill.kill()
elif(x==20):
    import shutdown
    shutdown.shutdown()
else:
    speak.speak("invalid answer was given by end user jarvis will automatically will terminate")