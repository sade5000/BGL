# !bin/etc
#This soft is created by https://github.com/sade5000
################################################################LOGO
print('=========================================================')
print(' ****   **   **     ****   ****   **    **    **' )
print(' *     *  *  *  *   *      *     *  *  *  *  *  *')
print(' ****  ****  *  *   ****   ****  *  *  *  *  *  *')
print('    *  *  *  *  *   *         *  *  *  *  *  *  *')
print(' ****  *  *  * *    ****   ****   **    **    ** ')
print('=========================================================')
#########################LIBRARY################################
import sys
import os
import socket
import requests
from tkinter import*
#########################WINDOW CONFIG##########################

main_window = Tk() #instance of the main window
window_logo = PhotoImage(file='logo_soft.png')
#welcome_msg_img = PhotoImage(file='logo_soft_20x20.png')
main_window.geometry("400x200")
main_window.title("BioGreenleaf")
main_window.iconphoto(True, window_logo)
main_window.config(background="black")


##################WELCOME MESSAGE################################
welcome_msg_label = Label(main_window, text = "Welcome to Biogreenleaf...",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
					#image = welcome_msg_img,compound= 'left')
welcome_msg_label.place(x = 5,y =10)
##################USER & PASSWORD################################
user_name_label = Label(main_window, text = "username: ",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
					#image = welcome_msg_img,compound= 'left')
user_name_label.place(x = 100,y=50)
user_entry = Entry(main_window,font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
user_entry.place(x =200,y = 50)
password_label = Label(main_window, text = "password: ",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
password_label.place(x = 100,y=100)
pass_entry = Entry(main_window,font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
pass_entry.config(show = "*")
pass_entry.place(x =200,y = 100)

#####################BUTTONS & SUBMIT###########################


main_window.mainloop()# placer and listner of events
