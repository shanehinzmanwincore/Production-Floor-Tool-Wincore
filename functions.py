"""
This file contains all of the functions for the ProdFloorTool.py
"""
from Tkinter import *
import os
import logging
import logger
import subprocess
import tkMessageBox
import hashlib
import time

#Brings in logger
logger = logger.setup_logger('root') 

#List of all PC's
options = [
        'PKB-SAW1',
        'PKB-SAW2',
        'PKB-SAW3',
        'PKB-SAW4',
        'PKB-SAW5',
        'PKB-SAW6',
        'PKB-SAW7',
        'PKB-SAW8',
        'PKB-SAW9',
        'PKB-SAW10',
        'PKB-SAW11',
        'PKB-SAW12',
        'PKB-SAW-13',
        'PKB-77-INSP-VM',
        'PKB-MLINE-INSP-VM',
        'PKB-54-INSP-VM',
        'PKB-54-AUTO-INSP',
        'PKB-PAINT-INSP',
        'VM-GL-TB-NEW',
        'VM-GL-TB-OLD',
        'PKB-LOADING-1',
        'PKB-LOADING-2',
        'PKB-LOADING-3',
        'PKB-LOADING-4',
        'PKB-LOADING-5',
        'PKB-LOADING6',
        'PKB-LOADING7'
        ]

#Clear text in entry field
def clearButtonClick(self):
    logger.info('Cleared field')
    self.pcEntry.delete(0,  'end')

#Restart specified PC
def restButtonClick(self):
    logger.info('User trying to reboot PC')
    
    #Set function variables
    logger.info('Checking to see if host is alive...')
    checkMessage = "Checking to see if host is alive..."
    outputMessage(self, checkMessage)
    pcName = str(self.pcEntry.get())
    alive = isAlive(pcName)

    #Test to see if there is something in the entry field. This prevents shutting down your PC
    if(pcName == "" or alive == "0"):

        #If the user does not type the PC in, this checks to see if the dropdown has anything of value.
        pcName = str(self.pcDrop.get())
        alive = isAlive(pcName)

        if(pcName == "" or alive == "0"):
            #Host not found
            logger.error('Host not found')
            message = "Cannot reboot, host not found"
            outputMessage(self, message)
        else:
            #Dropdown host found send command
            logger.info('Reboot command successfully sent')
            subprocess.call("shutdown /r /m " + "\\\\" + pcName + ' /c "The Wincore IT Departement is rebooting this PC" /t 005', shell=True)
            message = "Reboot command sent to " + pcName
            outputMessage(self, message)
    else:
        #Entry host found send command
        logger.info('Reboot command successfully sent')
        subprocess.call("shutdown /r /m " + "\\\\" + pcName + ' /c "The Wincore IT Departement is rebooting this PC" /t 005', shell=True)
        message = "Reboot command sent to " + pcName
        outputMessage(self, message)

#Kills TigerStop process on desired machine
def tigerKillButtonClick(self):
    
    logger.info('User trying to kill TigerStop process')
    #Set function variables
    logger.info('Checking to see if host is alive...')
    checkMessage = "Checking to see if host is alive..."
    outputMessage(self, checkMessage)
    pcName = str(self.pcEntry.get())
    alive = isAlive(pcName)

    #Test to see if there is something in the entry field or if the PC is alive. This prevents shutting down your TigerStop software
    if(pcName == "" or alive == "0"):
        
        #If the user does not type the PC in, this checks to see if the dropdown has anything of value. 
        pcName = str(self.pcDrop.get())
        alive = isAlive(pcName)

        if(pcName == "" or alive == "0"):
            #Host not found
            logger.error('Host not found')
            message = "Cannot kill process, host not found."
            outputMessage(self, message)
        else:
            #Dropdown host found send command
            result = killProc(pcName, "FtTigerStop.exe")
            if (result == 1):
                logger.info('Kill TigerStop command successfully sent')
                message = "Kill TigerStop command sent to " + pcName
                outputMessage(self, message)
            else:
                logger.info('Kill TigerStop command was unsuccessful')
                message = "Kill TigerStop command was unsuccessful on " + pcName
                outputMessage(self, message)
                tkMessageBox.showerror("Taskkill Error","There was an error issuing your command. This is most likely cause by: \n - The process is not running on the remote machine \n - WMI service is not running correctly on the remote machine")
    else:
        #Entry host found send command
        result = killProc(pcName, "FtTigerStop.exe")
        if (result == 1):
            logger.info('Kill TigerStop command successfully sent')
            message = "Kill TigerStop command sent to " + pcName
            outputMessage(self, message)
        else:
            logger.info('Kill TigerStop command was unsuccessful')
            message = "Kill TigerStop command was unsuccessful on " + pcName
            outputMessage(self, message)
            tkMessageBox.showerror("Taskkill Error","There was an error issuing your command. This is most likely cause by: \n - The process is not running on the remote machine \n - WMI service is not running correctly on the remote machine")

