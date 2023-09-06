from tkinter import*
from tkinter import messagebox
import random,os,tempfile
#functionality part

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberentry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('ERROR','Invalid Bill Number')




if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the Bill')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('SUCCESS',f'Bill Number{billnumber} is saved successfully' )
        billnumber = random.randint(500,1000)


billnumber=random.randint(500,1000)
def bill_area():
    if nameentry.get()=='' or phoneentry.get()=='':
        messagebox.showerror('Error','Customer Details are Required')
    elif cosmeticpriceentry.get()=='' and grocerypriceentry.get()=='' and colddrinkspriceentry.get()=='':
        messagebox.showerror('Error', 'No Products are selected')
    elif cosmeticpriceentry.get()=='0RS' and grocerypriceentry.get()=='0RS' and colddrinkspriceentry.get()=='0RS':
        messagebox.showerror('Error', 'No Products are selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameentry.get()}\n')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneentry.get()}\n')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================')
        if bathsoapentry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapentry.get()}\t\t\t{soapprice} RS')
        if hairsprayentry.get()!='0':
            textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayentry.get()}\t\t\t{hairsprayprice} RS')
        if hairgelentry.get() != '0':
            textarea.insert(END, f'\nHair Gel\t\t\t{hairgelentry.get()}\t\t\t{hairgelprice} RS')
        if facewashentry.get() != '0':
            textarea.insert(END, f'\nFace Wash\t\t\t{facewashentry.get()}\t\t\t{facewashprice} RS')
        if facecreamentry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{facecreamentry.get()}\t\t\t{facecreamprice} RS')
        if bodylotionentry.get() != '0':
            textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotionentry.get()}\t\t\t{bodylotionprice} RS')


        if riceentry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceentry.get()}\t\t\t{riceprice} RS')
        if oilentry.get() != '0':
            textarea.insert(END, f'\noil\t\t\t{oilentry.get()}\t\t\t{oilprice} RS')
        if daalentry.get() != '0':
            textarea.insert(END, f'\nDaal\t\t\t{daalentry.get()}\t\t\t{daalprice} RS')
        if sugarentry.get() != '0':
            textarea.insert(END, f'\nSugar\t\t\t{sugarentry.get()}\t\t\t{sugarprice} RS')
        if teaentry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{teaentry.get()}\t\t\t{teaprice} RS')
        if wheatentry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatentry.get()}\t\t\t{wheatprice} RS')


        if maazaentry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaentry.get()}\t\t\t{maazaprice} RS')
        if frootientry.get() != '0':
            textarea.insert(END, f'\Frooti\t\t\t{frootientry.get()}\t\t\t{frootiprice} RS')
        if pepsientry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsientry.get()}\t\t\t{pepsiprice} RS')
        if cocacolaentry.get() != '0':
            textarea.insert(END, f'\nCoca Cola\t\t\t{cocacolaentry.get()}\t\t\t{cocacolaprice} RS')
        if dewentry.get() != '0':
            textarea.insert(END, f'\nDew\t\t\t{dewentry.get()}\t\t\t{dewprice} RS')
        if spriteentry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t\t{spriteentry.get()}\t\t\t{spriteprice} RS')
        textarea.insert(END, '\n-------------------------------------------------------')

        if cosmetictaxentry.get()!='0.0RS':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmetictaxentry.get()}')
        if grocerytaxentry.get()!='0.0RS':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxentry.get()}')
        if colddrinkstaxentry.get()!='0.0RS':
            textarea.insert(END,f'\nDrinks Tax\t\t\t\t{colddrinkstaxentry.get()}')
        textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')
        textarea.insert(END, '\n-------------------------------------------------------')
        save_bill()

