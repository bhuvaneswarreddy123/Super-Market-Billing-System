import tkinter as tk
import pymysql
from tkinter import messagebox
class bill():
    def __init__(self,root):
        self.root = root
        self.root.title("Super Market")
        scrn_width = self.root.winfo_screenwidth()
        scrn_height = self.root.winfo_screenheight()
        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")
        mainTitle = tk.Label(self.root,text = "Super Market Billing System",bg="light gray" , fg="red" , bd=5,relief="groove",font=("Arial",40,"bold"))
        mainTitle.pack(side="top",fill="x")
        #---Variables----
        self.total = tk.IntVar()

        #----Input Frame --------

        self.inputFrame = tk.Frame(self.root,bg = "light gray" , bd =5 ,relief="groove")
        self.inputFrame.place(x=10,y=90,width=400,height=550)

        item = tk.Label(self.inputFrame,text = "Item Name :" ,bg = "light gray" , font = ("Arial",15,"bold"))
        item.grid(row=0,column=0,padx=10,pady=30)
        self.ItemIn = tk.Entry(self.inputFrame,bd=2,width=15,font=("Arial",15,"bold"))
        self.ItemIn.grid(row=0,column=1,pady=5)

        quant = tk.Label(self.inputFrame,text = "Item Quantity :" ,bg = "light gray" , font = ("Arial",15,"bold"))
        quant.grid(row=1,column=0,padx=10,pady=30)
        self.quantIn = tk.Entry(self.inputFrame,bd=2,width=15,font=("Arial",15,"bold"))
        self.quantIn.grid(row=1,column=1,pady=30)

        purchaseBtn = tk.Button(self.inputFrame,command = self.purchase,text="Purchase",bd=2,relief='raised',bg="sky blue",font=("Arial",15,"bold"))
        purchaseBtn.grid(row=2,column=0,padx=30,pady=70)

        PrintBillBtn = tk.Button(self.inputFrame,command=self.print_bill,text="Print Bill",bd=2,relief='raised',width=10,bg="sky blue",font=("Arial",15,"bold"))
        PrintBillBtn.grid(row=2,column=1,padx=40,pady=70)

        addBtn = tk.Button(self.inputFrame,command=self.add_fun,text="Add Item",bd=2,bg="sky blue",width=15,relief="groove",font=("Arial",15,"bold"))
        addBtn.grid(row=4,column=0,columnspan=15,padx=40,pady=30)



        #----Detail Fram-----

        self.detailFrame = tk.Frame(self.root,bg = "light gray" , bd =5 ,relief="groove")
        self.detailFrame.place(x=430,y=90,width=840,height=550)

        self.list = tk.Listbox(self.detailFrame,bg="cyan",font=("Arial",15),bd=3,relief="sunken",width=73,height=21)
        self.list.grid(row=0,column=0,padx=10,pady=10)

    def add_fun(self):
        self.addFrame = tk.Frame(self.root,bg="light green",bd=5,relief = "groove")
        self.addFrame.place(x=430,y=90,width=400,height=550)

        itemName = tk.Label(self.addFrame,text = "Item Name :" ,bg = "light green" , font = ("Arial",15,"bold"))
        itemName.grid(row=0,column=0,padx=10,pady=30)
        self.ItemNameIn = tk.Entry(self.addFrame,bd=2,width=15,font=("Arial",15,"bold"))
        self.ItemNameIn.grid(row=0,column=1,pady=5)

        itemquant = tk.Label(self.addFrame,text = "Enter Quantity :" ,bg = "light green" , font = ("Arial",15,"bold"))
        itemquant.grid(row=1,column=0,padx=10,pady=30)
        self.ItemquantIn = tk.Entry(self.addFrame,bd=2,width=15,font=("Arial",15,"bold"))
        self.ItemquantIn.grid(row=1,column=1,pady=5)

        itemprice = tk.Label(self.addFrame,text = "Enter Price :" ,bg = "light green" , font = ("Arial",15,"bold"))
        itemprice.grid(row=2,column=0,padx=10,pady=30)
        self.ItempriceIn = tk.Entry(self.addFrame,bd=2,width=15,font=("Arial",15,"bold"))
        self.ItempriceIn.grid(row=2,column=1,pady=5)
        okBtn = tk.Button(self.addFrame,command=self.insert_fun,text="ok",bd=2,bg="sky blue",width=10,relief="groove",font=("Arial",15,"bold"))
        okBtn.grid(row=3,column=0,pady=30)

        closeBtn = tk.Button(self.addFrame,command=self.close,text="close",bd=2,bg="sky blue",width=10,relief="groove",font=("Arial",15,"bold"))
        closeBtn.grid(row=3,column=1,pady=30)
    
    def close(self):
        self.addFrame.destroy()

    def insert_fun(self):
        self.item_name = self.ItemNameIn.get()
        self.item_quant=self.ItemquantIn.get()
        self.item_price = self.ItempriceIn.get()
        con = pymysql.connect(host="localhost",user="root",passwd="Bhuvan@12$",database="billdb")
        cur = con.cursor()
        cur.execute("insert into item (item_name,item_price,item_quant) values (%s,%s,%s)",(self.item_name,self.item_price,self.item_quant))
        con.commit()
        tk.messagebox.showinfo("success","Item added successfully !")
        con.close()
        self.clear()
    
    def clear(self):
        self.ItemNameIn.delete(0,tk.END)
        self.ItempriceIn.delete(0,tk.END)
        self.ItemquantIn.delete(0,tk.END)
    def purchase(self):
        item = self.ItemIn.get()
        quant = int(self.quantIn.get())
        con = pymysql.connect(host="localhost",user="root",passwd="Bhuvan@12$",database="billdb")
        cur = con.cursor()
        cur.execute("select item_price,item_quant from item where item_name=%s",item)
        data = cur.fetchone()
        if data:
            if data[1]>=quant:
                amount=data[0]*quant
                self.total.set(self.total.get()+amount)
                singleItem = f"price of {quant} {item} is : { amount } "
                self.list.insert(tk.END,singleItem)
                update = data[1]-quant
                cur.execute("update item set item_quant = %s where item_name = %s",(update,item))
                con.commit()
                con.close()
                self.clear_inputframe()

            else:
                tk.messagebox.showerror("Error","Item Quantity does not meet to Requirment")
        else:
            tk.messagebox.showerror("Error","Invalid Item Name !")
    def clear_inputframe(self):
        self.ItemIn.delete(0,tk.END)
        self.quantIn.delete(0,tk.END)
    def print_bill(self):
        line = '-------------------------'
        self.list.insert(tk.END,line)
        print_bill = f"Total Bill -------------:{self.total.get()}"
        self.list.insert(tk.END,print_bill)






























    

root = tk.Tk()
obj  = bill(root)
root.mainloop()