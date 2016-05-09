__author__ = "Jordonbc"
import logging
import time

logging.basicConfig(filename='JDE/Logs/' + str(time.strftime('%d-%m-%Y-%H-%M%p') + ".log"), level=logging.DEBUG)
jdeLog = logging.getLogger("JDE.py")

jdeLog.info("Importing tkinter")
try:
    from tkinter import *

    jdeLog.info("Import Successful")
except Exception as e:
    jdeLog.critical(str(e))

jdeLog.info("Importing os")
try:
    import os

    jdeLog.info("Import Successful")
except Exception as e:
    jdeLog.critical(str(e))

jdeLog.info("Importing JDE/Interfaces/login")
try:
    from JDE.Interfaces import login

    jdeLog.info("Import Successful!")
except Exception as e:
    jdeLog.critical(str(e))

jdeLog.info("Importing JDE/Interfaces/desktop")
try:
    from JDE.Interfaces import desktop

    jdeLog.info("Import Successful!")
except Exception as e:
    jdeLog.critical(str(e))

try:
    loginApp = login.login
    loginApp(windowTitle="JDE Login", widthHeight="1280x800", userDirs="Users/", bg="JDE/Images/background.png")
    userFile = open("active", "r")
    username = userFile.read()
    userFile.close()
    os.remove("active")

    print(username)

    desktopApp = desktop.desktop
    desktopApp(username=username)
except Exception as e:
    jdeLog.critical(str(e))
