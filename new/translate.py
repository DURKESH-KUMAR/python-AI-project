def translate():
    from translate import Translator
    import speak
    speak.speak("enter the language you use")
    x=input("ENTER THE LANGUAGE YOU USE :")
    speak.speak("enter the language you need to translate")
    y=input("ENTER THE LANGUAGE YOU NEED TO TRANSLATE :")
    speak.speak("enter the message you need to translate")
    z=input("ENTER THE MESSAGE :")
    b=Translator(from_lang=x,to_lang=y)
    a=b.translate(z)
    speak.speak(a)
    print(a)