def trackingKillButtonClick(self):
    
    logger.info('User trying to kill Tracking process')
    #Set function variables
    logger.info('Checking to see if host is alive...')
    checkMessage = "Checking to see if host is alive..."
    outputMessage(self, checkMessage)
    pcName = str(self.pcEntry.get())
    alive = isAlive(pcName)

    #Test to see if there is something in the entry field or if the PC is alive. This prevents shutting down your TigerStop software
    if(pcName == "" or alive == "0"):
        
        #If the user does not type the PC in, this checks to see if the dropdown has anything of value. 
        pcName = str(self.pcDrop.get())
        alive = isAlive(pcName)

        if(pcName == "" or alive == "0"):
            #Host not found
            logger.error('Host not found')
            message = "Cannot kill process, host not found."
            outputMessage(self, message)
        else:
            #Dropdown host found send command
            result = killProc(pcName, "FtTracking.exe")
            if (result == 1):
                logger.info('Kill Tracking command successfully sent')
                message = "Kill Tracking command sent to " + pcName
                outputMessage(self, message)
            else:
                logger.info('Kill Tracking command was unsuccessful')
                message = "Kill Tracking command was unsuccessful on " + pcName
                outputMessage(self, message)
                tkMessageBox.showerror("Taskkill Error","There was an error issuing your command. This is most likely cause by: \n - The process is not running on the remote machine \n - WMI service is not running correctly on the remote machine")
    else:
        #Entry host found send command
        result = killProc(pcName, "FtTracking.exe")
        if (result == 1):
            logger.info('Kill Tracking command successfully sent')
            message = "Kill Tracking command sent to " + pcName
            outputMessage(self, message)
        else:
            logger.info('Kill Tracking command was unsuccessful')
            message = "Kill Tracking command was unsuccessful on " + pcName
            outputMessage(self, message)
            tkMessageBox.showerror("Taskkill Error","There was an error issuing your command. This is most likely cause by: \n - The process is not running on the remote machine \n - WMI service is not running correctly on the remote machine")

def glassInspKillButtonClick(self):
    
    logger.info('User trying to kill glass line inspection process')
    #Set function variables
    logger.info('Checking to see if host is alive...')
    checkMessage = "Checking to see if host is alive..."
    outputMessage(self, checkMessage)
    pcName = str(self.pcEntry.get())
    alive = isAlive(pcName)

    #Test to see if there is something in the entry field or if the PC is alive. This prevents shutting down your TigerStop software
    if(pcName == "" or alive == "0"):
        
        #If the user does not type the PC in, this checks to see if the dropdown has anything of value. 
        pcName = str(self.pcDrop.get())
        alive = isAlive(pcName)

        if(pcName == "" or alive == "0"):
            #Host not found
            logger.error('Host not found')
            message = "Cannot kill process, host not found."
            outputMessage(self, message)
        else:
            #Dropdown host found send command
            result = killProc(pcName, "LnInspection.exe")
            if (result == 1):
                logger.info('Kill glass line inspection command successfully sent')
                message = "Kill glass line inspection command sent to " + pcName
                outputMessage(self, message)
            else:
                logger.info('Kill glass line inspection command was unsuccessful')
                message = "Kill glass line inspection command was unsuccessful on " + pcName
                outputMessage(self, message)
                tkMessageBox.showerror("Taskkill Error","There was an error issuing your command. This is most likely cause by: \n - The process is not running on the remote machine \n - WMI service is not running correctly on the remote machine")
    else:
        #Entry host found send command
        result = killProc(pcName, "LnInspection.exe")
        if (result == 1):
            logger.info('Kill glass line inspection command successfully sent')
            message = "Kill glass line inspection command sent to " + pcName
            outputMessage(self, message)
        else:
            logger.info('Kill glass line inspection command was unsuccessful')
            message = "Kill glass line inspection command was unsuccessful on " + pcName
            outputMessage(self, message)
            tkMessageBox.showerror("Taskkill Error","There was an error issuing your command. This is most likely cause by: \n - The process is not running on the remote machine \n - WMI service is not running correctly on the remote machine")