def total():
    global soapprice,hairsprayprice,hairgelprice,facewashprice,facecreamprice,bodylotionprice
    global riceprice, daalprice, oilprice, sugarprice, teaprice, wheatprice
    global maazaprice,frootiprice,dewprice,spriteprice,cocacolaprice,pepsiprice
    global totalbill
    #cosmetic price calaculation
    soapprice=int(bathsoapentry.get())*20
    facecreamprice=int(facecreamentry.get())*50
    facewashprice = int(facewashentry.get()) * 100
    hairsprayprice = int(hairsprayentry.get()) * 150
    hairgelprice = int(hairgelentry.get()) * 80
    bodylotionprice = int(bodylotionentry.get()) * 60

    totalcosmeticprice= soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceentry.delete(0,END)
    cosmeticpriceentry.insert(0,str(totalcosmeticprice)+'RS')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxentry.delete(0,END)
    cosmetictaxentry.insert(0,str(cosmetictax)+'RS')

#grocery price calculation
    riceprice=int(riceentry.get())*200
    daalprice = int(daalentry.get()) * 100
    oilprice = int(oilentry.get()) * 120
    sugarprice = int(sugarentry.get()) * 50
    teaprice = int(teaentry.get()) * 140
    wheatprice = int(wheatentry.get()) * 80

    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
    grocerypriceentry.delete(0,END)
    grocerypriceentry.insert(0,str(totalgroceryprice)+'RS')
    grocerytax = totalgroceryprice * 0.05
    grocerytaxentry.delete(0, END)
    grocerytaxentry.insert(0, str(grocerytax) + 'RS')

    #COLD DRINK PRICE CALCULATION
    maazaprice = int(maazaentry.get())*50
    frootiprice = int(frootientry.get()) *20
    dewprice = int(dewentry.get()) * 30
    pepsiprice = int(pepsientry.get()) * 20
    spriteprice = int(spriteentry.get()) * 45
    cococolaprice = int(cocacolaentry.get()) * 90

    totalcolddrinkprice=maazaprice+frootiprice+dewprice+pepsiprice+spriteprice+cococolaprice
    colddrinkspriceentry.delete(0,END)
    colddrinkspriceentry.insert(0,str(totalcolddrinkprice)+'RS')
    colddrinktax = totalcolddrinkprice * 0.08
    colddrinkstaxentry.delete(0, END)
    colddrinkstaxentry.insert(0, str(colddrinktax) + 'RS')

    totalbill=totalcosmeticprice+totalcolddrinkprice+totalgroceryprice+cosmetictax+grocerytax+colddrinktax

#GUI PART
root = Tk()
root.geometry('1270x685')
root.title("RETAIL BILLING SYSTEM")
root.iconbitmap('icon.ico')
headinglabel=Label(root,text="Retail Billing System",font=('times new roman',30,'bold')
                   ,bg='light steel blue',fg='navy',relief='groove')
headinglabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold')
                                  ,fg='navy',bd=8,relief=GROOVE,bg='light steel blue')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame, text='Name',font=('times new roman',15,'bold'),bg='light steel blue')
nameLabel.grid(row=0,column=0,padx=20,pady=2)
nameentry=Entry(customer_details_frame,font=("arial",'15'),bd=7,width=18)
nameentry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame, text='Phone Number',font=('times new roman',15,'bold'),bg='light steel blue')
phoneLabel.grid(row=0,column=2,padx=20)
phoneentry=Entry(customer_details_frame,font=("arial",'15'),bd=7,width=18)
phoneentry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame, text='Bill Number',font=('times new roman',15,'bold'),bg='light steel blue')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)
billnumberentry=Entry(customer_details_frame,font=("arial",'15'),bd=7,width=18)
billnumberentry.grid(row=0,column=5,padx=8)

searchbutton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchbutton.grid(row=0,column=6,padx=20,pady=8)


productsframe=Frame(root)
productsframe.pack()

cosmeticsframe=LabelFrame(productsframe,text='Cosmetics',font=('times new roman',15,'bold')
                                  ,fg='navy',bd=8,relief=GROOVE,bg='light steel blue')
cosmeticsframe.grid(row=0,column=0)

