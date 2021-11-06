import os, threading, sys, time
from playsound import playsound
from zipfile import ZipFile
from win32com.client import Dispatch
os.system('mode con: cols=50 lines=6')
def installer():
    with ZipFile(resource_path('data.zip'), 'r') as zipObj: 
        zipObj.extractall(f"{os.getenv('APPDATA')}\\Labyinstaller") #change directory
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def labyinstallersplash():
    print("|  _ |_ |_|")
    print("|_(_||_) _|")
    print("installer")
    print("")
def clearcmd():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # 
        command = 'cls'
    os.system(command)
def bgm():
    while True:
        playsound(resource_path("music.mp3"), block=False)
        time.sleep(248)
bgmm = threading.Thread(target=bgm)
bgmm.start()
clearcmd()
labyinstallersplash()

def installerwindow():
    print("Hey, would you like to install Labyinstaller? y/n") #change ame of the software (labyinstaller)
    answer = input("")
    if answer == "y":
        clearcmd()
        labyinstallersplash()
        print("Please wait a moment! Laby is doing her job!")
        installer()
        clearcmd()
        labyinstallersplash()
        print("Laby did it!")
    elif answer == "n":
        clearcmd()
        labyinstallersplash()
        print("Well, just enjoy the Music then~~")
        input("")
    else:
        clearcmd()
        labyinstallersplash()
        print("no no no! write y for yes or n for no!")
        time.sleep(3)
        clearcmd()
        labyinstallersplash()
        installerwindow()


installerwindow()
