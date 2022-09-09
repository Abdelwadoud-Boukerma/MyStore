from distutils.log import info
from itertools import product
import sqlite3
from tkinter import *
from tkinter import ttk
from unittest import result
from math import *


window = Tk()
window.title("MyStore--Green")
window.geometry("1080x720")
window.config(bg="green")
AB_tree = ttk.Treeview(window)
storeName = "MyStore--Green"

cal = StringVar()
multiplier = StringVar()
regulator = StringVar()

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def insert(date, product_category, price, quantity, remainder, total_money):
    conn = sqlite3.connect("ab.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS
                   inventory(itemDate TEXT, itemId TEXT, itemPrice Text, itemQuantity TEXT, itemRemainder TEXT, itemTotalMoney TEXT)""")
    cursor.execute("INSERT INTO inventory VALUES ('"+ str(date) +"','" + str(product_category) + "','" + str(price) + "','" + str(quantity) + "','" + str(remainder) + "','" + str(total_money) + "')")
    conn.commit()

def delete(data):
    conn = sqlite3.connect("ab.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS
                   inventory(itemDate TEXT, itemId TEXT, itemPrice Text, itemQuantity TEXT, itemRemainder TEXT, itemTotalMoney TEXT)""")
    
    cursor.execute("DELETE FROM inventory WHERE itemDate = '"+ str(data) +"'")
    conn.commit()

def update(date, product_category,price, quantity, remainder, total_money, idName):
    conn = sqlite3.connect("ab.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemDate TEXT, itemId TEXT, itemPrice Text, itemQuantity TEXT, itemRemainder TEXT, itemTotalMoney TEXT)""")

    cursor.execute("UPDATE inventory SET itemDate = '"+ str(date) + "', itemId = '" + str(product_category) + "', itemPrice = '" + str(price) + "', itemQuantity = '" + str(quantity) + "', itemRemainder = '" + str(remainder) + "', itemTotalMoney = '" + str(total_money) + "' WHERE itemDate='" +str(idName)+ "'")
    conn.commit()

