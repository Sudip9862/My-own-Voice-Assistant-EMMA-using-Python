import pyttsx3 #for speach
import datetime 
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import random #play random music
import cv2 #for taking a picture
import requests, sys, bs4
import time #for the video time duration



def emailencryption():
    txt = open("password.txt","r")
    text = txt.readlines()
    for x in text:
        a=x
    return a



engine = pyttsx3.init('sapi5') #sapi5 is a microsoft speach API
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices)  #voices[0].id for female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir!")
    
    elif hour>=12 and hour<18:
        speak("good afternoon sir!")

    else:
        speak("good evening sir!")

    speak("I am your assistant. how can i help u")

def takeCommand():
    #it takes microphone input  from user and returns string output

    r = sr.Recognizer() #audio recognizer
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8 # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 300  # to remove background noise
        audio = r.listen(source)

    #when we write try ?? -> when we assume i may lead to some error
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n") #print("user said:", query)

    except Exception as e:
        print(e)  
        print("say that again please sir")
        speak("say that again please sir")
        return "none"
    return query    


def sendEmail(to, content):
    pword = emailencryption()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', pword)
    server.sendmail('abc@gmail.com', to, content)
    server.close()

def createfolder():
    try:
        # path = "C:\\Users\\HP\\Desktop"
        # os.mkdir(path)
        speak("what will be the file name")
        query1 = takeCommand().lower() 
        os.chdir("C:\\Users\\HP\\Desktop")
        os.mkdir(query1)
        speak("successfully created in desktop")
    except OSError:
        speak("creation of the directory failed. in"+path)



def search_file(filename, search_path, pathsep=os.pathsep):
        path = os.path.join(search_path, filename)
        if os.path.exists(path):
             return os.path.abspath(path)


def renamefolder():
    try:
        # speak("sudip didnot add this in my system. he is so fucking rude")
        # query1 = takeCommand().lower()
        # if 'shut up' in query1:
        #     speak("you shut up. you are so fucking bossy")
        speak(" okk just a minute sir. I am showing u the files and folders present in desktop .")
        a = os.listdir("C:\\Users\\HP\\Desktop")
        print(a)
        speak("which file u want to rename")
        search_path = "C:\\Users\\HP\\Desktop"
        query1 = takeCommand().lower()
        thefile = query1
        find_file = search_file(thefile, search_path)
        if find_file:
            a= "find found at %s" %find_file
            print(a)
            speak(a)
            speak("trying to rename the file. please wait sir. what name u want to give to this file names")
            query1 = takeCommand().lower()
            newname = query1 
            path = os.chdir(search_path)
            os.rename(thefile,newname)
            speak("file rename successfull")
        else:
            speak("file not found")


    except Exception as e:
        print(e)
        speak("sorry, unable to rename files")


    
def deletefolder():
    try:
        speak(" okk just a minute sir. I am showing u the files and folders present in desktop .")
        a = os.listdir("C:\\Users\\HP\\Desktop")
        print(a)
        speak("which file u want to delete")
        search_path = "C:\\Users\\HP\\Desktop"
        query1 = takeCommand().lower()
        thefile = query1
        find_file = search_file(thefile, search_path)
        if find_file:
            a= "find found at %s" %find_file
            print(a)
            speak(a)
            speak("trying to delete the file.")
            speak("what is the password")
            query1 = takeCommand().lower()
            passworddel = query1
            if passworddel == "hello":
                folder = thefile
                parent = "C:\\Users\\HP\\Desktop"
                dicpath = os.path.join(parent,folder)
                os.rmdir(dicpath)
                speak("file deletion successfull")
            else:
                speak("wrong password")
        else:
            speak("file not found")

    except Exception as e:
        print(e)
        speak("unable to delete files")



def searchfilemain():
    speak("what is the file name u want to search")
    search_path = "C:\\Users\\HP\\Desktop" #'/bin' + os.pathsep + '/usr/bin' 
    query1 = takeCommand().lower()
    thefile = query1
    find_file = search_file(thefile, search_path)
    if find_file:
        a= "File found at %s" % find_file
        print(a)
        speak(a)
    else:
        speak("File not found")
        speak("I am showing u the files and folders present in desktop .")
        a = os.listdir("C:\\Users\\HP\\Desktop")
        print(a)            

            