def truckingKillButtonClick(self):
    
    logger.info('User trying to kill Trucking process')
    #Set function variables
    logger.info('Checking to see if host is alive...')
    checkMessage = "Checking to see if host is alive..."
    outputMessage(self, checkMessage)
    pcName = str(self.pcEntry.get())
    alive = isAlive(pcName)

    #Test to see if there is something in the entry field or if the PC is alive. This prevents shutting down your TigerStop software
    if(pcName == "" or alive == "0"):
        
        #If the user does not type the PC in, this checks to see if the dropdown has anything of value. 
        pcName = str(self.pcDrop.get())
        alive = isAlive(pcName)

        if(pcName == "" or alive == "0"):
            #Host not found
            logger.error('Host not found')
            message = "Cannot kill process, host not found."
            outputMessage(self, message)
        else:
            #Dropdown host found send command
            result = killProc(pcName, "FtTrucking.exe")
            if (result == 1):
                logger.info('Kill Trucking command successfully sent')
                message = "Kill Trucking command sent to " + pcName
                outputMessage(self, message)
            else:
                logger.info('Kill Trucking command was unsuccessful')
                message = "Kill Trucking command was unsuccessful on " + pcName
                outputMessage(self, message)
                tkMessageBox.showerror("Taskkill Error","There was an error issuing your command. This is most likely cause by: \n - The process is not running on the remote machine \n - WMI service is not running correctly on the remote machine")
    else:
        #Entry host found send command
        result = killProc(pcName, "FtTrucking.exe")
        if (result == 1):
            logger.info('Kill Trucking command successfully sent')
            message = "Kill Trucking command sent to " + pcName
            outputMessage(self, message)
        else:
            logger.info('Kill Trucking command was unsuccessful')
            message = "Kill Trucking command was unsuccessful on " + pcName
            outputMessage(self, message)
            tkMessageBox.showerror("Taskkill Error","There was an error issuing your command. This is most likely cause by: \n - The process is not running on the remote machine \n - WMI service is not running correctly on the remote machine")

#Determines if host is alive by pinging the host
def isAlive(name):
    
    hostname = name

    response = subprocess.call("ping -n 1 " + hostname, shell=True)
    if response == 0:
        #Host found, no error from ping
        return "1"
    else:
        #Host not found, error from ping
        return "0"

#Output message
def outputMessage(self, message):
    self.output.insert(END, str(message) + "\n")
    self.output.grid()

def pcButton(self, n):
    logger.info('User selected ' + n + ' PC')
    clearButtonClick(self)
    self.pcEntry.insert(END, n)

#Need this to be able to close windows
def on_closing(self, master):
    logger.info('User closed application')
    master.destroy()
    self.login.destroy()
    self.addLogin.destroy()

#Adds user
def addUser(self, master):
    addName = str(self.addLogin.addNameEntry.get())
    addPassword = str(self.addLogin.addPassEntry.get())

    outputMessage(self, 'Adding user ' + addName)
    logger.info('Adding user ' + addName)

    #Encrypt password
    addPassword = encryptText(self, addPassword)

    #Read file
    users = []
    with open("\\\\fs01\\share\\IT\\Shane\\log\\users.txt") as f:
        for line in f:
            users.append([str(n) for n in line.strip().split(',')])
    
    #Checks to see if user exists
    valid = 0
    i = 0
    while i < len(users):
        creds = users[i]
        currentCreds = [addName, addPassword]

        if(currentCreds[0] != creds[0]):
            valid += 0
        else:
            valid += 1
            break
        i += 1

    #If user does not exist, add the user
    if (valid == 0):
        userFile = open("\\\\fs01\\share\\IT\\Shane\\log\\users.txt", "a")
        userFile.write("\n")
        userFile.write(addName + "," + addPassword)
        userFile.close()
        master.deiconify()
        self.login.withdraw()
        self.addLogin.withdraw()
        tkMessageBox.showinfo("Add User", "Added User!")
        logger.info('Added user')
        outputMessage(self, 'Added User')
    #If user exists, do not add user
    else:
        tkMessageBox.showerror("Add User", "User exists!")
        logger.info('Adding user unsuccessful')
        outputMessage(self, 'Adding user unsuccessful')
        self.addLogin.addNameEntry.delete(0,  'end')
        self.addLogin.addPassEntry.delete(0,  'end')

#Login method
def auth(self, master):
    name = str(self.login.nameEntry.get())
    password = str(self.login.passEntry.get())

    password = encryptText(self, password)

    users = []
    with open("\\\\fs01\\share\\IT\\Shane\\log\\users.txt") as f:
        for line in f:
            users.append([str(n) for n in line.strip().split(',')])
    
    #Checks to see if user is in user database file
    valid = 0
    i = 0
    while i < len(users):
        creds = users[i]
        if(("['" + name + "', '" + password + "']") == str(creds)):
            valid = 1
            master.deiconify()
            self.login.withdraw()
            self.addLogin.withdraw()
            logger.warning(name + ' logged in')
            break
        else:
            valid = 0
        i += 1
    
    #If user is not in file, do not let them in
    if (valid == 0): 
        logger.info('Login unsuccessful')
        tkMessageBox.showerror("Login", "Invalid Login!")
        self.login.nameEntry.delete(0,  'end')
        self.login.passEntry.delete(0,  'end')
    #If user is in file, let them in
    else:
        logger.info('Login successful')

