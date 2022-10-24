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
#from PIL import ImageTK,Image
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sys
import os
import socket
import requests
########################WINDOW CONFIG###########################
menu_window = Tk()
menu_window.geometry("1900x1024")
menu_window.title("Biogreenleaf-menu")
menu_window_logo = PhotoImage(file='logo_soft.png')
menu_window.iconphoto(True,menu_window_logo)
menu_window.config(background= "black")
### INITIATE FRAME HEADER
btn_frame = Frame(menu_window,bd= 4 ,bg = 'white')
btn_frame.pack()
### INITIATE FRAME PRODUCT
btn_frame_product = Frame(menu_window,bd= 4 ,bg = 'white')
btn_frame_product.place(x = 100 , y = 80)

######################LABEL FIRST##############################
#menu_first_msg =  Label(btn_frame, text = "Welcome to Menu page...",
					#font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
#menu_first_msg.grid(row = 0 , column = 0)
######################TOP BUTTONS###############################
###FIRST BUTTON COMBOBOX- Add btn
head_one_tabel_label =  Label(btn_frame, text = "Add Item",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
head_one_tabel_label.grid(row= 1 , column= 0)
def when_is_clicked(event):
	# open a new window
	btn_add_combo_value = btn_add_combo.get()
	if(btn_add_combo_value == 'Products'):#products loop
		print("you selected products")#test prod
		#####Product Name
		prod_label= Label(btn_frame_product,text= "Add Products: ",font=('Roboto',15,'bold'),fg= 'green',bg='white')
		prod_label.grid(row = 0, column = 0)
		prod_label_name = Label(btn_frame_product,text= "Commodity: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_name.grid(row= 1,column= 0)
		prod_entry_name = Entry(btn_frame_product,text="Commodity",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_name.grid(row= 1,column= 1)
		#####Quantity
		prod_label_quantity = Label(btn_frame_product,text= "Quantity: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_quantity.grid(row= 2,column= 0)
		prod_entry_quantity = Entry(btn_frame_product,text="quantity",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_quantity.grid(row= 2,column= 1)
		#####Quality
		prod_label_quality = Label(btn_frame_product,text= "Quality: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_quality.grid(row= 3,column= 0)
		prod_entry_quality = Entry(btn_frame_product,text="quality",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_quality.grid(row= 3,column= 1)
		#####Origin
		prod_label_origin = Label(btn_frame_product,text= "Origin: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_origin.grid(row= 4,column= 0)
		prod_entry_origin = Entry(btn_frame_product,text="Origin",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_origin.grid(row= 4,column= 1)
		#####Packing
		prod_label_packing = Label(btn_frame_product,text= "Packing: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_packing.grid(row= 5,column= 0)
		prod_entry_packing = Entry(btn_frame_product,text="Packing",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_packing.grid(row= 5,column= 1)
		#####Shipping
		shipping_list = ["None","by Sea","by Truck","by Railway","by Plane"]
		prod_label_shipping = Label(btn_frame_product,text= "Shipping: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_shipping.grid(row= 1,column= 2)
		def shipping_select(event):
			btn_shipping_list_value = btn_shipping_list.get()
			print("click")
		action_shipping_list = StringVar()
		action_shipping_list.set(shipping_list[0])
		btn_shipping_list = ttk.Combobox(btn_frame_product,value= shipping_list)
		btn_shipping_list.bind("<<ComboboxSelected>>",shipping_select)
		btn_shipping_list['state'] = "readonly"
		btn_shipping_list.grid(row = 1, column= 3)
		#####Price(INCOTERM)
		price_list = ["None","EXW","FCA","FAS","FOB","CFR","CIF","CPT","CIP","DAT","DAP","DDP"]
		prod_label_price = Label(btn_frame_product,text= "Incoterms: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_price.grid(row= 2,column= 2)
		def price_select(event):
			btn_price_list_value = btn_price_list.get()
			print("click")
		action_price_list = StringVar()
		action_price_list.set(price_list[0])
		btn_price_list = ttk.Combobox(btn_frame_product,value= price_list)
		btn_price_list.bind("<<ComboboxSelected>>",price_select)
		btn_price_list['state'] = "readonly"
		btn_price_list.grid(row = 2, column= 3)
		
	print("click")
btn_list = ["None","Products","Companies"]
action = StringVar()
action.set(btn_list[0])
btn_add_combo = ttk.Combobox(btn_frame,value= btn_list )
btn_add_combo.bind("<<ComboboxSelected>>",when_is_clicked)
btn_add_combo['state'] = 'readonly'
btn_add_combo.grid(row= 2, column = 0)
###SECOND BUTTON COMBOBOX - Orders
head_two_tabel_label =  Label(btn_frame, text = "Orders",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
head_two_tabel_label.grid(row = 1,column = 1)
def when_is_clicked(event):
	# open a new window
	print("click")
btn_list_two = ["None","For Sellers","For Buyers"]
action = StringVar()
action.set(btn_list_two[0])
btn_ord_combo = ttk.Combobox(btn_frame,value= btn_list_two )
btn_ord_combo.bind("<<ComboboxSelected>>",when_is_clicked)
btn_ord_combo['state'] = 'readonly'
btn_ord_combo.grid(row = 2, column = 1)
###THIRD BUTTON - Connect/Deals
head_three_tabel_label =  Label(btn_frame, text = "Connect Deals",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
head_three_tabel_label.grid(row = 1,column = 2)

def deals():
	print("btn was clicked")
btn_cnt_deal = Button(btn_frame, text= "Connect", font=('Roboto',10,'bold'), padx = 60, pady = -10,fg= "Green", bg= "white", command= deals)
btn_cnt_deal.grid(row = 2, column = 2)
###FORTH BUTTON - status
head_forth_tabel_label =  Label(btn_frame, text = "Deal Status",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
head_forth_tabel_label.grid(row = 1, column = 3)

def deals():
	print("btn was clicked")
btn_cnt_status = Button(btn_frame, text= "Status", font=('Roboto',10,'bold'), padx = 60, pady = -10,fg= "Green", bg= "white", command= deals)
btn_cnt_status.grid(row = 2, column = 3)
###FIFTH BUTTON - options
head_fifth_tabel_label =  Label(btn_frame, text = "Settings",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
head_fifth_tabel_label.grid(row = 1, column = 4)

def deals():
	print("btn was clicked")
btn_cnt_option = Button(btn_frame, text= "Options", font=('Roboto',10,'bold'), padx = 60, pady = -10,fg= "Green", bg= "white", command= deals)
btn_cnt_option.grid(row = 2, column = 4)
###Company bkg - photo
#photo_label_1 = PhotoImage(file="test_img_one.png")
#img_label = Label(menu_window,image= photo_label_1)
#img_label.place(x = 5,y=200)
menu_window.mainloop()
