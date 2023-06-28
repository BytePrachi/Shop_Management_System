import itertools
import random
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class shop:
    id_iter = itertools.count()
    def __init__(self, root):
        self.row = []
        self.root = root
        self.root.title("Shop Management System")
        self.root.geometry("1350x700+0+0")
        self.id = next(shop.id_iter)


        title = Label(self.root, text="Shop Management System", bd= 10, relief=GROOVE, font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        # -------- All Variables -----------------
        self.id_var= StringVar()
        self.name_var = StringVar()
        self.contact_var = StringVar()
        self.address_var = StringVar()
        self.item_var = StringVar()
        self.quantity_var = StringVar()
        self.price_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ----------- Manage Frame ----------------

        Manage_Frame = Frame(self.root, bd=1, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=680)

        m_title = Label(Manage_Frame, text="Garments Shop", bg="crimson", fg="white", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)


        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd= 1, relief=GROOVE)
        txt_name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=1, relief=GROOVE)
        txt_contact.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(Manage_Frame, width=29, height=4, font=("", 10))
        self.txt_address.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_item = Label(Manage_Frame, text="Item Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_item.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_item = Entry(Manage_Frame, textvariable=self.item_var, width= 20, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
        txt_item.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        combo_item = ttk.Combobox(Manage_Frame, textvariable=self.item_var, font=("times new roman", 13, "bold"), state='readonly')
        combo_item['values'] = (
        "Shirt S", "Shirt M", "Shirt L", "Shirt XL", "Shirt XXL", "Jeans size-30", "Jeans size-32", "Jeans size-34",
        "Jeans size-36", "Jeans size-38", "Jeans size-40", "Jeans size-42", "Jeans size-46", "Jeans size-52",
        "Pant size-28", "Pant size-30", "Pant size-32", "Pant size-34", "Pant size-36", "Pant size-38", "Pant size-40",
        "Pant size-42", "Trouser S", "Trouser M", "Trouser L", "Trouser XL", "Trouser XXL", "Black Tie", "Maroon Tie",
        "Blue Tie", "Green Tie", "Red cap", "Black cap", "Blue cap", "White cap", "Pink cap", "Brown cap", "Belt S",
        "Belt M", "Belt L", "Kama Sutra Pocket Perfume", "Park Avenue Neo Perfume", "Brut Deodorant",
        "Nivea Deep Deodorant", "Calvin Klein Perfume", "Ralph Lauren", "Tommy Hilfiger Wallet", "Montblanc Wallet",
        "Urban Forest Wallet", "Shinola Wallet", "Tom Ford Wallet", "Goyard wallet", "Nike Hoodie", "Champion Hoodie",
        "ADIDAS Hoodie", "American Giant", "H&M Hoodie", "Calvin Klein Hoodie", "Blue Coat", "Maroon Coat",
        "Black Coat", "Grey Coat", "Full Sleeve Sweater S", "Full Sleeve Sweater L", "Half Sleeve Sweater S",
        "Half Sleeve Sweater L")
        combo_item.grid(row=4, column=1, padx=20, pady=10)

        lbl_quantity = Label(Manage_Frame, text="Quantity", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_quantity.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_quantity = Entry(Manage_Frame, textvariable=self.quantity_var, font=("times new roman", 15, "bold"), bd=1, relief=GROOVE)
        txt_quantity.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_price = Label(Manage_Frame, text="Price", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_price.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_price = Entry(Manage_Frame, textvariable=self.price_var, font=("times new roman", 15, "bold"), bd=1, relief=GROOVE)
        self.txt_price.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # --------- Button Frame ------------------

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=12, y= 565, width=420)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_items).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10, command= self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10, command= self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        # ----------- Detail Frame ----------------

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=1000, height=680)

        lbl_search = Label(Detail_Frame, text="     Search By", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable = self.search_by, width=12, font=("times new roman", 17, "bold"), state='readonly')
        combo_search['values'] = ("Id", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search = Entry(Detail_Frame, textvariable = self.search_txt, width=15, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=20, pady= 5, command= self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=20, pady=5, command= self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        # ------------ Table Frame ----------------
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=40, y=70, width=850, height=550)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.shop_table = ttk.Treeview(Table_Frame, columns=('id', 'name', 'contact', 'address', 'item', 'quantity', 'price'),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.shop_table.heading("id", text="ID")
        self.shop_table.heading("name", text="Name")
        self.shop_table.heading("contact", text="Contact")
        self.shop_table.heading("address", text="Address")
        self.shop_table.heading("item", text="Item Name")
        self.shop_table.heading("quantity", text="Quantity")
        self.shop_table.heading("price", text="Price")
        self.shop_table['show'] = 'headings'
        self.shop_table.column("id", width=100)
        self.shop_table.column("name", width= 200)
        self.shop_table.column("contact", width=100)
        self.shop_table.column("address", width=400)
        self.shop_table.column("item", width=200)
        self.shop_table.column("quantity", width=100)
        self.shop_table.column("price", width=100)
        self.shop_table.pack(fill=BOTH, expand=1)
        self.shop_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_items(self):
        if self.name_var.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        else:
            con = pymysql.connect(host="127.0.0.1", user="root", password="pwd", database="shop")
            cur = con.cursor()
            cur.execute("insert into shopmanagement values(%s, %s, %s, %s, %s, %s, %s)",
                        (self.id,
                         self.name_var.get(),
                         self.contact_var.get(),
                         self.txt_address.get('1.0', END),
                         self.item_var.get(),
                         self.quantity_var.get(),
                         self.price_var.get()
                         ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")


    def fetch_data(self):
        con = pymysql.connect(host="127.0.0.1", user="root", password="pwd", database="shop")
        cur = con.cursor()
        cur.execute("select Id, Name , Contact, Address, Item, Quantity ,Price from shopmanagement order by Id Desc")
        rows = cur.fetchall()
        if len(rows)!= 0:
            self.shop_table.delete(*self.shop_table.get_children())
            for row in rows:
                self.shop_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.name_var.set("")
        self.contact_var.set("")
        self.txt_address.delete("1.0", END)
        self.item_var.set("")
        self.quantity_var.set("")
        self.price_var.set("")

    def get_cursor(self, ev):
        cursor_row= self.shop_table.focus()
        content=self.shop_table.item(cursor_row)
        row=content['values']
        print(row)
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.contact_var.set(row[2])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[3])
        self.item_var.set(row[4])
        self.quantity_var.set(row[5])
        self.price_var.set(row[6])

    def update_data(self):

        con = pymysql.connect(host="127.0.0.1", user="root", password="pwd", database="shop")
        cur = con.cursor()

        cur.execute("update shopmanagement set name = %s, contact = %s, address = %s, item = %s, quantity = %s, price = %s where id = %s",
                    (
                     self.name_var.get(),
                     self.contact_var.get(),
                     self.txt_address.get("1.0", END),
                     self.item_var.get(),
                     self.quantity_var.get(),
                     self.price_var.get(),
                     self.id_var.get()

                    ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="127.0.0.1", user="root", password="pwd", database="shop")
        cur = con.cursor()
        cur.execute("delete from shopmanagement where id=%s", self.id_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="127.0.0.1", user="root", password="pwd", database="shop")
        cur = con.cursor()
        cur.execute("select * from shopmanagement where "+str(self.search_by.get())+" = '"+str(self.search_txt.get())+"'")
        rows = cur.fetchall()
        if len(rows)!= 0:
            self.shop_table.delete(*self.shop_table.get_children())
            for row in rows:
                self.shop_table.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
ob = shop(root)
root.mainloop()