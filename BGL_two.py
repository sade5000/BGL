# !bin/etc
#This contain the main menu......more to writte
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
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sys
import os
import socket
import requests
########################WINDOW CONFIG###########################
menu_window = Tk()
menu_window.geometry("1024x768")
menu_window.title("Biogreenleaf-menu")
menu_window_logo = PhotoImage(file='logo_soft.png')
menu_window.iconphoto(True,menu_window_logo)
menu_window.config(background= "black")
######################LABEL FIRST##############################
menu_first_msg =  Label(menu_window, text = "Welcome to Menu page...",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
menu_first_msg.grid(row = 0 , column = 0)
######################TOP BUTTONS###############################
###FIRST BUTTON COMBOBOX- Add btn
head_one_tabel_label_none =  Label(menu_window, text = " ",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_one_tabel_label_none.grid(row = 1, column = 0)
head_one_tabel_label =  Label(menu_window, text = "Add Item",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_one_tabel_label.grid(row = 2 , column = 0)
def when_is_clicked(event):
	# open a new window
	print("")
btn_list = ["None","Products","Companies"]
action = StringVar()
action.set(btn_list[0])
btn_add_combo = ttk.Combobox(menu_window,value= btn_list )
btn_add_combo.bind("<<ComboboxSelected>>",when_is_clicked)
btn_add_combo['state'] = 'readonly'
btn_add_combo.grid(row= 3,column = 0)
###SECOND BUTTON COMBOBOX - Orders
head_two_tabel_label_none =  Label(menu_window, text = " ",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_two_tabel_label_none.grid(row = 1, column = 1)
head_two_tabel_label =  Label(menu_window, text = "Orders",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_two_tabel_label.grid(row = 2 , column = 1)
def when_is_clicked(event):
	# open a new window
	print("")
btn_list_two = ["None","For Sellers","For Buyers"]
action = StringVar()
action.set(btn_list_two[0])
btn_ord_combo = ttk.Combobox(menu_window,value= btn_list_two )
btn_ord_combo.bind("<<ComboboxSelected>>",when_is_clicked)
btn_ord_combo['state'] = 'readonly'
btn_ord_combo.grid(row= 3,column = 1)


menu_window.mainloop()