def read():
    conn = sqlite3.connect("ab.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS
                   inventory(itemDate TEXT, itemId TEXT, itemPrice Text, itemQuantity TEXT, itemRemainder TEXT, itemTotalMoney TEXT)""")
    
    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results

def insert_data():
    itemDate = str(entryDate.get()) 
    itemId = str(entryId.get())
    #itemPurchase = str(entry_purchase.get())
    itemPrice = str(entryPrice.get())
    itemQuant = str(entryQuant.get())
    itemRemainder = str(remainder_entry.get())
    itemTotalMoney = str(Total_money_entry.get())
    if itemDate == "" or itemDate == " ":
        print("error insterting Date.")
    elif itemId == "" or itemId == " ":
        print("error insterting ID.")
    #elif itemPurchase == "" or itemPurchase == " ":
        #print("error insterting Purchase.")
    elif itemPrice == "" or itemPrice == " ":
        print("error insterting price.")
    elif itemQuant == "" or itemQuant == " ":
        print("error insterting quantity.")
    elif itemRemainder == "" or itemRemainder == " ":
        print("error insterting Remainder.")
    elif itemTotalMoney == "" or itemTotalMoney == " ":
        print("error insterting the total.")
    else:
        insert(str(itemDate), str(itemId), str(itemPrice), str(itemQuant), str(itemRemainder), str(itemTotalMoney))
    
    for data in AB_tree.get_children():
        AB_tree.delete(data)
    
    for result in reverse(read()):
        AB_tree.insert(parent= "", index= "end", iid= result, text= "", values= (result), tag= "orow")

    AB_tree.tag_configure("orow", background= "#EEEEEE")
    AB_tree.grid(row= 1, column= 5, columnspan= 4, rowspan= 5, padx= 10, pady= 10)
    
def delete_data():
    selected_item = AB_tree.selection()[0]
    deleteData = str(AB_tree.item(selected_item)["values"][0])
    delete(deleteData)     
    
    for data in AB_tree.get_children():
        AB_tree.delete(data)
    
    for result in reverse(read()):
        AB_tree.insert(parent= "", index="end", iid= result, text="", values=(result), tag= "orow")
    
    AB_tree.tag_configure("orow", background= "#EEEEEE")
    AB_tree.grid(row= 1, column= 5, columnspan= 4, rowspan= 5, padx= 10, pady= 10)

def delete_all():
    delete("data.db")

def update_data():
    selected_item = AB_tree.selection()[0]
    update_name = AB_tree.item(selected_item)['values'][0]
    update(entryDate.get(), entryId.get(), entryPrice.get(), entryQuant.get(),  remainder_entry.get(), Total_money_entry.get(), update_name)
    

    for data in AB_tree.get_children():
        AB_tree.delete(data)

    for result in reverse(read()):
        AB_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    AB_tree.tag_configure('orow', background='#EEEEEE')
    AB_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def update_quant():
    num1 = int(entryQuant.get())
    num2 = int(entrySell.get())
    result = num1 - num2
    cal.set(str(result))
    
def Multiply_quant_money():
    num1 = float(entryPrice.get())
    num2 = float(entrySell.get())
    mult = num1 * num2
    multiplier.set(str(float(mult)))
    
def find_sell():
    num = int(entry_purchase.get())
    regulate = (num * 30 / 100) + num
    regulator.set(str(regulate))

titleLabel = Label(window, 
                   text= storeName,
                   font=("comicsans", 40, 'bold'),
                   bd= 2,
                   fg="orange",
                   bg= "green"
                   )
titleLabel.place(x= 750, y= 10)

date_label = Label(window,
                   text= "Date: ",
                   font= ("comicsans", 12, "bold"),
                   fg= "orange",
                   bg= "green",
                   )
date_label.place(x= 825, y= 100)

entryDate = Entry(window, 
                width= 25,
                bd= 5, 
                font= ("italic", 12, "bold"),
                bg= "orange", 
                fg= "green")
entryDate.place(x= 900, y= 100)

idLabel = Label(window, 
                text= "Product:", 
                font= ("comicsans", 12, "bold"),
                fg="orange",
                bg= "green")
idLabel.place(x= 800, y= 150)

entryId = Entry(window, 
                width= 25,
                bd= 5, 
                font= ("italic", 12, "bold"),
                bg= "orange", 
                fg= "green")
entryId.place(x= 900, y= 150)

purchase_label = Label(window, 
                       text= "Purchase:",
                       font= ("comicsans", 12, "bold"),
                       fg= "orange",
                       bg= "green",)
purchase_label.place(x= 785, y= 200)

entry_purchase = Entry(window,
                        width= 25,
                        bd= 5, 
                        font= ("italic", 12, "bold"),
                        bg= "orange", 
                        fg= "green")

entry_purchase.place(x= 900, y= 200)

QuantityLabel = Label(window, 
                text= "Quantity:", 
                font= ("comicsans", 12, "bold"), 
                fg="orange",
                bg= "green")
QuantityLabel.place(x= 790, y= 250)

entryQuant = Entry(window,
                width= 25,
                bd= 5, 
                font= ("Italic", 12, "bold"),
                bg= "orange", 
                fg= "green")
entryQuant.place(x= 900, y= 250)

PriceLabel = Label(window, 
                text= "Price of selling:", 
                font= ("comicsans", 12, "bold"),
                fg="orange",
                bg= "green")
PriceLabel.place(x= 747, y= 300)


entryPrice = Entry(window, 
                textvariable= regulator, 
                width= 25,
                bd= 5, 
                font= ("italic", 12, "bold"),
                bg= "orange", 
                fg= "green")
entryPrice.place(x= 900, y= 300)


remainder_label = Label(window, 
                text= "Remaining:",
                font= ("comicsans", 12, "bold"), 
                fg="orange",
                bg= "green"
                  )
remainder_label.place(x= 781, y = 350)

remainder_entry = Entry(window, 
                 textvariable= cal,
                 width= 25,
                 bd= 5, 
                 font= ("Italic", 12, "bold"),
                 bg= "orange", 
                fg= "green")
remainder_entry.place(x= 900, y = 350)

Sell_label= Label(window,
                text= "Quantity Sold:" , 
                font= ("comicsans", 12, "bold"), 
                fg="orange",
                bg= "green")
Sell_label.place(x= 30, y= 300)

entrySell = Entry(window, 
                width= 25,
                bd= 5, 
                font= ("Italic", 12, "bold"),
                bg= "orange", 
                fg= "green")
entrySell.place(x= 150, y= 300)


button_Enter = Button(window, 
                      text= "Enter", 
                      font= ("comicsans", 15), 
                      bg= "#87CEEB",
                      activebackground= "#87CEEB",
                      fg= "#000000", 
                      activeforeground= "#000000" ,
                      padx= 5,
                      pady= 5, 
                      width= 5,
                      bd=3 , 
                      command= insert_data
                      )
button_Enter.place(x= 148, y= 550)


button_Update = Button(window, 
                      text= "Update", 
                      font= ("comicsans", 15), 
                      bg= "#FFFF00",
                      activebackground= "#FFFF00",
                      fg= "#000000", 
                      activeforeground= "#000000" ,
                      padx= 5,
                      pady= 5, 
                      width= 5,
                      bd=3,
                      command= update_data
                      )
button_Update.place(x= 248, y= 550)

button_Delete = Button(window, 
                      text= "Delete", 
                      font= ("comicsans", 15), 
                      bg= "#ff0000",
                      activebackground= "#ff0000",
                      fg= "#000000", 
                      activeforeground= "#000000",
                      padx= 5,
                      pady= 5, 
                      width= 5,
                      bd=3,
                      command= delete_data 
                      )
button_Delete.place(x= 348, y= 550)

button_regulator = Button(window,
                    text= "Sell",
                    font= ("comicsans", 10, "bold"), 
                    bg= "orange",
                    activebackground= "orange",
                    fg= "green", 
                    activeforeground= "green",
                    padx= 5,
                    pady= 5, 
                    width= 5,
                    height=1,
                    bd=3,
                    command= find_sell)
button_regulator.place(x= 670, y= 300)

#delete_all_button = Button(window, 
#                           text= "Delete all",
#                           font= ("comicsans", 15), 
 #                          bg= "#ff0000",
  #                         activebackground= "#ff0000",
   #                        fg= "#000000", 
    #                       activeforeground= "#000000",
     #                      padx= 5,
      #                     pady= 5, 
       #                    width= 5,
        #                   bd=3,
         #                  command= delete_all 
          #                 )
#delete_all_button.place(x= 948, y= 700)

button_Update_Stock = Button(window, 
                      text= "Stock", 
                      font= ("comicsans", 10), 
                      bg= "#ff0000",
                      activebackground= "#ff0000",
                      fg= "#000000", 
                      activeforeground= "#000000",
                      padx= 5,
                      pady= 5, 
                      width= 5,
                      height= 1,
                      bd=3,
                      command= lambda: update_quant() 
                      )
button_Update_Stock.place(x= 400, y = 299)

button_sell_total = Button(window, 
                      text= "Total money",
                      font= ("comicsans", 10, "bold"), 
                      bg= "blue",
                      activebackground= "blue",
                      fg= "white", 
                      activeforeground= "white",
                      padx= 5,
                      pady= 5, 
                      width= 15,
                      bd=3,
                      command= lambda: Multiply_quant_money()
                           )
button_sell_total.place(x= 150, y= 400)


Total_money = Label(window, 
                text="Total Money of the selected product:",
                font= ("comicsans", 12, "bold"), 
                fg="orange",
                bg= "green"
                    )
Total_money.place(x= 30, y= 350)

Total_money_entry = Entry(window, 
                 textvariable= multiplier,
                 width= 25,
                 bd= 5, 
                 font= ("Italic", 12, "bold"),
                 bg= "orange", 
                fg= "green")
Total_money_entry.place(x= 320, y = 350)

Info = Label(window, 
             text = "This program is only for quantity measures, which means, it is not meant for calculating weight", 
             font= ("comicsans", 10),
             bg = "green",
             fg= "orange")
Info.place(x= 10, y= 770)

creator = Label(window, 
             text = "Created by: Abdelwadoud Boukerma", 
             font= ("comicsans", 10),
             bg = "green",
             fg= "orange")
creator.place(x= 900, y= 750)

Version = Label(window, 
             text = "Version: 0.5.1", 
             font= ("comicsans", 10),
             bg = "green",
             fg= "orange")
Version.place(x= 900, y= 770)

style = ttk.Style()
style.configure("TreeView Heading", font=("Arial", 15, "bold"))

AB_tree["columns"] = ("Date", "Product", "Price", "Quantity", "Remaining", "Total Price")
AB_tree.column("#0", width= 0, stretch= NO)
AB_tree.column("Date", anchor= W,width= 120)
AB_tree.column("Product", anchor= W,width= 100)
AB_tree.column("Price", anchor= W,width= 100)
AB_tree.column("Quantity", anchor= W,width= 100)
AB_tree.column("Remaining", anchor= W,width= 100)
AB_tree.column("Total Price", anchor= W, width= 100)
AB_tree.heading("Date", text="Date",anchor= W)
AB_tree.heading("Product", text="Product",anchor= W)
AB_tree.heading("Price", text="Price",anchor= W)
AB_tree.heading("Quantity", text="Quantity",anchor= W)
AB_tree.heading("Remaining", text="Remaining",anchor= W)
AB_tree.heading("Total Price", text="Total Price",anchor= W)

for data in AB_tree.get_children():
    AB_tree.delete(data)

AB_tree.tag_configure('orow', background= "#EEEEEE", font=("Arial", 15, "bold"))
AB_tree.place(x= 10, y= 10)

#for result in reverse(read()):
        #AB_tree.insert(parent= "", index= "end", iid=0, text= "", values= (result), tag= "orow")


window.mainloop()