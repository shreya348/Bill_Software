from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import random,os
import sqlite3
from tkinter import messagebox
import tempfile
from time import strftime



class Bill_App:
  def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        
        #Variables
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        #self.product=StringVar()
        self.subcategory=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


    #Prodcut categories list
        self.Category=["Select Option","Fruits","Vegetables","Dairy","Bread/Bakery","Cereals/Pulses","Snacks","Beverages"]
        self.SubCatFruits=["Apples","Mangoes","Bananas","Oranges","Watermelon"]
        self.price_Apples= 100
        self.price_Mangoes= 100
        self.price_banana=40
        self.price_Orange= 50
        self.price_watermelon= 70

        self.SubCatVeggie=["Spinach","Potato","Tomato","Green chillies","Onion"]
        self.price_spinach=20
        self.price_potato=40
        self.price_tomato=30
        self.price_green=20
        self.price_onion=50
            
        self.SubCatDairy=["Milk","Cheese","Egg","Paneer"]
        self.price_Milk= 40
        self.price_cheese = 100
        self.price_egg= 40
        self.price_paneer = 120

        self.SubCatBread=["White bread","Whole wheat bread","Multi grain","French bread"]
        self.price_white=40
        self.price_whole=45
        self.price_multi=50
        self.price_french=70

        self.SubCatCereals=["Rice","Wheat","Oats","Chickpea","Lentils","Beans","Dry peas"]
        self.price_rice=45
        self.price_wheat=50
        self.price_oats=50
        self.price_chickpea=20
        self.price_lentils=30
        self.price_beans=35
        self.price_drypeas=40
            

        self.SubCatSnacks=["Chips","Popcorn","Chocolates","Biscuits"]
        self.Chips=["Lays","Balaji","Bingo"]
        self.price_Lays=10
        self.price_Balaji=10
        self.price_Bingo=10

        self.Chocolates=["Dairy Milk","Kitkat","Fivestar"]
        self.price_Dairymilk=20
        self.price_Kitkat=20
        self.price_Five=10

        self.Biscuits=["Oreo","Good day","Hide and Seek"]
        self.price_Oreo=30
        self.price_Good=20
        self.price_Hide=30       

        self.SubCatBev=["Soft Drink","Fruit juices","Coffee"]
        self.Soft_Drinks=["Pepsi","Coke","Cocacola","Sprite"]
        self.price_pepsi=40
        self.price_Coke=30
        self.price_Cocacola=30
        self.price_Sprite=30
        
        self.Fruit_Juices=["Tropicana","Real"]
        self.price_tropicana=["125-1L"]
        self.price_real=100

        self.Coffee=["Nescafe","Bru","Davidoff"]
        self.price_nes= 30

        #image 1
        img=Image.open("image/istockphoto-1157106624-612x612.jpg")
        img=img.resize((400,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lb1_img=Label(self.root,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=400,height=130)

    #image 2
        img_1=Image.open("image/istockphoto-835833518-170667a.jpg")
        img_1=img_1.resize((400,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        
        lb1_img_1=Label(self.root,image=self.photoimg_1)
        lb1_img_1.place(x=400,y=0,width=400,height=130)
    
    #image 3 
        img_2=Image.open("image/istockphoto-995038782-612x612.jpg")
        img_2=img_2.resize((480,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        lb1_img_2=Label(self.root,image=self.photoimg_2)
        lb1_img_2.place(x=800,y=0,width=480,height=130)

        lb1_title=Label(self.root,text="Nature's Basket",font=("times new roman",35,"bold"),bg="lightgreen",fg="indigo")
        lb1_title.place(x=0,y=130,width=1300,height=45)
        
        #Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)    #1000=1 sec


        lbl = Label(lb1_title,font=('times new roman',16,'bold'),bg='light green',fg='indigo')
        lbl.place(x=0,y=0,width=120,height=45) 
        time()  

        
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1400,height=620)
        
        #Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="indigo")
        Cust_Frame.place(x=0,y=5,width=200,height=140)
        
        self.lb1_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lb1_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",12,"bold"),width=10)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.lb1CustName=Label(Cust_Frame,font=("times new roman",12,"bold"),text="Name",bd=4)
        self.lb1CustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=10)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        
        self.lb1Email=Label(Cust_Frame,text="Email",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lb1Email.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=10)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        #product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="indigo")
        Product_Frame.place(x=205,y=5,width=700,height=140)
        
        self.lb1Category=Label(Product_Frame,text="Select Categories",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lb1Category.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("times new roman",12,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)
        
        #subcategory
        self.lb1SubCategory=Label(Product_Frame,text="Subcategories",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lb1SubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.Combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],textvariable=self.subcategory,font=("times new roman",12,"bold"),width=24,state="readonly")
        self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.price)
        
    #product Name
   # self.lb1Product=Label(Product_Frame,text="Product Name",font=("times new roman",12,"bold"),bg="white",bd=4)
   # self.lb1Product.grid(row=2,column=0,sticky=W,padx=5,pady=2)
    
    #self.ComboProduct=ttk.Combobox(Product_Frame,font=("times new roman",12,"bold"),width=24,state="readonly")
    #self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
    #price
        self.lb1PPrice=Label(Product_Frame,text="Price",font=("times new roman",12,"bold"),bg="white", bd=4)
        self.lb1PPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        
        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("times new roman",12,"bold"),width=18,state="readonly")
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        
        #quantity
        self.lb1Qty=Label(Product_Frame,text="Qty",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lb1Qty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        
        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("times new roman",12,"bold"),width=20)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        

        
        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=900,height=340)
        
        #image 4
        img_3=Image.open("image/istockphoto-1315699311-170667a.jpg")
        img_3=img_3.resize((450,200),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        
        lb1_img_3=Label(MiddleFrame,image=self.photoimg_3)
        lb1_img_3.place(x=0,y=0,width=450,height=200)

        #image 5
        img_4=Image.open("image/shopping-879498__480.jpg")
        img_4=img_4.resize((450,200),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)
        
        lb1_img_4=Label(MiddleFrame,image=self.photoimg_4)
        lb1_img_4.place(x=450,y=0,width=450,height=200)

        #search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=920,y=10,width=500,height=40)
        
        self.lb1Bill=Label(Search_Frame,font=("times new roman",12,"bold"),fg="white",bg="indigo",text="Bill Number")
        self.lb1Bill.grid(row=0,column=0,sticky=W,padx=1)
        
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",12,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)
        
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("times new roman",10,"bold"),bg="green",fg="white",width=5,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)
        
        
        #Right Frame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="indigo")
        RightLabelFrame.place(x=920,y=45,width=340,height=305)
        
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="indigo",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        #Bill counter label frame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="indigo")
        Bottom_Frame.place(x=0,y=350,width=1265,height=120)
        
        self.lb1SubTotal=Label(Bottom_Frame,text="Sub Total",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lb1SubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.EntySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("times new roman",12,"bold"),width=20)
        self.EntySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.lb1_Tax=Label(Bottom_Frame,text="Tax",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lb1_Tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_Tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("times new roman",12,"bold"),width=20)
        self.txt_Tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.AmountTotal=Label(Bottom_Frame,text="Total",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.AmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.AmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("times new roman",12,"bold"),width=20)
        self.AmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        #Buttom Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)
        
        self.BtnAddtoCart=Button(Btn_Frame,command=self.AddItem,height=3,text="Add To Cart",font=("times new roman",10,"bold"),bg="indigo",fg="white",width=20,cursor="hand2")
        self.BtnAddtoCart.grid(row=0,column=0)
        
        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=3,text="Generate Bill",font=("times new roman",10,"bold"),bg="indigo",fg="white",width=20,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)
        
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=3,text="Save Bill",font=("times new roman",10,"bold"),bg="indigo",fg="white",width=20,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)
        
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=3,text="Print",font=("times new roman",10,"bold"),bg="indigo",fg="white",width=20,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)
        
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=3,text="Clear",font=("times new roman",10,"bold"),bg="indigo",fg="white",width=20,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)
        
        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=3,text="Exit",font=("times new roman",10,"bold"),bg="indigo",fg="white",width=20,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()
        
        self.l=[]
      #************FUNCTION DECLARATION**************
  def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.Combo_SubCategory.get()=="":
            messagebox.showerror("Error","Please select the product")
        else:
            self.textarea.insert(END,f"\n {self.Combo_SubCategory.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%2f'%(((sum(self.l)) + ((((sum(self.l)) - self.prices.get()))*Tax)/100))))
  def reg(self):
        CustName = self.c_name.get()
        CustMob = self.c_phone.get()
        conn = sqlite3.connect("grodetails.db")
        c=conn.cursor()
        c.execute("INSERT INTO grocerypy VALUES ('"+CustName+"','"+CustMob+"')")
        conn.commit()
        conn.close()  
        
  def gen_bill(self):
      if self.Combo_SubCategory.get()=="":
          messagebox.showerror("Error","Please Add to cart the product")
      else:
          text=self.textarea.get(10.0,(10.0+float(len(self.l))))
          self.welcome()
          self.textarea.insert(END,text)
          self.textarea.insert(END,"\n===================================")
          self.textarea.insert(END,f"\n Sub Amount:\t\t{self.sub_total.get()}")
          self.textarea.insert(END,f"\n Tax Amount:\t\t{self.tax_input.get()}")
          self.textarea.insert(END,f"\n Total Amount:\t\t{self.total.get()}")
          self.textarea.insert(END,f"\n===================================")
          
  def save_bill(self):
      op=messagebox.askyesno("Save Bill","Do you want to save the bill")
      if op>0:
          self.bill_data=self.textarea.get(1.0,END)
          f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
          f1.write(self.bill_data)
          op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
          f1.close()
          
  def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


  def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")


  def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        #self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")

     ##WELCOME PAGE
  def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t  Welcome to Nature's Basket")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email :{self.c_email.get()}")

        self.textarea.insert(END,"\n===================================")
        self.textarea.insert(END,"\n Products \t\tQty\t\tPrice")
        self.textarea.insert(END,"\n===================================\n")



  
  def Categories(self,event=""):
        if self.Combo_Category.get()=="Fruits":
            self.Combo_SubCategory.config(value=self.SubCatFruits)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Vegetables":
            self.Combo_SubCategory.config(value=self.SubCatVeggie)
            self.Combo_SubCategory.current(0)
        
        if self.Combo_Category.get()=="Dairy":
            self.Combo_SubCategory.config(value=self.SubCatDairy)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Bread/Bakery":
            self.Combo_SubCategory.config(value=self.SubCatBread)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Cereals/Pulses":
            self.Combo_SubCategory.config(value=self.SubCatCereals)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Snacks":
            self.Combo_SubCategory.config(value=self.SubCatSnacks)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=="Beverages":
            self.Combo_SubCategory.config(value=self.SubCatBev)
            self.Combo_SubCategory.current(0) 

  def price(self,event=""):
        #Fruits
        if self.Combo_SubCategory.get()=="Apples":
            self.ComboPrice.config(value=self.price_Apples)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_SubCategory.get()=="Mangoes":
            self.ComboPrice.config(value=self.price_Mangoes)
            self.ComboPrice.current(0)
            self.qty.set(1)        

        if self.Combo_SubCategory.get()=="Bananas":
            self.ComboPrice.config(value=self.price_banana)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_SubCategory.get()=="Oranges":
            self.ComboPrice.config(value=self.price_Orange)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Watermelon":
            self.ComboPrice.config(value=self.price_watermelon)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #vegetables "Spinach","Potato","Tomato","Green chillies","Onion"
        if self.Combo_SubCategory.get()=="Spinach":
            self.ComboPrice.config(value=self.price_spinach)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_SubCategory.get()=="Potato":
            self.ComboPrice.config(value=self.price_potato)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Tomato":
            self.ComboPrice.config(value=self.price_tomato)
            self.ComboPrice.current(0)
            self.qty.set(1)     

        if self.Combo_SubCategory.get()=="Green chillies":
            self.ComboPrice.config(value=self.price_green)
            self.ComboPrice.current(0)
            self.qty.set(1)     

        if self.Combo_SubCategory.get()=="Onion":
            self.ComboPrice.config(value=self.price_onion)
            self.ComboPrice.current(0)
            self.qty.set(1)   

        #Dairy "Milk","Cheese","Egg","Paneer"
        if self.Combo_SubCategory.get()=="Milk":
            self.ComboPrice.config(value=self.price_Milk)
            self.ComboPrice.current(0)
            self.qty.set(1)      

        if self.Combo_SubCategory.get()=="Cheese":
            self.ComboPrice.config(value=self.price_cheese)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Egg":
            self.ComboPrice.config(value=self.price_egg)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Paneer":
            self.ComboPrice.config(value=self.price_paneer)
            self.ComboPrice.current(0)
            self.qty.set(1)   

        #Bread "White bread","Whole wheat bread","Multi grain","French bread"
        if self.Combo_SubCategory.get()=="White bread":
            self.ComboPrice.config(value=self.price_white)
            self.ComboPrice.current(0)
            self.qty.set(1)     

        if self.Combo_SubCategory.get()=="Whole wheat bread":
            self.ComboPrice.config(value=self.price_whole)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Multi grain":
            self.ComboPrice.config(value=self.price_multi)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_SubCategory.get()=="French bread":
            self.ComboPrice.config(value=self.price_french)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        #Cereals "Rice","Wheat","Oats","Chickpea","Lentils","Beans","Dry peas"
        if self.Combo_SubCategory.get()=="Rice":
            self.ComboPrice.config(value=self.price_rice)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Wheat":
            self.ComboPrice.config(value=self.price_wheat)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Oats":
            self.ComboPrice.config(value=self.price_oats)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Chickpea":
            self.ComboPrice.config(value=self.price_chickpea)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_SubCategory.get()=="Lentils":
            self.ComboPrice.config(value=self.price_lentils)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Beans":
            self.ComboPrice.config(value=self.price_beans)
            self.ComboPrice.current(0)
            self.qty.set(1)    

        if self.Combo_SubCategory.get()=="Dry peas":
            self.ComboPrice.config(value=self.price_drypeas)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #snacks "Chips","Popcorn","Chocolates","Biscuits"
        if self.Combo_SubCategory.get()=="Chips":
            self.ComboPrice.config(value=self.price_chips)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_SubCategory.get()=="Popcorn":
            self.ComboPrice.config(value=self.price_popcorn)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_SubCategory.get()=="Chocolates":
            self.Combo_Price.config(value=self.price_chocolates)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Combo_SubCategory.get()=="Biscuits":
            self.ComboPrice.config(value=self.price_biscuits)
            self.ComboPrice.current(0)
            self.qty.set(1)            
     
        #beverages "Soft Drink","Fruit juices","Coffee
        if self.Combo_SubCategory.get()=="Sof Drinks":
            self.ComboPrice.config(value=self.price_softdrinks)
            self.ComboPrice.current(0)
            self.qty.set(1)  

        if self.Combo_SubCategory.get()=="Fruit juices":
            self.ComboPrice.config(value=self.price_fruitsjuices)
            self.ComboPrice.current(0)
            self.qty.set(1)      
        
        if self.Combo_SubCategory.get()=="Coffee":
            self.ComboPrice.config(value=self.price_coffee)
            self.ComboPrice.current(0)
            self.qty.set(1)  


  
  
  
   
    
  
    
    
    
    
    
    
if __name__=='__main__':
        root=Tk()
        obj=Bill_App(root)
        root.mainloop()

      