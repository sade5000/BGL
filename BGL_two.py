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
menu_first_msg.place(x = 5 , y = 10)
######################TOP BUTTONS###############################
###FIRST BUTTON COMBOBOX- Add btn
head_one_tabel_label_none =  Label(menu_window, text = " ",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_one_tabel_label_none.place(x = 5, y = 15)
head_one_tabel_label =  Label(menu_window, text = "Add Item",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_one_tabel_label.place(x =80 , y = 40)
def when_is_clicked(event):
	# open a new window
	print("click")
btn_list = ["None","Products","Companies"]
action = StringVar()
action.set(btn_list[0])
btn_add_combo = ttk.Combobox(menu_window,value= btn_list )
btn_add_combo.bind("<<ComboboxSelected>>",when_is_clicked)
btn_add_combo['state'] = 'readonly'
btn_add_combo.place(x = 20,y = 60)
###SECOND BUTTON COMBOBOX - Orders

head_two_tabel_label =  Label(menu_window, text = "Orders",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_two_tabel_label.place(x = 310,y = 40)
def when_is_clicked(event):
	# open a new window
	print("click")
btn_list_two = ["None","For Sellers","For Buyers"]
action = StringVar()
action.set(btn_list_two[0])
btn_ord_combo = ttk.Combobox(menu_window,value= btn_list_two )
btn_ord_combo.bind("<<ComboboxSelected>>",when_is_clicked)
btn_ord_combo['state'] = 'readonly'
btn_ord_combo.place(x = 240,y = 60)
###THIRD BUTTON - Connect/Deals
head_three_tabel_label =  Label(menu_window, text = "Connect Deals",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_three_tabel_label.place(x = 500,y = 40)

def deals():
	print("btn was clicked")
btn_cnt_deal = Button(menu_window, text= "Connect", font=('Roboto',10,'bold'), padx = 60, pady = -10,fg= "Green", bg= "white", command= deals)
btn_cnt_deal.place(x = 460,y = 60)
###FORTH BUTTON - status
head_forth_tabel_label =  Label(menu_window, text = "Deal Status",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_forth_tabel_label.place(x = 720,y = 40)

def deals():
	print("btn was clicked")
btn_cnt_status = Button(menu_window, text= "Status", font=('Roboto',10,'bold'), padx = 60, pady = -10,fg= "Green", bg= "white", command= deals)
btn_cnt_status.place(x = 670,y = 60)
###FIFTH BUTTON - options
head_fifth_tabel_label =  Label(menu_window, text = "Settings",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'black')
head_fifth_tabel_label.place(x = 930,y = 40)

def deals():
	print("btn was clicked")
btn_cnt_option = Button(menu_window, text= "Options", font=('Roboto',10,'bold'), padx = 60, pady = -10,fg= "Green", bg= "white", command= deals)
btn_cnt_option.place(x = 870,y = 60)

menu_window.mainloop()