#Initialize menu UI
def initUI(self):
    logger.info('Loading main menu')

    self.master.title("Menu")
    
    menubar = Menu(self.master)
    self.master.config(menu=menubar)
    
    fileMenu = Menu(menubar)
    toolsMenu = Menu(menubar)

    #Adding menu items
    fileMenu.add_command(label="Exit", command = lambda: onExit(self))
    fileMenu.add_command(label="Logout", command = lambda: menuLogin(self))
    fileMenu.add_command(label="Add User", command = lambda: addUserButtonClick(self))
    menubar.add_cascade(label="File", menu=fileMenu)

    toolsMenu.add_command(label="Refresh View", command = lambda: PCRef(self, options))
    toolsMenu.add_command(label="Remove Batch", command = lambda: removeBatch(self, options))
    menubar.add_cascade(label="Tools", menu=toolsMenu)

    logger.info('Menu load complete')

#Add user window menu
def addUserMenu(self):
    logger.info('Loading add user menu')

    self.addLogin.title("Menu")
    
    menubar = Menu(self.addLogin)
    self.addLogin.config(menu=menubar)
    
    addUserFileMenu = Menu(menubar)

    #Adding menu items
    addUserFileMenu.add_command(label="Back", command = lambda: backAddUser(self))
    menubar.add_cascade(label="File", menu=addUserFileMenu)

#Exit application
def onExit(self):
    logger.info('User closed application')
    self.quit()

#Login button on menu button function
def menuLogin(self):
    logger.info('User logged out')
    self.login.deiconify()
    self.master.withdraw()
    self.addLogin.withdraw()  
    self.login.nameEntry.delete(0,  'end')
    self.login.passEntry.delete(0,  'end')   

#Add user on menu button function
def addUserButtonClick(self):
    logger.info('Adding User')
    self.addLogin.deiconify()
    self.login.withdraw()
    self.master.withdraw()
    self.addLogin.addNameEntry.delete(0,  'end')
    self.addLogin.addPassEntry.delete(0,  'end')

#Encrypts text with sha512
def encryptText(self, text):
    text = hashlib.sha512(text)
    text = text.hexdigest()
    return text

#Back  button fot adding user window
def backAddUser(self):
    logger.info('Stopped adding user')
    self.addLogin.withdraw()
    self.login.withdraw()
    self.master.deiconify()

#Kill a process
def killProc(pcName, proc):
    p = subprocess.Popen('taskkill /s ' + pcName + ' /IM ' + proc + ' /f', stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if (output == ""):
        return 0
    else:
        return 1

#Checks to see if PC is alive and then gives it the right button color
def btnColor(self, PC):
    outputMessage(self, 'Checking ' + PC)
    if(isAlive(PC) == "1"):
        return '#08B8FF'
    else:
        return 'red'

#Removes all batch files on desktop of the PC's in the options list
def removeBatch(self, options):
    i=0
    while i < len(options):
        subprocess.call('WMIC /node:"' + options[i] + '" process call create "cmd.exe /c del %userprofile%\Desktop\*.bat /force"', shell = True)
        i += 1
    outputMessage(self, 'Removed all desktop batch file icons')
    logger.info('Removed all desktop batch file icons')

#Looks through all of the computers to see what button color the PC will have. Blue for alive red for dead
def PCRef(self, options):
    i=0
    while i < len(options):
        btnColor(self, options[i])
        i += 1

'''
This function currently runs as the user that runs this program. I need it to be ran as another user with my privileges
Ill be back for you...|
                      V
def startProc(pcName, proc):
    if (proc == "TigerStop"):
        p = subprocess.Popen("""WMIC /node:""" + '"' + pcName + '"' +  """ process call create 'cmd.exe /c "C:\Program Files (x86)\FeneVision\TigerStop HMI\FtTigerStop.exe"'""", stdout=subprocess.PIPE, shell=True)
        time.sleep(.4)
        subprocess.call('taskkill /s ' + pcName + ' /IM cmd.exe /f')
        (output, err) = p.communicate()
        print (output)
        print (err)
        if (output == ""):
            return 0
        else:
            return 1
'''