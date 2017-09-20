"""
ProdFloorTool.py is designed to be used by the Wincore IT department. 
It is currently made to used with all of the window plant VM's.
More features can be added.
This file contains all of the GUI elements of the program.
The functions.py file contains all of the functions. 
The logger.py file includes the logger for the whole application. 
"""
from Tkinter import *
from PIL import Image, ImageTk
import functions
import threading
from threading import Thread
import time
import Tkinter as tk

class GUI(Frame):

    def __init__(self,master=None):

        #Set up master
        master = Tk()
        master.title("ProdFloorTool V2.3.3")
        master.configure(background = 'lightgrey', border = '5')
        master.geometry("1605x830")

        #Init frame
        functions.logger.info('Loading main window')
        Frame.__init__(self, master)
        self.grid()
        functions.initUI(self)

        #List of PC's created in the functions file 
        options = functions.options
        options = ['Select One'] + options
     
        #First text label in program
        self.pcLabel = Label(master, text="Please enter desired PC name:")
        self.pcLabel.grid(column = 0, row = 0, columnspan=2, padx = 5, pady = 5, sticky = W)
        self.pcLabel.configure(background = 'lightgrey')

        #User input field to enter PC
        self.pcEntry = StringVar()
        self.pcEntry = Entry(textvariable=self.pcEntry)
        self.pcEntry.grid(column = 2, row = 0, padx = 5, pady = 5, sticky = W+E)

        #Drop down label
        self.pcDropLabel = Label(master, text="Or select a PC from the list:")
        self.pcDropLabel.grid(column = 0, row = 1, columnspan = 2, padx = 5, pady = 5, sticky = W)
        self.pcDropLabel.configure(background = 'lightgrey')

        #Dropdown for user to select PC
        self.pcDrop = StringVar()
        self.drop = OptionMenu(master, self.pcDrop, *options)
        self.pcDrop.set(options[0])
        self.drop.grid(column = 2, row = 1, columnspan = 2, padx = 5, pady = 5, sticky = W+E)
        self.drop.configure(highlightbackground = 'lightgrey', cursor = "hand2")

        #Clear button
        self.clearTextButton = Button(master, text="Clear", command = lambda: functions.clearButtonClick(self))
        self.clearTextButton.grid(column = 3, row = 0, padx = 5, pady = 5, sticky = W+E)
        self.clearTextButton.configure(cursor = "hand2")

        #Restart button
        self.restSubmitButton = Button(master, text="Restart PC", command = lambda: functions.restButtonClick(self))
        self.restSubmitButton.grid(column = 0, row = 6, padx = 5, pady = 5, sticky = W+E)
        self.restSubmitButton.configure(background = 'red', cursor = "hand2")

        #Kill tiger process button
        self.tigerKillSubmitButton = Button(master, text="Kill TigerStop", command = lambda: functions.tigerKillButtonClick(self))
        self.tigerKillSubmitButton.grid(column = 0, row = 2, padx = 5, pady = 5, sticky = W+E)
        self.tigerKillSubmitButton.configure(background = 'yellow', cursor = "hand2")

        #Kill tracking process button
        self.trackingKillSubmitButton = Button(master, text="Kill Tracking", command = lambda: functions.trackingKillButtonClick(self))
        self.trackingKillSubmitButton.grid(column = 0, row = 3, padx = 5, pady = 5, sticky = W+E)
        self.trackingKillSubmitButton.configure(background = 'yellow', cursor = "hand2")

        #Kill trucking process button
        self.truckingKillSubmitButton = Button(master, text="Kill Trucking", command = lambda: functions.truckingKillButtonClick(self))
        self.truckingKillSubmitButton.grid(column = 0, row = 4, padx = 5, pady = 5, sticky = W+E)
        self.truckingKillSubmitButton.configure(background = 'yellow', cursor = "hand2")

        #Kill glass inspection process button
        self.glassInspKillSubmitButton = Button(master, text="Kill Glass", command = lambda: functions.glassInspKillButtonClick(self))
        self.glassInspKillSubmitButton.grid(column = 0, row = 5, padx = 5, pady = 5, sticky = W+E)
        self.glassInspKillSubmitButton.configure(background = 'yellow', cursor = "hand2")

        #Output box
        self.outputvscrollbar = tk.Scrollbar(master)

        self.output = Text(master, width = 40, height = 6)
        self.output.grid(column = 1, row = 2, columnspan = 3, rowspan = 1980, padx = 5, pady = 0, sticky = W+E+N+S)
        self.output.configure(background = 'black', foreground = 'lime', yscrollcommand = self.outputvscrollbar.set)

        self.outputvscrollbar.config(command = self.output.yview)
        self.outputvscrollbar.grid(column = 6, row = 2, rowspan = 1980, sticky = N+S+W)
        
        #Floor layout image
        photo = ImageTk.PhotoImage(Image.open('floor.PNG'))
        self.label = Label(image = photo)
        self.label.image = photo

        #Canvas
        self.vscrollbar = tk.Scrollbar(master)
        self.yscrollbar = tk.Scrollbar(master)
        
        self.mainCan = Canvas(master, width = "1120", height = "780", yscrollcommand = self.vscrollbar.set, xscrollcommand  = self.yscrollbar.set, scrollregion=(0,0,2240,1560))
        self.mainCan.grid(column = 10, row = 1, rowspan = 1979, columnspan = 1000, sticky = N+S+E+W)

        self.vscrollbar.config(command = self.mainCan.yview)
        self.vscrollbar.grid(column = 9, row = 1, rowspan = 1979, padx = (10, 0), sticky = N+S+E)

        self.yscrollbar.config(command = self.mainCan.xview, orient='horizontal')
        self.yscrollbar.grid(column = 9, row = 0, columnspan = 2000, padx = (10, 0), pady = (0,0),  sticky = E+W+S)

        #Canvas Background
        self.canBackground = self.mainCan.create_image(0,0, image = photo, anchor = "nw")

        #Saw1 button
        self.saw1 = Button(master, text="1", command = lambda: functions.pcButton(self, 'PKB-SAW1'))
        self.saw1.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw1.configure(width = 1, cursor = "hand2")
        self.saw1_window = self.mainCan.create_window(450, 272, window = self.saw1)
        self.saw1.hostName = 'PKB-SAW1'
        functions.thinClients.append(self.saw1)

        #Saw2 button
        self.saw2 = Button(master, text="2", command = lambda: functions.pcButton(self, 'PKB-SAW2'))
        self.saw2.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw2.configure(width = 1, cursor = "hand2")
        self.saw2_window = self.mainCan.create_window(405, 272, window = self.saw2)
        self.saw2.hostName = 'PKB-SAW2'
        functions.thinClients.append(self.saw2)

        #Saw3 button
        self.saw3 = Button(master, text="3", command = lambda: functions.pcButton(self, 'PKB-SAW3'))
        self.saw3.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw3.configure(width = 1, cursor = "hand2")
        self.saw3_window = self.mainCan.create_window(356, 272, window = self.saw3)
        self.saw3.hostName = 'PKB-SAW3'
        functions.thinClients.append(self.saw3)

        #Saw4 button
        self.saw4 = Button(master, text="4", command = lambda: functions.pcButton(self, 'PKB-SAW4'))
        self.saw4.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw4.configure(width = 1, cursor = "hand2")
        self.saw4_window = self.mainCan.create_window(335, 272, window = self.saw4)
        self.saw4.hostName = 'PKB-SAW4'
        functions.thinClients.append(self.saw4)

        #Saw5 button
        self.saw5 = Button(master, text="5", command = lambda: functions.pcButton(self, 'PKB-SAW5'))
        self.saw5.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw5.configure(width = 1, cursor = "hand2")
        self.saw5_window = self.mainCan.create_window(295, 272, window = self.saw5)
        self.saw5.hostName = 'PKB-SAW5'
        functions.thinClients.append(self.saw5)

        #Saw6 button
        self.saw6 = Button(master, text="6", command = lambda: functions.pcButton(self, 'PKB-SAW6'))
        self.saw6.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw6.configure(width = 1, cursor = "hand2")
        self.saw6_window = self.mainCan.create_window(275, 272, window = self.saw6)
        self.saw6.hostName = 'PKB-SAW6'
        functions.thinClients.append(self.saw6)

        #Saw7 button
        self.saw7 = Button(master, text="7", command = lambda: functions.pcButton(self, 'PKB-SAW7'))
        self.saw7.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw7.configure(width = 1, cursor = "hand2")
        self.saw7_window = self.mainCan.create_window(245, 272, window = self.saw7)
        self.saw7.hostName = 'PKB-SAW7'
        functions.thinClients.append(self.saw7)

        #Saw8 button
        self.saw8 = Button(master, text="8", command = lambda: functions.pcButton(self, 'PKB-SAW8'))
        self.saw8.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw8.configure(width = 1, cursor = "hand2")
        self.saw8_window = self.mainCan.create_window(225, 272, window = self.saw8)
        self.saw8.hostName = 'PKB-SAW8'
        functions.thinClients.append(self.saw8)

        #Saw9 button
        self.saw9 = Button(master, text="9", command = lambda: functions.pcButton(self, 'PKB-SAW9'))
        self.saw9.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw9.configure(width = 1, cursor = "hand2")
        self.saw9_window = self.mainCan.create_window(879, 272, window = self.saw9)
        self.saw9.hostName = 'PKB-SAW9'
        functions.thinClients.append(self.saw9)

        #Saw10 button
        self.saw10 = Button(master, text="10", command = lambda: functions.pcButton(self, 'PKB-SAW10'))
        self.saw10.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw10.configure(width = 1, cursor = "hand2")
        self.saw10_window = self.mainCan.create_window(803, 272, window = self.saw10)
        self.saw10.hostName = 'PKB-SAW10'
        functions.thinClients.append(self.saw10)

        #Saw11 button
        self.saw11 = Button(master, text="11", command = lambda: functions.pcButton(self, 'PKB-SAW11'))
        self.saw11.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw11.configure(width = 1, cursor = "hand2")
        self.saw11_window = self.mainCan.create_window(900, 272, window = self.saw11)
        self.saw11.hostName = 'PKB-SAW11'
        functions.thinClients.append(self.saw11)
        
        #Saw12 button
        self.saw12 = Button(master, text="12", command = lambda: functions.pcButton(self, 'PKB-SAW12'))
        self.saw12.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw12.configure(width = 1, cursor = "hand2")
        self.saw12_window = self.mainCan.create_window(783, 272, window = self.saw12)
        self.saw12.hostName = 'PKB-SAW12'
        functions.thinClients.append(self.saw12)

        #Saw13 button
        self.saw13 = Button(master, text="13", command = lambda: functions.pcButton(self, 'PKB-SAW-13'))
        self.saw13.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.saw13.configure(width = 1, cursor = "hand2")
        self.saw13_window = self.mainCan.create_window(840, 272, window = self.saw13)
        self.saw13.hostName = 'PKB-SAW-13'
        functions.thinClients.append(self.saw13)

        #77 inspection button
        self.insp77 = Button(master, text="77", command = lambda: functions.pcButton(self, 'PKB-77-INSP-VM'))
        self.insp77.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.insp77.configure(width = 1, cursor = "hand2")
        self.insp77_window = self.mainCan.create_window(256, 595, window = self.insp77)
        self.insp77.hostName = 'PKB-77-INSP-VM'
        functions.thinClients.append(self.insp77)

        #Center inspection button
        self.inspCenter = Button(master, text="C", command = lambda: functions.pcButton(self, 'PKB-MLINE-INSP-VM'))
        self.inspCenter.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.inspCenter.configure(width = 1, cursor = "hand2")
        self.inspCenter_window = self.mainCan.create_window(363, 595, window = self.inspCenter)
        self.inspCenter.hostName = 'PKB-MLINE-INSP-VM'
        functions.thinClients.append(self.inspCenter)

        #54 inspection button
        self.insp54 = Button(master, text="54", command = lambda: functions.pcButton(self, 'PKB-54-INSP-VM'))
        self.insp54.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.insp54.configure(width = 1, cursor = "hand2")
        self.insp54_window = self.mainCan.create_window(809, 546, window = self.insp54)
        self.insp54.hostName = 'PKB-54-INSP-VM'
        functions.thinClients.append(self.insp54)

        #54 auto inspection button
        self.insp54a = Button(master, text="A", command = lambda: functions.pcButton(self, 'PKB-54-AUTO-INSP'))
        self.insp54a.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.insp54a.configure(width = 1, cursor = "hand2")
        self.insp54a_window = self.mainCan.create_window(1020, 542, window = self.insp54a)
        self.insp54a.hostName = 'PKB-54-AUTO-INSP'
        functions.thinClients.append(self.insp54a)

        #Paint inspection button
        self.inspPaint = Button(master, text="P", command = lambda: functions.pcButton(self, 'PKB-PAINT-INSP'))
        self.inspPaint.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.inspPaint.configure(width = 1, cursor = "hand2")
        self.inspPaint_window = self.mainCan.create_window(1059, 38, window = self.inspPaint)
        self.inspPaint.hostName = 'PKB-PAINT-INSP'
        functions.thinClients.append(self.inspPaint)

        #Glass repair line
        self.glassRepair = Button(master, text="GR", command = lambda: functions.pcButton(self, 'VM-GL-TB-NEW'))
        self.glassRepair.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.glassRepair.configure(width = 1, cursor = "hand2")
        self.glassRepair_window = self.mainCan.create_window(532, 390, window = self.glassRepair)
        self.glassRepair.hostName = 'VM-GL-TB-NEW'
        functions.thinClients.append(self.glassRepair)

        #Glass Main line
        self.glassMain = Button(master, text="GM", command = lambda: functions.pcButton(self, 'VM-GL-TB-OLD'))
        self.glassMain.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.glassMain.configure(width = 1, cursor = "hand2")
        self.glassMain_window = self.mainCan.create_window(685, 425, window = self.glassMain)
        self.glassMain.hostName = 'VM-GL-TB-OLD'
        functions.thinClients.append(self.glassMain)

        #Loading 1
        self.loading1 = Button(master, text="L1", command = lambda: functions.pcButton(self, 'PKB-LOADING-1'))
        self.loading1.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.loading1.configure(width = 1, cursor = "hand2")
        self.loading1_window = self.mainCan.create_window(594, 765, window = self.loading1)
        self.loading1.hostName = 'PKB-LOADING-1'
        functions.thinClients.append(self.loading1)

        #Loading 2
        self.loading2 = Button(master, text="L2", command = lambda: functions.pcButton(self, 'PKB-LOADING-2'))
        self.loading2.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.loading2.configure(width = 1, cursor = "hand2")
        self.loading2_window = self.mainCan.create_window(558, 765, window = self.loading2)
        self.loading2.hostName = 'PKB-LOADING-2'
        functions.thinClients.append(self.loading2)

        #Loading 3
        self.loading3 = Button(master, text="L3", command = lambda: functions.pcButton(self, 'PKB-LOADING-3'))
        self.loading3.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.loading3.configure(width = 1, cursor = "hand2")
        self.loading3_window = self.mainCan.create_window(522, 765, window = self.loading3)
        self.loading3.hostName = 'PKB-LOADING-3'
        functions.thinClients.append(self.loading3)

        #Loading 4
        self.loading4 = Button(master, text="L4", command = lambda: functions.pcButton(self, 'PKB-LOADING-4'))
        self.loading4.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.loading4.configure(width = 1, cursor = "hand2")
        self.loading4_window = self.mainCan.create_window(487, 765, window = self.loading4)
        self.loading4.hostName = 'PKB-LOADING-4'
        functions.thinClients.append(self.loading4)

        #Loading 5
        self.loading5 = Button(master, text="L5", command = lambda: functions.pcButton(self, 'PKB-LOADING-5'))
        self.loading5.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.loading5.configure(width = 1, cursor = "hand2")
        self.loading5_window = self.mainCan.create_window(453, 765, window = self.loading5)
        self.loading5.hostName = 'PKB-LOADING-5'
        functions.thinClients.append(self.loading5)

        #Loading 6
        self.loading6 = Button(master, text="L6", command = lambda: functions.pcButton(self, 'PKB-LOADING6'))
        self.loading6.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.loading6.configure(width = 1, cursor = "hand2")
        self.loading6_window = self.mainCan.create_window(1106, 685, window = self.loading6)
        self.loading6.hostName = 'PKB-LOADING6'
        functions.thinClients.append(self.loading6)

        #Loading 7
        self.loading7 = Button(master, text="L7", command = lambda: functions.pcButton(self, 'PKB-LOADING7'))
        self.loading7.grid(padx = 0, pady = 0, sticky = W+E+N+S)
        self.loading7.configure(width = 1, cursor = "hand2")
        self.loading7_window = self.mainCan.create_window(1106, 748, window = self.loading7)
        self.loading7.hostName = 'PKB-LOADING7'
        functions.thinClients.append(self.loading7)

        functions.logger.info('Main window load complete')

        #Hides master window on startup
        master.withdraw()

        """
        End main window
        Start add user window
        """

        functions.logger.info('Loading add user window')

        #Add user window
        self.addLogin = Tk()
        self.addLogin.title("Add User")
        self.addLogin.configure(background = 'lightgrey', border = '5')

        #Add user username label
        self.addLogin.addUserLabel = Label(self.addLogin, text="Please enter the new users username: ")
        self.addLogin.addUserLabel.grid(row = 0, column = 0)
        self.addLogin.addUserLabel.configure(background = 'lightgrey')

        #Add user username entry
        self.addLogin.addNameEntry = StringVar()
        self.addLogin.addNameEntry = Entry(self.addLogin, textvariable=self.addLogin.addNameEntry)
        self.addLogin.addNameEntry.grid(row = 0, column = 1)

        #Add user pass label
        self.addLogin.addPassLabel = Label(self.addLogin, text="Please enter the new users password: ")
        self.addLogin.addPassLabel.grid(row = 1, column = 0)
        self.addLogin.addPassLabel.configure(background = 'lightgrey')

        #Add user pass entry
        self.addLogin.addPassEntry = StringVar()
        self.addLogin.addPassEntry = Entry(self.addLogin, show = "*", textvariable=self.addLogin.addPassEntry)
        self.addLogin.addPassEntry.grid(row = 1, column = 1)

        #Add user button
        self.addLogin.addLoginButton = Button(self.addLogin, text="Add User", command = lambda: functions.addUser(self, master))
        self.addLogin.addLoginButton.grid(row = 2, column = 0, columnspan = 2)

        #Hide window until called upon
        self.addLogin.withdraw()

        functions.addUserMenu(self)

        functions.logger.info('Add user window load complete')

        """
        End add user window
        Start login window
        """

        functions.logger.info('Loading login')
        
        #Login window
        self.login = Tk()
        self.login.title("Login")
        self.login.configure(background = 'lightgrey', border = '5')

        #Login user label
        self.login.userLabel = Label(self.login, text="Please enter your username: ")
        self.login.userLabel.grid(row = 0, column = 0)
        self.login.userLabel.configure(background = 'lightgrey')

        #Login user entry
        self.login.nameEntry = StringVar()
        self.login.nameEntry = Entry(self.login, textvariable=self.login.nameEntry)
        self.login.nameEntry.grid(row = 0, column = 1)

        #Login pass label
        self.login.passLabel = Label(self.login, text="Please enter your password: ")
        self.login.passLabel.grid(row = 1, column = 0)
        self.login.passLabel.configure(background = 'lightgrey')

        #Login pass entry
        self.login.passEntry = StringVar()
        self.login.passEntry = Entry(self.login, show = "*", textvariable=self.login.passEntry)
        self.login.passEntry.grid(row = 1, column = 1)

        #Login user button
        self.login.loginButton = Button(self.login, text="Login", command = lambda: functions.auth(self, master))
        self.login.loginButton.grid(row = 2, column = 0, columnspan = 2)

        functions.logger.info('Login load complete')

        """
        End login window
        """

        #Need this to be able to close windows as well
        self.login.protocol("WM_DELETE_WINDOW", lambda: functions.on_closing(self, master))
        self.addLogin.protocol("WM_DELETE_WINDOW", lambda: functions.on_closing(self, master))
        master.protocol("WM_DELETE_WINDOW", lambda: functions.on_closing(self, master))

#main loop
if __name__ == "__main__":
    
    guiFrame = GUI()
    guiFrame.mainloop()
