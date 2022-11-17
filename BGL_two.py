##########################################################
## !bin/etc                                             ##
## This contain the main menu......more to writte       ##
## This soft is created by https://github.com/sade5000  ##
##########################################################
print('=========================================================')
print(' ****   **   **     ****   ****   **    **    **' )
print(' *     *  *  *  *   *      *     *  *  *  *  *  *')
print(' ****  ****  *  *   ****   ****  *  *  *  *  *  *')
print('    *  *  *  *  *   *         *  *  *  *  *  *  *')
print(' ****  *  *  * *    ****   ****   **    **    ** ')
print('=========================================================')
#########################LIBRARY#########################
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
from fpdf import FPDF
########################WINDOW CONFIG####################
menu_window = Tk()
menu_window.geometry("1280x720")
menu_window.title("Biogreenleaf-menu")
menu_window_logo = PhotoImage(file='logo_soft.png')
menu_window.iconphoto(True,menu_window_logo)
menu_window.config(background= "black")
### INITIATE FRAME HEADER
btn_frame = Frame(menu_window,bd= 4 ,bg = 'white')
#btn_frame.pack()
btn_frame.grid(row= 0, column= 0,sticky = W)
##################################DISPLACER
displacer1 = Label(menu_window,bg= 'black').grid(row= 1, column= 0,sticky = W)
### INITIATE FRAME PRODUCT
btn_frame_product = Frame(menu_window,bd= 4 ,bg = 'white')
#btn_frame_product.place(x = 100 , y = 80)
btn_frame_product.grid(row= 2, column =0,sticky = W)
### INITIATE FRAME PRODUCT PROPERTIES
frame_prod_prop = Frame(btn_frame_product,bd= 4 ,bg = 'white')
frame_prod_prop.grid(row= 10, column= 1, columnspan= 3,sticky = W)
### INITIATE FRAME COMPANIES
frame_company = Frame(menu_window,bd= 4 ,bg = 'white')
frame_company.grid(row= 2, column =0,sticky = W)
######################LABEL FIRST##############################
#menu_first_msg =  Label(btn_frame, text = "Welcome to Menu page...",
					#font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
#menu_first_msg.grid(row = 0 , column = 0)
######################TOP BUTTONS###############################
### Dictionary





