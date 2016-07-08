__author__ = "Jordonbc"
import logging
import time
import os
import sys

if not os.path.exists("JDE/Logs"):
    os.mkdir("JDE/Logs")

logging.basicConfig(filename='JDE/Logs/' + str(time.strftime('%d-%m-%Y-%H-%M%p') + ".log"), level=logging.DEBUG,
                    datefmt='%I:%M:%S %p',
                    format='%(asctime)s:%(name)s:%(lineno)d}:%(levelname)s - %(message)s')

jdeLog = logging.getLogger(__name__)

jdeLog.info("Python version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2]))

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
    from JDE.Interfaces import desktop as desktop

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

    desktop.desktop(windowTitle="JDE Desktop", username=username)
except Exception as e:
    jdeLog.critical(str(e))