def takephoto():
    camera = cv2.VideoCapture(0)
    speak("taking picture process will start now.     I will take 2 photos simultaneously")
    for i in range(2):
        ret, img = camera.read()
        if ret == True:
            cv2.imwrite("emmaphoto"+str(random.randint(1,1000))+".png",img)
        else:
            speak("cannot able to open camera")
    speak("photo capture complete")
    camera.release()
    cv2.destroyAllWindows()
    speak("closing the camera")
    del(camera)
    

def takevideo():  
    capture_duration = 10
    speak('opening camera')
    camera = cv2.VideoCapture(0)
    speak('I will take 2 videos simultaneously')
    for i in range(2):
        speak('taking first video')
        fourcc = cv2.VideoWriter_fourcc(*'XVID') #XVID is a codec to compress the video size
        savepath = 'E:\\vscode\\python\\jarvis\\emmavideo'+str(random.randint(1,1000))+'.avi'
        out = cv2.VideoWriter(savepath,fourcc,20.0,(640,480)) #saved in a location
        start_time=time.time()
        while(int(time.time()-start_time)<capture_duration):
            ret,frame = camera.read()
            if not ret:
                speak('sryy unable to open camera')
                break
            else:
                out.write(frame)
                cv2.imshow('frame',frame)
            
    speak('closing camera')
    camera.release()
    cv2.destroyAllWindows()
    speak('video saved successfully')


    speak("the video was successfully saved")

    

    



if __name__ == "__main__":
    speak("hello mr. sudeep")
    wishMe()
    while True:
        query = takeCommand().lower()

        #login for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'google search' in query:
            try:
                speak("what you want to search")
                query1 = takeCommand().lower()
                webbrowser.open("https://google.com/search?q="+query1)
            except Exception as e:
                print(e)
                speak("unable to fetch")
           

        elif 'play music' in query:
            try:
                speak("what type of music u want to listen")
                m = takeCommand().lower()
                if 'play any music' in m:
                    path = "C:\\Users\\HP\\Music"
                    mus = os.listdir(path)
                    playmus = random.choice(mus)
                    os.startfile(os.path.join(path,playmus))
                    
                elif 'play music from kabir singh' in m:
                    os.startfile("C:\\Users\\HP\\Music\\Mere-Sohneya_(webmusic.in).mp3")
                elif 'play my favourite song' in m:
                    os.startfile("C:\\Users\\HP\\Music\\Gryffin - Body Back ft. Maia Wright (Official Music Video).mp3")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to play music. please check my system")

        
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, now the time is {strTime}")
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<5:
                print("have a good day ahead")
            elif hour>5 and hour<17:
                speak("have a good day")
            elif hour>=17 and hour<24:
                speak("good night")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codepath)

        elif 'send email to nibas' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "bbb@gmail.com" #send mail to this
                sendEmail(to, content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry, can't able to send the email. I am having some trouble in my system")
        
        

        elif 'show me the files in desktop'  in query:
            try:
                print(os.listdir("C:\\Users\\HP\\Desktop"))

            except Exception as e:
                print(e)
                speak('sorry sir, unable to proceed please check my system')
        
        elif 'create file in desktop' in query:
            createfolder()

        elif 'rename file in desktop' in query:
            renamefolder()

        elif 'delete file from desktop' in query:
            deletefolder()

        elif'search file in desktop' in query:
            try:
                searchfilemain()
                
            except Exception as e :
                print(e)
                speak("unable to process sir")

        elif 'take photo' in query:
            try:
                takephoto()
            except Exception as e:
                print(e)
                speak("unable to process")

        elif 'take video' in query:
            try:
                takevideo()
            except Exception as e:
                print(e)
                speak("unable to process")


        elif 'thank you' in query:
            speak("its my duty sir")

        elif 'invisible' in query:
            try:
                execfile('invisible cloak.py')
            except NameError:
                exec(open('invisible cloak.py').read())
        elif  'go to sleep' in query:
            try:
                exit()
            except Exception as e:
                print(e)
                speak("sorry, can't go to sleep now. I am having some trouble in my system")