######## FPDF ######
def soft_corporate_offer(comodity,quantity,origin,packing,loading_ports,price,unit,incoterms):
	pdf_title = 'Soft Corporate Offer'
	pdf_website = 'Website: '
	pdf_footer = 'BIO GREEN LEAF Co.Reg.No.: RO45339474 Str. Malu Rosu , No. 96, Bl. 35C, ap. 4 Ploiesti Romania '
	pdf_intro = 'With full legal and corporate responsibility and under penalty of perjury we BIO \b GREEN LEAF hereby declare to be willing and able to sell'# Refined Sunflower Oil at the\b below conditions:'
	pdf_comodity_test = comodity
	pdf_comodity_test_1= 'at the below conditions:'
	class PDF(FPDF):
		def header(self):
			self.image('Logo_BGL.jpeg',25,5,50)
			#self.image('Address_icon.png',125,5,3)
			self.image('web_buttons.png', 130,15,8)
			self.image('White-header-good.jpg', 0,50,210)
			self.set_font('Arial','U',15)
			#w = self.get_string_width(pdf_title) + 1
			#self.set_x((210 - w)/2)
			self.set_draw_color(255,255,255)
			self.set_fill_color(255,255,255)
			self.set_text_color(0,0,0)
			self.set_line_width(1)
			#self.cell(w,100,pdf_title,0,0,'C',1)
			self.ln(1)
			#### website label ####
			self.set_font('Arial','B',9)
			self.set_text_color(0,0,51)
			self.set_x(137)
			self.cell(1, 15,'Website:', 0, 0, 'L', False, '')
			#### website addres ###
			self.set_font('Arial','U',9)
			self.set_text_color(0,153,0)
			self.set_x(151)
			self.cell(1, 15,'biogreenleaf.eu', 0, 0, 'L', False, 'www.biogreenleaf.eu')
			#### email label #####
			self.set_font('Arial','B',9)
			self.set_text_color(0,0,51)
			self.set_x(137)
			self.cell(1, 29,'E-mail:', 0, 0, 'L', False, '')
			#### email ###########
			self.set_font('Arial','U',9)
			self.set_text_color(0,153,0)
			self.set_x(149)
			self.cell(1, 29,'office@biogreenleaf.eu', 0, 0, 'L', False, 'office@biogreenleaf.eu')
			#### Address #########
			self.set_font('Arial','B',8)
			self.set_text_color(0,0,51)
			self.set_x(137)
			self.cell(1, 43,'Str. Malu Rosu, No. 96, Ploiesti, Romania', 0, 0, 'B', False, '')
			#### Mobile ##########
			self.set_font('Arial','B',9)
			self.set_text_color(0,0,51)
			self.set_x(137)
			self.cell(1, 56,'+44 7436272744 / +40 725654555', 0, 0, 'B', False, '')
			######################
			#self.image('margin_pdf.jpeg', 0,50,210)
			#### END OF HEADER####
		def footer(self):
			### position and color
			self.set_y(-15)
			self.set_fill_color(0,0,51)
			self.rect(0,297 - 6,210,10,'F')
			self.rect(0,70,6,297-70-6,'F')
			self.set_fill_color(0,0,51)
			self.rect(210-6,70,6,297-70-6,'F')
			self.set_font('Arial', 'B', 7)
			w = self.get_string_width(pdf_footer) + 1
			self.set_x((210 - w)/2)
			self.set_text_color(255,255,255)	
			self.cell(1, 25,'BIO GREEN LEAF Co.Reg.No.: RO45339474 Str. Malu Rosu , No. 96, Bl. 35C, ap. 4 Ploiesti Romania ', 0, 0, 'B', False, '')
			#### END OF FOOTER ####
		def chapter_body(self):
		
			self.set_font('Helvetica','B',25)
			self.set_fill_color(255,255,255)
			w = self.get_string_width(pdf_title) + 1
			self.set_y(80)
			self.set_x((210 - w)/2)
			self.set_text_color(0,0,51)	
			self.cell(1, 25,pdf_title, 0, 0, 'U', False, '')
			self.ln(4)
			self.set_font('Arial','B',10)
			self.set_fill_color(255,255,255)
			self.set_y(110)
			self.set_x(15)
			self.set_text_color(0,0,51)	
			self.multi_cell(0, 5,pdf_intro, 0,  'J', False, '')
			self.ln(1)	
			#
			self.set_font('Arial','B',10)
			self.set_fill_color(255,255,255)
			self.set_y(115)
			self.set_x(76)
			self.set_text_color(0,102,0)	
			self.multi_cell(0, 5,pdf_comodity_test, 0,  'J', False, '')
			self.ln(1)
			#
			self.set_font('Arial','B',10)
			self.set_fill_color(255,255,255)
			self.set_y(115)
			w = self.get_string_width(pdf_comodity_test) + 1
			self.set_x(76+w)
			self.set_text_color(0,0,51)	
			self.multi_cell(0, 5,pdf_comodity_test_1, 0,  'J', False, '')
			self.ln(1)
			# Comodity:
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(130)
			self.set_x(40)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,'COMMODITY', 0, 0, 'L', False, '')
			self.ln(1)
		
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(130)
			self.set_x(100)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,":"+comodity, 0, 0, 'L', False, '')
			self.ln(1)
			#Quantity:
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(140)
			self.set_x(40)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,'QUANTITY', 0, 0, 'L', False, '')
			self.ln(1)
		
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(140)
			self.set_x(100)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,":"+ quantity + unit + "/Month", 0, 0, 'L', False, '')
			self.ln(1)
			#Origin
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(150)
			self.set_x(40)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,'ORIGIN', 0, 0, 'L', False, '')
			self.ln(1)
		
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(150)
			self.set_x(100)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,":"+ origin, 0, 0, 'L', False, '')
			self.ln(1)
			#Packing
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(160)
			self.set_x(40)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,'PACKING', 0, 0, 'L', False, '')
			self.ln(1)
		
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(160)
			self.set_x(100)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,":"+ packing, 0, 0, 'L', False, '')
			self.ln(1)
			#Loading Ports
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(170)
			self.set_x(40)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,'LOADING PORTS', 0, 0, 'L', False, '')
			self.ln(1)
		
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(170)
			self.set_x(100)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,":" + loading_ports, 0, 0, 'L', False, '')
			self.ln(1)
			#Price
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(180)
			self.set_x(40)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,incoterms + ' PRICE', 0, 0, 'L', False, '')
			self.ln(1)
		
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(180)
			self.set_x(100)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,":"+ price+ " $"+ "/"+ unit, 0, 0, 'L', False, '')
			self.ln(1)
			#Specifications
			self.set_font('Arial','B',15)
			self.set_fill_color(255,255,255)
			self.set_y(190)
			self.set_x(40)
			self.set_text_color(0,0,51)	
			self.cell(0, 5,'SPECIFICATIONS:', 0, 0, 'L', False, '')
			self.ln(1)
			#Spec. Title
			
			
			#### END OF BODY ######
				
	pdf = PDF(orientation = 'P', unit = 'mm', format='A4')
	pdf.set_title(pdf_title)
	pdf.add_page()
	pdf.chapter_body()
	pdf.set_author('Biogreenleaf')
	pdf.output('pdf_test.pdf','F')

