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
main_window.resizable(0,0)# delete maximize btn
##################WELCOME MESSAGE################################
welcome_msg_label = Label(main_window, text = "Welcome to Biogreenleaf...",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
welcome_msg_label.place(x = 5,y =10)
##################USER & PASSWORD################################
user_name_label = Label(main_window, text = "username: ",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
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
########BUTTON FUNC
def btn_clear():
	user_entry.delete(0,END)
	pass_entry.delete(0,END)
def btn_submit():
	user_entr = user_entry.get()
	pass_entr = pass_entry.get()
	
		
button_exit = Button(main_window, text ="Exit",font = ('Roboto',10,'bold'),padx = 30,fg = 'green',bg ='white',command= main_window.quit)
button_exit.place(x = 20,y = 150)
button_clear = Button(main_window, text ="Clear",font = ('Roboto',10,'bold'),padx = 30,fg = 'green',bg ='white',command= btn_clear)
button_clear.place(x = 135,y = 150)
button_submit = Button(main_window, text ="Submit",font = ('Roboto',10,'bold'),padx = 30,fg = 'green',bg ='white',command= btn_submit)
button_submit.place(x = 260,y = 150)

main_window.mainloop()# placer and listner of events