bathsoaplabel=Label(cosmeticsframe,text='Bath Soap',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
bathsoaplabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")
bathsoapentry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapentry.grid(row=0,column=1,pady=9,padx=10)
bathsoapentry.insert(0,0)

facecreamlabel=Label(cosmeticsframe,text='Face Cream',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
facecreamlabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")
facecreamentry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamentry.grid(row=1,column=1,pady=9,padx=10)
facecreamentry.insert(0,0)

facewashlabel=Label(cosmeticsframe,text='Face Wash',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
facewashlabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")
facewashentry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,bd=5)
facewashentry.grid(row=2,column=1,pady=9,padx=10 )
facewashentry.insert(0,0)

hairspraylabel=Label(cosmeticsframe,text='Hair Spray',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
hairspraylabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")
hairsprayentry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayentry.grid(row=3,column=1,pady=9,padx=10 )
hairsprayentry.insert(0,0)

hairgellabel=Label(cosmeticsframe,text='Hair Gel',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
hairgellabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelentry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelentry.grid(row=4,column=1,pady=9,padx=10)
hairgelentry.insert(0,0)

bodylotionlabel=Label(cosmeticsframe,text='Body Lotion',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
bodylotionlabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodylotionentry=Entry(cosmeticsframe,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionentry.grid(row=5,column=1,pady=9,padx=10)
bodylotionentry.insert(0,0)

groceryframe=LabelFrame(productsframe,text='Grocery',font=('times new roman',15,'bold')
                                  ,fg='navy',bd=8,relief=GROOVE,bg='light steel blue')
groceryframe.grid(row=0,column=1)

ricelabel=Label(groceryframe,text='Rice',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
ricelabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceentry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,bd=5)
riceentry.grid(row=0,column=1,pady=9,padx=10)
riceentry.insert(0,0)

oillabel=Label(groceryframe,text='Oil',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
oillabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilentry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,bd=5)
oilentry.grid(row=1,column=1,pady=9,padx=10)
oilentry.insert(0,0)

daallabel=Label(groceryframe,text='Daal',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
daallabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
daalentry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,bd=5)
daalentry.grid(row=2,column=1,pady=9,padx=10)
daalentry.insert(0,0)

wheatlabel=Label(groceryframe,text='Wheat',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
wheatlabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatentry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,bd=5)
wheatentry.grid(row=3,column=1,pady=9,padx=10)
wheatentry.insert(0,0)

sugarlabel=Label(groceryframe,text='Sugar',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
sugarlabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarentry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,bd=5)
sugarentry.grid(row=4,column=1,pady=9,padx=10)
sugarentry.insert(0,0)

tealabel=Label(groceryframe,text='Tea',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
tealabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
teaentry=Entry(groceryframe,font=('times new roman',15,'bold'),width=10,bd=5)
teaentry.grid(row=5,column=1,pady=9,padx=10)
teaentry.insert(0,0)


colddrinksframe=LabelFrame(productsframe,text='Cold Drinks',font=('times new roman',15,'bold')
                                  ,fg='navy',bd=8,relief=GROOVE,bg='light steel blue')
colddrinksframe.grid(row=0,column=2)

maazalabel=Label(colddrinksframe,text='Maaza',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
maazalabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
maazaentry=Entry(colddrinksframe,font=('times new roman',15,'bold'),width=10,bd=5)
maazaentry.grid(row=0,column=1,pady=9,padx=10)
maazaentry.insert(0,0)

pepsilabel=Label(colddrinksframe,text='Pepsi',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
pepsilabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsientry=Entry(colddrinksframe,font=('times new roman',15,'bold'),width=10,bd=5)
pepsientry.grid(row=1,column=1,pady=9,padx=10)
pepsientry.insert(0,0)

spritelabel=Label(colddrinksframe,text='Sprite',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
spritelabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteentry=Entry(colddrinksframe,font=('times new roman',15,'bold'),width=10,bd=5)
spriteentry.grid(row=2,column=1,pady=9,padx=10)
spriteentry.insert(0,0)

dewlabel=Label(colddrinksframe,text='Dew',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
dewlabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
dewentry=Entry(colddrinksframe,font=('times new roman',15,'bold'),width=10,bd=5)
dewentry.grid(row=3,column=1,pady=9,padx=10)
dewentry.insert(0,0)

frootilabel=Label(colddrinksframe,text='Frooti',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
frootilabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
frootientry=Entry(colddrinksframe,font=('times new roman',15,'bold'),width=10,bd=5)
frootientry.grid(row=4,column=1,pady=9,padx=10)
frootientry.insert(0,0)

cocacolalabel=Label(colddrinksframe,text='Coca Cola',font=('times new roman',15,'bold'),bg='light steel blue'
                    ,fg='black')
cocacolalabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
cocacolaentry=Entry(colddrinksframe,font=('times new roman',15,'bold'),width=10,bd=5)
cocacolaentry.grid(row=5,column=1,pady=9,padx=10)
cocacolaentry.insert(0,0)

billframe=Frame(productsframe,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billarealabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


billmenuframe=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold')
                                  ,fg='navy',bd=8,relief=GROOVE,bg='light steel blue')
billmenuframe.pack()

cosmeticpricelabel=Label(billmenuframe,text='Cosmetic Price',font=('times new roman',14,'bold'),bg='light steel blue'
                    ,fg='black')
cosmeticpricelabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
cosmeticpriceentry=Entry(billmenuframe,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticpriceentry.grid(row=0,column=1,pady=6,padx=10)

grocerypricelabel=Label(billmenuframe,text='Grocery Price',font=('times new roman',14,'bold'),bg='light steel blue'
                    ,fg='black')
grocerypricelabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')
grocerypriceentry=Entry(billmenuframe,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceentry.grid(row=1,column=1,pady=6,padx=10)


colddrinkspricelabel=Label(billmenuframe,text='Cold Drinks Price',font=('times new roman',14,'bold'),bg='light steel blue'
                    ,fg='black')
colddrinkspricelabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
colddrinkspriceentry=Entry(billmenuframe,font=('times new roman',14,'bold'),width=10,bd=5)
colddrinkspriceentry.grid(row=2,column=1,pady=6,padx=10)


cosmetictaxlabel=Label(billmenuframe,text='Cosmetic Tax',font=('times new roman',14,'bold'),bg='light steel blue'
                    ,fg='black')
cosmetictaxlabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
cosmetictaxentry=Entry(billmenuframe,font=('times new roman',14,'bold'),width=10,bd=5)
cosmetictaxentry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxlabel=Label(billmenuframe,text='Grocery Tax',font=('times new roman',14,'bold'),bg='light steel blue'
                    ,fg='black')
grocerytaxlabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxentry=Entry(billmenuframe,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxentry.grid(row=1,column=3,pady=6,padx=10)


colddrinkstaxlabel=Label(billmenuframe,text='Cold Drinks Tax',font=('times new roman',14,'bold'),bg='light steel blue'
                    ,fg='black')
colddrinkstaxlabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
colddrinkstaxentry=Entry(billmenuframe,font=('times new roman',14,'bold'),width=10,bd=5)
colddrinkstaxentry.grid(row=2,column=3,pady=6,padx=10)


buttonframe=Frame(billmenuframe,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

totalbuttonframe=Button(buttonframe,text='TOTAL',font=('arial',16,'bold')
                        ,bg='light steel blue',bd=5,width=8,pady=10,command=total)
totalbuttonframe.grid(row=0,column=0,pady=20,padx=5)

billbuttonframe=Button(buttonframe,text='BILL',font=('arial',16,'bold'),bg='light steel blue',bd=5,width=8,pady=10,command=bill_area)
billbuttonframe.grid(row=0,column=1,pady=20,padx=5)

emailbuttonframe=Button(buttonframe,text='EMAIL',font=('arial',16,'bold'),bg='light steel blue',bd=5,width=8,pady=10)
emailbuttonframe.grid(row=0,column=2,pady=20,padx=5)

printbuttonframe=Button(buttonframe,text='PRINT',font=('arial',16,'bold'),bg='light steel blue',bd=5,width=8,pady=10,command=print_bill)
printbuttonframe.grid(row=0,column=3,pady=20,padx=5)

clearbuttonframe=Button(buttonframe,text='CLEAR',font=('arial',16,'bold'),bg='light steel blue',bd=5,width=8,pady=10)
clearbuttonframe.grid(row=0,column=4,pady=20,padx=5)
root.mainloop()