###FIRST BUTTON COMBOBOX- Add btn
head_one_tabel_label =  Label(btn_frame, text = "Add Item",
					font = ('Roboto',10,'bold'),fg = 'green',bg= 'white')
head_one_tabel_label.grid(row= 1 , column= 0)
def when_is_clicked(event):
	# open a new window
	btn_add_combo_value = btn_add_combo.get()
	if(btn_add_combo_value == 'Products'):#products loop
		frame_company.grid_forget()
		print("you selected products")#test prod
		#####Product Name
		prod_label= Label(btn_frame_product,text= 'Products',font=('Roboto',15,'bold'),fg= 'green',bg='white')
		prod_label.grid(row = 0, column = 0,sticky = W)
		prod_label_name = Label(btn_frame_product,text= "Commodity: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_name.grid(row= 1,column= 0,sticky = W)
		prod_entry_name = Entry(btn_frame_product,text="Commodity",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_name.grid(row= 1,column= 1)
		#####Quantity
		prod_label_quantity = Label(btn_frame_product,text= "Quantity: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_quantity.grid(row= 2,column= 0,sticky = W)
		prod_entry_quantity = Entry(btn_frame_product,text="quantity",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_quantity.grid(row= 2,column= 1)
		#####Quality
		prod_label_quality = Label(btn_frame_product,text= "Quality: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_quality.grid(row= 3,column= 0,sticky = W)
		prod_entry_quality = Entry(btn_frame_product,text="quality",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_quality.grid(row= 3,column= 1)
		#####Origin
		prod_label_origin = Label(btn_frame_product,text= "Origin: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_origin.grid(row= 4,column= 0,sticky = W)
		prod_entry_origin = Entry(btn_frame_product,text="Origin",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_origin.grid(row= 4,column= 1)
		#####Packing
		prod_label_packing = Label(btn_frame_product,text= "Packing: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_packing.grid(row= 5,column= 0,sticky = W)
		prod_entry_packing = Entry(btn_frame_product,text="Packing",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_packing.grid(row= 5,column= 1)
		#####Unit Mesure
		unit_list = ["None","g","Kg","Tons","MT","litter","mm","cm","m","unit"]
		prod_label_MU = Label(btn_frame_product,text= "Mesure Unit: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_MU.grid(row= 2,column= 2,sticky = W)
		def shipping_select(event):
			global btn_shipping_list_value
			btn_shipping_list_value = btn_shipping_list.get()
			print("click")
		action_shipping_list = StringVar()
		action_shipping_list.set(unit_list[0])
		btn_shipping_list = ttk.Combobox(btn_frame_product,value= unit_list)
		btn_shipping_list.bind("<<ComboboxSelected>>",shipping_select)
		btn_shipping_list['state'] = "readonly"
		btn_shipping_list.current(0)
		btn_shipping_list.grid(row = 2, column= 3)
		#####Price(INCOTERM)
		price_list = ["None","EXW","FCA","FAS","FOB","CFR","CIF","CPT","CIP","DAT","DAP","DDP"]
		prod_label_price = Label(btn_frame_product,text= "Incoterms: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_price.grid(row= 1,column= 2,sticky = W)
		def price_select(event):
			global btn_price_list_value
			btn_price_list_value = btn_price_list.get()
			print("click")
		action_price_list = StringVar()
		action_price_list.set(price_list[0])
		btn_price_list = ttk.Combobox(btn_frame_product,value= price_list)
		btn_price_list.bind("<<ComboboxSelected>>",price_select)
		btn_price_list['state'] = "readonly"
		btn_price_list.current(0)
		btn_price_list.grid(row = 1, column= 3)
		#####Real Price
		prod_label_real_price = Label(btn_frame_product,text= "Price: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_real_price.grid(row= 3,column= 2,sticky = W)
		prod_entry_real_price = Entry(btn_frame_product,text="price",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_real_price.grid(row= 3,column= 3)
		#####Exact Location
		prod_label_location = Label(btn_frame_product,text= "Exact Location: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_location.grid(row= 4,column= 2,sticky = W)
		prod_entry_location = Entry(btn_frame_product,text="destination",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_location.grid(row= 4,column= 3)
		#####Contract length
		prod_label_contract_length = Label(btn_frame_product,text= "Contract Length: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_label_contract_length.grid(row= 5,column= 2,sticky = W)
		prod_entry_contract_length = Entry(btn_frame_product,text="Contract length",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		prod_entry_contract_length.grid(row= 5,column= 3)
		label_space_btn = Label(btn_frame_product,text="",bg= 'white').grid(row = 6, column = 0)
		####Add Button
		def add_product():
			print("You added a product")
			####Button function
			### Get TO Var
			global comodity
			comodity = prod_entry_name.get()
			global quantity
			quantity = prod_entry_quantity.get()
			global quality
			quality  = prod_entry_quality.get()
			global origin
			origin   = prod_entry_origin.get()
			global packing
			packing  = prod_entry_packing.get()
			global mesure
			mesure   = btn_shipping_list_value
			global payment
			payment  = btn_price_list_value
			global price
			price    = prod_entry_real_price.get()
			global location
			location = prod_entry_location.get()
			global contract
			contract = prod_entry_contract_length.get()
			print("comodity: "+comodity+" \n"
				+"quantity: "+ quantity + " \n"
				+"quality: "+ quality + " \n"
				+"origin: "+ origin + " \n"
				+"packing: "+ packing + " \n"
				+"mesure: "+ mesure + " \n"
				+"payment: "+ payment + " \n"
				+"price: "+ price + " \n"
				+"location: "+ location + " \n"
				+"contract: "+ contract)### For testing - shut down after that
			### Write a PDF file
				
			### Write to file ####
			with open('product_file.pdf','w') as f:
			
				f.write("This is a Bio Green Leaf file \n"
				+"comodity: "+comodity+" \n"
				+"quantity: "+ quantity + " \n"
				+"quality: "+ quality + " \n"
				+"origin: "+ origin + " \n"
				+"packing: "+ packing + " \n"
				+"mesure: "+ mesure + " \n"
				+"payment: "+ payment + " \n"
				+"price: "+ price + " \n"
				+"location: "+ location + " \n"
				+"contract: "+ contract + " \n"
				+ "www.biogreenleaf.eu")
				f.close()
			
			soft_corporate_offer(comodity,quantity,origin,packing,location,price,mesure,payment)
			
			#####This will delete all entry after adding data to the file 
			prod_entry_name.delete(0,END)
			prod_entry_quantity.delete(0,END)
			prod_entry_quality.delete(0,END)
			prod_entry_origin.delete(0,END)
			prod_entry_packing.delete(0,END)
			btn_shipping_list.current(0)
			btn_price_list.current(0)
			prod_entry_real_price.delete(0,END)
			prod_entry_location.delete(0,END)
			prod_entry_contract_length.delete(0,END)
			
		btn_add_product = Button(btn_frame_product,text= "Add Product",font=('Roboto',10,'bold'),fg= 'green',bg='white',command= add_product)
		btn_add_product.grid(row = 7,column= 3, sticky = E)###need to be changed in time 
		####Browse Picture Button
		def add_photos():
			print("You added a picture")
		btn_add_picture = Button(btn_frame_product,text= "Add Photos",font=('Roboto',10,'bold'),fg= 'green',bg='white',command= add_photos)
		btn_add_picture.grid(row= 7, column= 0,sticky = W)###need to be changed in time 
		####Add Company
		def add_company():
			print("Add a Company")
		btn_add_company = Button(btn_frame_product,text= "Add Company",font=('Roboto',10,'bold'),fg= 'green',bg='white',command= add_company)
		btn_add_company.grid(row= 7, column= 1)###need to be changed in time 
		####Select Company
		def select_company():
			print("Select a Company")
		btn_select_company = Button(btn_frame_product,text= "Sel. Company",font=('Roboto',10,'bold'),fg= 'green',bg='white',command= select_company)
		btn_select_company.grid(row= 7, column= 2)###need to be changed in time
		label_space_prp = Label(btn_frame_product,text=" ",bg= 'white').grid(row = 8, column = 0)
		######### LOOOP FUNCTION AGAIN
		label_no_of_prop = Label(btn_frame_product,text= "No. of Properties: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_no_of_prop.grid(row= 9, column= 0)
		entry_no_of_prop = Entry(btn_frame_product,text="no of prop",font=('Roboto',10,'bold'),fg= 'green',bg='white',width=3)
		entry_no_of_prop.grid(row= 9, column= 1,sticky = W)
		
		def properties_states(frame,no_of_props):
			global prop_list
			prop_list = []
			global prop_list_index
			prop_list_index = []
			if(int(no_of_props) == 0):
				label_shown = Label(frame,text= "No Other Properties",font=('Roboto',10,'bold'),fg= 'green',bg='white')
				label_shown.grid(row=0,column= 0)
			elif(int(no_of_props) > 0):
			
				for x in range(int(no_of_props)):
					entry_prop_dim = Entry(frame,font=('Roboto',10,'bold'),fg= 'green',bg='white')
					entry_prop_dim.grid(row = x , column = 0)
					prop_list.append(entry_prop_dim)
					entry_prop_index = Entry(frame,font=('Roboto',10,'bold'),fg= 'green',bg='white')
					entry_prop_index.grid(row= x  , column = 1)
					prop_list_index.append(entry_prop_index)
				def submit_btn_prop():
					for prop in prop_list:
						entry_lst = ''
						entry_lst = entry_lst + str(prop.get()) + '\n'
						print(entry_lst)
					for index in prop_list_index:
						entry_idx = ''
						entry_idx = entry_idx + str(index.get()) + '\n'
						print(entry_idx)
									
				btn_submit_prop = Button(frame,text= "Submit",font=('Roboto',10,'bold'),fg= 'green',bg='white',command= submit_btn_prop)
				btn_submit_prop.grid(row = (int(no_of_props)+1),column= 0)
							
		def no_of_prop():
			global no_of_prop
			no_of_prop = entry_no_of_prop.get()
			properties_states(frame_prod_prop,no_of_prop)
			print(no_of_prop)
			
		btn_no_of_prop = Button(btn_frame_product,text= "Properties +:",font=('Roboto',10,'bold'),fg= 'green',bg='white',command= no_of_prop)
		btn_no_of_prop.grid(row= 9,column= 2,sticky = W)
		
		###################
	if(btn_add_combo_value == 'Companies'):#Update companies
		btn_frame_product.grid_forget()
		#print("You chose companies")
		label_company = Label(frame_company, text= "Companies",font=('Roboto',15,'bold'),fg= 'green',bg='white')
		label_company.grid(row= 0, column= 0,sticky = W)
		### Company Name
		label_company_name = Label(frame_company, text= "Company name: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_name.grid(row= 1, column= 0,sticky = W)
		entry_company_name = Entry(frame_company, text= "Company name",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_name.grid(row= 1, column= 1,sticky = W)
		### Company Reg. No
		label_company_regno = Label(frame_company, text= "Registration No.: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_regno.grid(row= 2, column= 0,sticky = W)
		entry_company_regno = Entry(frame_company, text= "Reg. No.",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_regno.grid(row= 2, column= 1,sticky = W)
		### Comp. VAT
		label_company_VAT = Label(frame_company, text= "V.A.T. No.: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_VAT.grid(row= 3, column= 0,sticky = W)
		entry_company_VAT = Entry(frame_company, text= "VAT No.",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_VAT.grid(row= 3, column= 1,sticky = W)
		### Comp. Origin
		label_company_origin = Label(frame_company, text= "Company Based: ",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_origin.grid(row= 4, column= 0,sticky = W)
		entry_company_origin = Entry(frame_company, text= "Company Origin",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_origin.grid(row= 4, column= 1,sticky = W)
		### Comp. Address
		label_company_address = Label(frame_company, text= "Company Address:",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_address.grid(row= 5, column= 0,sticky = W)
		entry_company_address = Entry(frame_company, text= "Company Address",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_address.grid(row= 5, column= 1,sticky = W)
		### Comp. Email
		label_company_mail = Label(frame_company, text= "Company Mail:",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_mail.grid(row= 1, column= 2,sticky = W)
		entry_company_mail = Entry(frame_company, text= "Company Mail",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_mail.grid(row= 1, column= 3,sticky = W)
		### Comp. Phone
		label_company_phone = Label(frame_company, text= "Company Phone:",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_phone.grid(row= 2, column= 2,sticky = W)
		entry_company_phone = Entry(frame_company, text= "Company Phone",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_phone.grid(row= 2, column= 3,sticky = W)
		### Comp. Profile
		label_company_profile = Label(frame_company, text= "Company Profile:",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_profile.grid(row= 3, column= 2,sticky = W)
		entry_company_profile = Entry(frame_company, text= "Company Profile",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_profile.grid(row= 3, column= 3,sticky = W)
		### Comp. Reprezentant
		label_company_reprezentant= Label(frame_company, text= "Company Delegate:",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_reprezentant.grid(row= 4, column= 2,sticky = W)
		entry_company_reprezentant = Entry(frame_company, text= "Company Delegate",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_reprezentant.grid(row= 4, column= 3,sticky = W)
		### Comp. Financial
		label_company_financial= Label(frame_company, text= "Financial Staus:",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_financial.grid(row= 5, column= 2,sticky = W)
		entry_company_financial = Entry(frame_company, text= "Financial Staus",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_financial.grid(row= 5, column= 3,sticky = W)
		### Company CEO
		label_company_CEO= Label(frame_company, text= "Company CEO:",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		label_company_CEO.grid(row= 6, column= 0,sticky = W)
		entry_company_CEO = Entry(frame_company, text= "Company CEO",font=('Roboto',10,'bold'),fg= 'green',bg='white')
		entry_company_CEO.grid(row= 6, column= 1,sticky = W)
		###

	if(btn_add_combo_value == 'Products'):#update products
		print("product selected")
		btn_frame_product.grid(row= 2, column =0,sticky = W)
		prod_entry_name.delete(0,END)
		prod_entry_quantity.delete(0,END)
		prod_entry_quality.delete(0,END)
		prod_entry_origin.delete(0,END)
		prod_entry_packing.delete(0,END)
		btn_shipping_list.current(0)
		btn_price_list.current(0)
		prod_entry_real_price.delete(0,END)
		prod_entry_location.delete(0,END)
		prod_entry_contract_length.delete(0,END)	
	#if(btn_add_combo_value == 'Companies'):#Update companies
		#print("You chose companies")
		
	elif(btn_add_combo_value == 'None'):#products loop
		print("You chose none")
		
btn_list = ["None","Products","Companies"]
action = StringVar()
action.set(btn_list[1])
btn_add_combo = ttk.Combobox(btn_frame,text= btn_list[0],value= btn_list )
btn_add_combo.bind("<<ComboboxSelected>>",when_is_clicked)
btn_add_combo['state'] = 'readonly'
btn_add_combo.current(0)
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
btn_ord_combo.current(0)
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

menu_window.mainloop()
