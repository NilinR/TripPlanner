from tkinter import *# import tkinter and all its functions
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from datetime import date
from tkcalendar import Calendar#pip install tkcalendar
import math
import random
import mysql.connector
from PIL import ImageTk, Image
#PIL - Python Image Library (for older image types)
#Pillow - newer fork version of PIL for jpeg, png

root = Tk()# create root window
root.title("Trip Planner") # title of the GUI window
root.state('zoomed') #makes it full screened
root.config(bg="black") # background color

# Creating top frame
top_frame = Frame(root, width=1350 ,height=180, bg='black')
top_frame.grid(row=0, column=0,sticky='W')

#Titles
label1 = Label(top_frame, text = "TRIP PLANNER",font=("Courier New", 35),bg="black",fg="white")
label1.grid(row=0,column=0,sticky='W')

label3=Label(top_frame, text = " ",bg="black")
label3.grid(row=1,column=1,ipadx=150)

#seperator
line_frame=Frame(root, width=1350,height=2,bg='white')
line_frame.grid(row=1, column=0,sticky='W')

#bottom frame
b_frame=Frame(root, width=1350,height=700,bg='black')
b_frame.grid(row=2, column=0,sticky='W',padx=5)
b_frame.pack_propagate(0)#Doesnt allow the widgets inside to determine the dimension
global main_label

# loading image
image1 = PhotoImage(file="p2.png")
image1=image1.subsample(2,2) # resize image using subsample
main_label=Label(b_frame, image=image1,bg='black').pack()


#LOGIN BUTTON
def LOG():
    #Bringing the list frm the file
    with open('data.txt', 'r') as f:
       list1 =f.read()
       loginlist=list(eval(list1)) #turns the string returned into a list

    #login frame
    l_frame = Frame(main_label, bd=2, bg='white',highlightbackground="white", highlightthickness=2,relief=SOLID, padx=10, pady=10)
    l_frame.place(x=380, y=290)
   
    r_uname=""
    r_pwd=""
    l_username=""
    l_pwd=""

    #register function
    def register():
        l_frame.place(x=845, y=335)
        def reg():
            r_uname=register_uname .get()
            r_pwd=register_pwd.get()
            c=1
            while c==1: #infinite loop
                m=register_mobile.get()
                #validation
                if (register_name.get()==''  or register_name.get()==' '): #empty name
                    messagebox.showinfo("Error", "Enter Valid Name")
                    break
                if m.isdigit()==False or len(m)!=10:
                    messagebox.showinfo("Error", "Enter Valid Mobile Number")
                    break
                if (r_uname==" " or r_uname=="" or len(r_uname)<=1): #if no username is typed
                    messagebox.showinfo("Error", "Invalid Username")
                    r_uname="" #emptying the entry
                    break
                if (r_pwd==" " or r_pwd==""or len(r_pwd)<=1):
                    messagebox.showinfo("Error", "Invalid Password")
                    break
                if(pwd_again.get()!=register_pwd.get()):
                   messagebox.showinfo("Error", "Invalid Password")
                   break
               
                else:
                    inp=[r_uname ,r_pwd ] #takes the username and password as a list
                    loginlist.append(inp) #puts them as a nested list
                    #places the updated list back in the file
                    with open('data.txt', 'w') as f:
                        f.write(str(loginlist)) #file takes in string values
                        messagebox.showinfo("Success", "Registered Successfully")
                        right_frame.destroy()
                        l_frame.place(x=475, y=300)
                        break

        #creating frame for register
        right_frame = Frame(main_label, bd=2, bg='white',highlightbackground="white", highlightthickness=2,relief=SOLID, padx=10, pady=10)

        Label(right_frame, text="Enter Name", bg='white',font=('Times', 19)).grid(row=0, column=0, sticky=W, pady=10)
        Label( right_frame,  text="Enter Username",  bg='white', font=('Times', 19) ).grid(row=1, column=0, sticky=W, pady=10)
        Label( right_frame,  text="Contact Number",  bg='white', font=('Times', 19)).grid(row=2, column=0, sticky=W, pady=10)
        Label(right_frame, text="Enter Password", bg='white',font=('Times', 19)).grid(row=5, column=0, sticky=W, pady=10)
        Label(right_frame, text="Re-Enter Password", bg='white',font=('Times', 19)).grid(row=6, column=0, sticky=W, pady=10)

        #taking values
        register_name = Entry(right_frame, font=('Times', 19))
        register_uname = Entry(right_frame, font=('Times', 19))
        register_mobile = Entry(right_frame, font=('Times', 19))
        register_pwd = Entry(right_frame, font=('Times', 19),show='*')
        pwd_again = Entry(right_frame, font=('Times', 19),show='*')
        register_btn = Button(right_frame, width=18, text='Register', font=('Times', 19), relief=SOLID,cursor='hand2',command=reg)

        register_name.grid(row=0, column=1, pady=10, padx=20)
        register_uname.grid(row=1, column=1, pady=10, padx=20)
        register_mobile.grid(row=2, column=1, pady=10, padx=20)
        register_pwd.grid(row=5, column=1, pady=10, padx=20)
        pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=1, pady=10, padx=20)
        right_frame.place(x=300, y=300)
                   
    #login function
    def login():
        l_username = log_uname.get()
        l_pwd = log_pwd.get()
        c=0  #varible to check if username is found

        #validation
        if (l_username==" " or l_username==""):
            messagebox.showinfo("Error", "Invalid Username")
        if (l_pwd==" " or l_pwd==""):
            messagebox.showinfo("Error", "Invalid Password")

        else:#login requirement
            for i in loginlist:
                if l_username in i:
                    c+=1
                    j=loginlist.index(i)
                    if l_pwd==loginlist[j][1]: #checks if the correct password is given
                        messagebox.showinfo("Sucess", "Login sucessfull")
                        l_frame.destroy() #destroys the current window
                        Button(top_frame, text =l_username,font=("Courier New", 20),borderwidth=0,bg="black",fg="white").grid(row=1,column=7,padx=25)
                        break
                    else:
                        messagebox.showinfo("Error", "Wrong Password")
                        break
            if(c==0):
                messagebox.showinfo("Error", "Username not found")
    # Login frame
    Label(l_frame,  text="Enter Username",  bg='white',font=('Times', 19)).grid(row=0, column=0, sticky=W, pady=10)
    Label(l_frame, text="Enter Password", bg='white',font=('Times', 19)).grid(row=1, column=0, sticky='W')
   
    #taking the values using textboxes
    log_uname = Entry(l_frame, font=('Times', 19))
    log_pwd = Entry(l_frame, font=('Times', 19),show='*')

    login_btn = Button(l_frame, width=15, text='Login', font=('Times', 19), relief=SOLID,cursor='hand2',command=login)
    signup= Button(l_frame, width=15, text='Sign-up', font=('Times', 19), relief=SOLID,cursor='hand2',command=register)

   

    # widgets placement
    log_uname.grid(row=0, column=1, pady=10, padx=20)
    log_pwd.grid(row=1, column=1, pady=10, padx=20)
    login_btn.grid(row=2, column=1, pady=10, padx=20)
    Label(l_frame,text="Don't have an account?", bg='white',font=('Times', 19)).grid(row=3, column=0, pady=10)
    signup.grid(row=4,column=0)

LOG()

def flight():
    global frame
    var1= StringVar()
    var2= StringVar()
    frame = Frame(main_label, bd=2, bg='white',highlightbackground="white", highlightthickness=2,relief=SOLID, padx=10, pady=10)
    frame.place(x=5,y=105)
    label3=Label(frame, text="Book Flight",bg='white', font=('Courier 17 bold')).grid(row=2, column=0, padx=4, pady=10, ipadx=2)
    from_label=Label(frame, text="From:",bg='lightgrey', font=('Courier 16 bold ')).grid(row=3, column=0)
    to_label=Label(frame, text="To:",bg='lightgrey', font=('Courier 16 bold')).grid(row=3, column=1, padx=1, pady=3, ipadx=10)
    departure=Label(frame,text="Departure Date",font=('Courier 16 bold')).grid(row=3, column=2, padx=1, pady=3, ipadx=10)
    global cal
    cal = Calendar(frame, selectmode = 'day',year = 2060, month = 12,day = 25)
    def ca():
        cal.grid(row=4, column=2)
    Button(frame,bg='grey',command=ca).grid(row=3, column=3,ipadx=10)
    #entry = Entry(frame,font=('Courier 16 bold'),textvariable = entry_var).grid(row=4, column=2)
    options=["DEL Delhi","BLR Bangaluru","BOM Mumbai","HND Tokyo"]

    w =ttk.Combobox(frame,values=options)
    w.grid(row=4, column=0,padx=1)
    
    x = ttk.Combobox(frame,values=options)
    x.grid(row=4, column=1,padx=10,sticky='w')
            
    def GoFlight():
        Fro=w.get()
        To=x.get()
        c=Fro[0:3]
        d=To[0:3]
        if c==d: #From and To areas cant be same
            messagebox.showinfo("Error", "Choose Valid Options")
        else:
            frame2 = Frame(main_label, bd=2, bg='white',highlightbackground="white", highlightthickness=2,relief=SOLID, padx=10, pady=10)
            frame2.place(x=5,y=105)
            #mysql
            mydb=mysql.connector.connect(host='localhost',user='root',password='1234')
            co=mydb.cursor()
            #for 5 flights
            it=2
            global list1
            list1=[]
            for i in range (5):
                co.execute("use flight")
                if i==0: #during the first loop
                    co.execute("select * from distance")
                    data=co.fetchall()
                    for i in data: #finding distance from both places
                        if (i[0]==c or i[1]==c) and (i[1]==d or i[0]==d):
                            dist=i[2]
                            tim=i[3]
                    Label(frame2,text='Distance:'+str(dist),font=('Courier 12 bold')).grid(row=1,column=1)
                    
                #the average cost of flights is found to be around 6 rs per km
                cost=dist*random.randrange(3,8)
                #to choose random flights
                co.execute("select * from companies")
                dat=co.fetchall()
                comp=dat[random.randrange(0,5)][0]
                time=random.randrange(5,12)
                ti=round(float(time),2)
                dtime=str(ti+tim).split('.')
                list1.append([comp,cost])
                Label(frame2,text=comp,font=('Courier 25 bold')).grid(row=it,column=1)
                Label(frame2,text=str(time)+":00",font=('Courier 18 bold')).grid(row=it+1,column=1)
                Label(frame2,text=str(tim)+"hrs",font=('Courier 18 bold')).grid(row=it+1,column=2)
                Label(frame2,text=dtime[0]+":00",font=('Courier 18 bold')).grid(row=it+1,column=3)
                Label(frame2,text="--------->",font=('Courier 18 bold')).grid(row=it+2,column=2)
                Label(frame2,text= '₹'+str(cost),font=('Courier 18 bold')).grid(row=it+1,column=4)
                Label(frame2,text=Fro[4:],font=('Courier 18 bold')).grid(row=it+2,column=1)
                Label(frame2,text=To[4:],font=('Courier 18 bold')).grid(row=it+2,column=3)
                it+=3

                def stk(lma):
                    #taking previous enties of csv
                    mydb=mysql.connector.connect(host='localhost',user='root',password='1234')
                    co=mydb.cursor()
                    co.execute("use flight")
                    co.execute("select * from companies")
                    data=co.fetchall()
                    with open("rec.txt",'r+')as fr:
                        list2 =fr.read()
                        dat=list(eval(list2))
                        err=0
                        for i in data:
                            for j in range (len(dat)):
                                if lma[0]==i[0] and lma[0]==dat[j][0]:
                                    if i[1]<=5: #making the limit of flight booking 5 at a time
                                        err=1
                                        co.execute("UPDATE Companies SET seats =seats+1 WHERE name="+"\'"+lma[0]+"\'")
                                        mydb.commit()
                                        print("Number of seats taken=:",i[1]+1)
                                        #entering new number
                                        no=dat[j][1]+1
                                        dat[j][1]=no
                                        fr.truncate(0) # to erase all data
                                        fr.seek(0)
                                        fr.write(str(dat))
                    if err==0:
                        co.execute("UPDATE Companies SET seats =0 WHERE name="+"\'"+lma[0]+"\'")
                        mydb.commit()
                        messagebox.showinfo("Error", "Stack Overflow")
                        
                        
                def bil(lm):
                    frame2.destroy()
                    fra= Frame(main_label, bd=2, bg='white',highlightbackground="white", highlightthickness=2,relief=SOLID, padx=10, pady=10)
                    fra.place(x=5,y=105)
                    Label(fra,text=lm[0],font=('Courier 20 bold')).grid(row=0,column=0)
                    Label(fra,text='₹'+str(lm[1]),font=('Courier 20 bold')).grid(row=1,column=1)
                    Label(fra,text=' on '+str(cal.get_date()),font=('Courier 12 bold')).grid(row=0,column=1)
                    Label(fra,text=Fro,font=('Courier 12 bold')).grid(row=2,column=0)
                    Label(fra,text="--------->",font=('Courier 12 bold')).grid(row=2,column=1)
                    Label(fra,text=To,font=('Courier 12 bold')).grid(row=2,column=3)
                    Button(fra,text="Confirm",bg='lawn green',font=('Courier 10 bold'),command=lambda:(fra.destroy(),stk(lm))).grid(row=3,column=0)
                    #lamda places mulitple commands in a button
                    
                def b1():
                    li1=list1[0]
                    frame2.destroy()
                    bil(li1)
                def b2():
                    li1=list1[1]
                    frame2.destroy()
                    bil(li1)
                def b3():
                    li1=list1[2]
                    frame2.destroy()
                    bil(li1)
                def b4():
                    li1=list1[3]
                    frame2.destroy()
                    bil(li1)
                def b5():
                    li1=list1[4]
                    frame2.destroy()
                    bil(li1)
                
        B1=Button(frame2,text=">",bg='lawn green',command=b1).grid(row=3, column=5)
        B2=Button(frame2,text=">",bg='lawn green',command=b2).grid(row=6, column=5)
        B3=Button(frame2,text=">",bg='lawn green',command=b3).grid(row=9, column=5)
        B4=Button(frame2,text=">",bg='lawn green',command=b4).grid(row=12, column=5)
        B5=Button(frame2,text=">",bg='lawn green',command=b5).grid(row=15, column=5)

        Button(frame2,text=" X ",bg='red',command=frame2.destroy).grid(row=1, column=5,sticky='e')
        frame.destroy()

    Button(frame,text=" X ",bg='red',command=frame.destroy).grid(row=1, column=5,sticky='e')
    Button(frame,text=" > ",bg='lawn green',command=GoFlight).grid(row=3, column=5,padx=20,sticky='w')


def hotel():
    #General function that takes in string value of date and tells if it is valid or not
    #returns 0 is date entered is valid
    #returns 1 if date is invalid
    def validate_date(date_str):
        global extention_flag
        extention_flag =0
        #flag that holds return value
        validdate_flag = 0
        if(date_str.count('-')!= 2):
            validdate_flag = 1
        if(validdate_flag == 0):
            #Extracting date, month and year from check in date entered by user
            yeartemp,montemp,datetemp = date_str.split('-')

            #year validation: should be > current year and within 1 year of current year
            if(yeartemp.isdigit()):
                if(int(yeartemp)<2026):
                    validdate_flag = 1            
                if(int(yeartemp)>2024):
                    extention_flag=1
                    validdate_flag = 1            
            else:
                validdate_flag = 1
           
            #month validation: 1<=month<=12
            if(montemp.isdigit()):
                if(int(montemp)<1):
                    validdate_flag = 1            
                if(int(montemp)>12):
                    validdate_flag = 1            
            else:
                validdate_flag = 1
           
            #date validation: 1<=date<=31 for months jan,mar,may,july,aug,oct,dec
            #date validation: 1<=date<=30 for months sept,april,june,nov
            #date validation: 1<=date<=28 for months feb
            if(datetemp.isdigit()):
                if(int(datetemp)<1):
                    validdate_flag = 1
                if((int(montemp)== 1) or (int(montemp)== 3) or (int(montemp)== 5) or (int(montemp)== 7) or (int(montemp)== 8) or (int(montemp)== 10) or (int(montemp)== 12)):
                    if(int(datetemp)>31):
                        validdate_flag = 1
                if((int(montemp)== 4) or (int(montemp)== 6) or (int(montemp)== 9) or (int(montemp)== 11)):
                    if(int(datetemp)>30):
                        validdate_flag = 1
                if((int(montemp)== 2)):
                    if(int(datetemp)>28):
                        validdate_flag = 1
            else:
                validdate_flag = 1
        return validdate_flag

    #Displays final window after booking process is completed
    def final_window():
        def WindowExit():
            files_execution()
            main.destroy()
            finalwindow.destroy()

        def files_execution():
            global data
            #writing the data into the file
            fw=open("Reservation details","a")
            data=[full_name_of_primary_guest,phoneno,emailid,date1,date2,room_selection,paymode_selected,total]
            fw.write("\n")
            fw.write(str(data))
            fw.write("\n")
            fw.close()

        finalwindow =Toplevel(root)
        finalwindow.title("Acknowledgement Window")
        finalwindow.geometry("500x400")
        fwframe=LabelFrame(finalwindow,text="Acknowledgement ",padx=50,pady=50)
        fwframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        fvlabel1=Label(fwframe,text="Dear "+full_name_of_primary_guest+",",font=("Californian FB",16))
        fvlabel1.grid(row=0,column=0,pady=10)
        fvlabel2=Label(fwframe,text="Your booking at our hotel is confirmed. ",font=("Californian FB",16))
        fvlabel2.grid(row=1,column=0,pady=10)
        fvlabel3=Label(fwframe,text="We look forward to welcoming you soon. ",font=("Californian FB",16))
        fvlabel3.grid(row=2,column=0,pady=10)
        fvbutton = Button(fwframe,text ="Exit",borderwidth=10,fg='red',command = WindowExit)
        fvbutton.grid(row=3,column=0,pady=10)

    def hotel_report():
        with open("Reservation details","r") as f:
            data=f.read().split("\n")
            new=[]
            for i in data:
                if(i==''):
                    pass
                else:
                    new.append(i)
        print("new",new)
        
        final=[]
        for j in new:
            x=j.strip("[]").split(",")
            final.append(x)
        print("\n",final)
        
        end=[]
        for m in final:
            if(m[5]==" 'Executive Twin Room'"):
                end.append([m])
                with open('REPORT.txt', 'w') as p:
                        p.write(str(end))
        #newfile=open("REPORT","w")
        #newfile.write("DETAILS OF GUESTS WHO HAVE BOOKED THE MOST PREFERRED ROOM TYPE:EXECUTIVE TWIN ROOM")
        #newfile.write("\n")        
        #for m in final:
           # if(m[5]==" 'Executive Twin Room'"):
            #    newfile.write(str(m))
             #   newfile.write("\n")
        #newfile.close()

    #Displays Invoice window after computaion of final bill value    
    def invoice_window():
        def IWCmd():
            final_window()
            invoicewindow.destroy()
            hotel_report()
            
        invoicewindow = Toplevel(root)
        invoicewindow.title("Invoice")
        invoicewindow.geometry("600x700")
        ivframe=LabelFrame(invoicewindow,text="Invoice for " + full_name_of_primary_guest,padx=50,pady=50)
        ivframe.place(relx=0.5,rely=0.5,anchor=CENTER)
       
        ivlabel1=Label(ivframe,text="Number of rooms selected for stay :" + norooms,font=("Californian FB",16))
        ivlabel1.pack(pady=10)
        ivlabel2=Label(ivframe,text="Number of Guests :" + str(current_occupancy),font=("Californian FB",16))
        ivlabel1.pack(pady=10)
        ivlabel3=Label(ivframe,text="Check-in Date :" + date1,font=("Californian FB",16))
        ivlabel3.pack(pady=10)
        ivlabel4=Label(ivframe,text="Check-out Date :" + date2,font=("Californian FB",16))
        ivlabel4.pack(pady=10)
        ivlabel5=Label(ivframe,text="Room Category :" + room_selection,font=("Californian FB",16))
        ivlabel5.pack(pady=10)
        ivlabel6=Label(ivframe,text="Tariff per night per room : Rs." + str(selected_room_tarrif_per_night),font=("Californian FB",16))
        ivlabel6.pack(pady=10)
        ivlabel7=Label(ivframe,text="Payment Mode :" + paymode_selected,font=("Californian FB",16))
        ivlabel7.pack(pady=10)

        tariff_for_stay=int(norooms)* selected_room_tarrif_per_night*int(timeto_checkout.days)
        if(selected_room_tarrif_per_night>1000):
            gst=15
        else:
            gst=10
        taxes=(gst/100)*tariff_for_stay
        global total
        total=tariff_for_stay+taxes
       
        ivlabel8=Label(ivframe,text="Total tariff excluding taxes :" + str(tariff_for_stay),font=("Californian FB",16))
        ivlabel8.pack(pady=10)
        ivlabel9=Label(ivframe,text="Taxes @" + str(gst)+"% on tariff:"+str(taxes),font=("Californian FB",16))
        ivlabel9.pack(pady=10)
        ivlabel10=Label(ivframe,text="Final bill amount :" + str(total),font=("Californian FB",16))
        ivlabel10.pack(pady=10)
        ivbutton = Button(ivframe,text ="Accept",borderwidth=10,fg='red',command = IWCmd)
        ivbutton.pack(pady=10)
        
    #Function that accepts user inputs for payments
    def payment_window():
        def payment_select(e):
            global paymode_selected, room_tarrif_list, payment_mode_list
            paymode_selected = payment_mode.get()
        def PWCmd():
            invoice_window()
            paymentWindow.destroy()
        def PWCancel():
            paymentWindow.destroy()
            guest_details_window()
           
        room_tarrif_list=[("Executive Double Room",800),
                                 ("Executive Twin Room",900),
                                 ("Family Suite",1600),
                                 ("King Suite",1800)
                                 ]
        payment_mode_list=[
                                "Credit/Debit Card",
                                "Bank Transfer",
                                "UPI Payments",
                                "Pay On Arrival"
                                ]
        types_of_rooms = len(room_tarrif_list)
        
        global selected_room_tarrif_per_night
        #Unpacking room data from room_tarrif_list
        #room_label holds the type of room,tarrif_per_night holds tarrif of each room per night
        for i in range(types_of_rooms):
            room_label,tarrif_per_night=room_tarrif_list[i]
            if(room_label==room_selection):
                selected_room_tarrif_per_night = tarrif_per_night

        paymentWindow=Toplevel(root)
        paymentWindow.title("Payment Window")
        paymentWindow.geometry("900x650")
        pvframe=LabelFrame(paymentWindow,text="Payment Mode Selection: ",padx=50,pady=50)
        pvframe.place(relx=0.5,rely=0.5,anchor=CENTER)
       
        roomtype1=Label(pvframe,text="Room Selected for stay: ",font=("Californian FB",16))
        roomtype1.grid(row=0,column=0,padx=5,pady=10)
        roomtype2=Label(pvframe,text=room_selection,font=("Californian FB",16))
        roomtype2.grid(row=0,column=2,padx=5,pady=10)
        tarriflabel1 = Label(pvframe,text="Tariff per night: ",font=("Californian FB",16))
        tarriflabel1.grid(row=1,column=0,padx=5,pady=10)
        tarriflabel2 = Label(pvframe,text="Rs."+str(selected_room_tarrif_per_night),font=("Californian FB",16))
        tarriflabel2.grid(row=1,column=2,padx=5,pady=10)
        paylabel = Label(pvframe,text="Select mode of payment: ",font=("Californian FB",16))
        paylabel.grid(row=2,column=0,padx=5,pady=10)
       
        payment_mode = ttk.Combobox(pvframe,value=payment_mode_list)
        payment_mode.current(0)
        payment_mode.grid(row=2,column=2,padx=5,pady=10)
        payment_mode.bind("<<ComboboxSelected>>",payment_select)
           
        button2 = Button(pvframe,text ="View Invoice",borderwidth=10,fg='red',command =PWCmd )
        button2.grid(row=3,column=0,ipadx=10,ipady=10,pady=10)
        leave=Button(pvframe,text="Cancel",fg="red",command=PWCancel,borderwidth=10)
        leave.grid(row=3,column=2,ipadx=10,ipady=10,pady=10)
        
    #Function that validates the Guest details: Name, phone number and Email
    def guestvalidation_window():
        global phoneno, emailid
        def GVWCmd():
            payment_window()
            gvwindow.destroy()
        def GVWCancel():
            gvwindow.destroy()
            guest_details_window()
            
        gvwindow = Toplevel(root)
        gvwindow.title("Guest Details Status")
        gvwindow.geometry("600x500")
        gvframe=LabelFrame(gvwindow,text="Confirmation of Guest Personal Details: ",padx=50,pady=50)
        gvframe.place(relx=0.5,rely=0.5,anchor=CENTER)
       
        #flag that holds true if all validations have passed
        validation_flag = 0
       
        #Text validation for Guest first and last name
        #Name should be a non empty string with characters
        firstname = fnametxt.get()
        lengthfn = len(firstname)
        if (lengthfn>0):
            if(firstname.isalpha() == False):
                gvlabel1=Label(gvframe,text="First name should contain only character values",font=("Californian FB",16))
                gvlabel1.pack(pady=10)
                validation_flag = 1
        else:
            gvlabel1=Label(gvframe,text="First name should cannot be a non empty string",font=("Californian FB",16))
            gvlabel1.pack(pady=10)
            validation_flag = 1

        lastname = lnametxt.get()
        lengthln = len(lastname)
        if (lengthln>0):
            if(lastname.isalpha() == False):
                gvlabel2=Label(gvframe,text="Last name should contain only character values",font=("Californian FB",16))
                gvlabel2.pack(pady=10)
                validation_flag = 1
        else:
            gvlabel2=Label(gvframe,text="Last name should cannot be a non empty string",font=("Californian FB",16))
            gvlabel2.pack(pady=10)
            validation_flag = 1
        if (validation_flag == 0):
            global full_name_of_primary_guest
            full_name_of_primary_guest= name_prefix + " " + firstname + " " +lastname
            gvlabel1=Label(gvframe,text="Name of Guest : "+full_name_of_primary_guest,font=("Californian FB",16))
            gvlabel1.pack(pady=10)
           
        #Text validation for phone number of guest
        #Phone number should be non negative 10-digit integer values
        phoneno = phonetxt.get()
        if((phoneno.isalpha() == True) or (phoneno.isalnum() == True)):
            if(phoneno.isdigit() == False):
                gvlabel3=Label(gvframe,text="Phone number must be a numeric integer value",font=("Californian FB",16))
                gvlabel3.pack(pady=10)
                validation_flag = 1
            else:
                if(len(phoneno) != 10):
                    gvlabel3=Label(gvframe,text="Please enter a 10 digit mobile number",font=("Californian FB",16))
                    gvlabel3.pack(pady=10)
                    validation_flag = 1
        else:
            gvlabel3=Label(gvframe,text="Invalid data for Guest mobile number",font=("Californian FB",16))
            gvlabel3.pack(pady=10)
            validation_flag = 1
           
        if (validation_flag == 0):
            gvlabel2=Label(gvframe,text="Contact number : "+phoneno,font=("Californian FB",16))
            gvlabel2.pack(pady=10)

        #Text validation for phone number of guest
        #Email ID should contain at least @ and . symbols
        emailid = emailtxt.get()
        if(emailid.find('@') == -1):
            gvlabel4=Label(gvframe,text="Please enter a valid Email ID",font=("Californian FB",16))
            gvlabel4.pack(pady=10)
            validation_flag = 1
        elif(emailid.find('.') == -1):
            gvlabel4=Label(gvframe,text="Please enter a valid Email ID",font=("Californian FB",16))
            gvlabel4.pack(pady=10)
            validation_flag = 1
        if (validation_flag == 0):
            gvlabel3=Label(gvframe,text="Email ID : "+emailid,font=("Californian FB",16))
            gvlabel3.pack(pady=10)

        if(validation_flag == 0):
            frame=Frame(gvframe)
            frame.pack(pady=20)
            button4 = Button(frame,text ="Continue to Payment",borderwidth=10,fg='red',command = GVWCmd)
            button4.grid(row=0,column=0,ipadx=10,ipady=10,padx=10,pady=10)
            leave=Button(frame,text="Cancel",fg="red",command=GVWCancel,borderwidth=10)
            leave.grid(row=0,column=2,ipadx=10,ipady=10,padx=10,pady=10)
        else:
            button4=Button(gvframe,text="Return",fg="red",command=GVWCancel,borderwidth=10)
            button4.pack(pady=10)
            
    #Function that accepts Guest details: Name, phone number, email and address        
    def guest_details_window():
        def name_select(e):
            global name_prefix
            name_prefix = nametxt.get()
        def GDWCmd():
            guestvalidation_window()
            gdw.destroy()
        def GDWCancel():
            gdw.destroy()
            details_window()
       
        gdw=Toplevel(root)
        gdw.title("Guest Details Window")
        gdw.geometry("900x650")
        gevframe=LabelFrame(gdw,text="Enter Primary guest details below: ",padx=50,pady=50)
        gevframe.place(relx=0.5,rely=0.5,anchor=CENTER)
       
        gfullname=Label(gevframe,text="Enter full name of guest",font=("Californian FB",14))
        gfullname.grid(row=1,column=0,padx=5,pady=10)
        namelist=[
            "Mr.",
            "Mrs.",
            "Ms.",
            ]
        global nametxt
        nametxt = ttk.Combobox(gevframe,value=namelist)
        nametxt.current(0)
        nametxt.grid(row=2,column=0,padx=5,pady=10)
        nametxt.bind("<<ComboboxSelected>>",name_select)    
        global fnametxt
        fnametxt = Entry(gevframe,borderwidth=5)
        fnametxt.insert(0," ")
        fnametxt.grid(row=2,column=2,padx=5,pady=10)
        global lnametxt
        lnametxt = Entry(gevframe,borderwidth=5)
        lnametxt.insert(0," ")
        lnametxt.grid(row=2,column=4,padx=5,pady=13)
       
        phone=Label(gevframe,text="Enter contact number",font=("Californian FB",14))
        phone.grid(row=3,column=0,padx=5,pady=10)
        global phonetxt
        phonetxt = Entry(gevframe,borderwidth=5)
        phonetxt.insert(0,"1234567890")
        phonetxt.grid(row=3,column=2,padx=5,pady=10)
       
        email=Label(gevframe,text="Enter email",font=("Californian FB",14))
        email.grid(row=4,column=0,padx=5,pady=10)
        global emailtxt
        emailtxt = Entry(gevframe,borderwidth=5)
        emailtxt.insert(0,"userid@domain.com")
        emailtxt.grid(row=4,column=2,padx=5,pady=10)

        address=Label(gevframe,text="Enter full address of guest (Optional)",font=("Californian FB",14))
        address.grid(row=5,column=0,padx=5,pady=10)
        global addtxt1
        addtxt1 = Entry(gevframe,borderwidth=5)
        addtxt1.insert(0,"House number, Locality name")
        addtxt1.grid(row=6,column=0,padx=5,pady=10)
        global addtxt
        addtxt2 = Entry(gevframe,borderwidth=5)
        addtxt2.insert(0,"Area, City, State")
        addtxt2.grid(row=6,column=2,padx=5,pady=10)
        global addtxt3
        addtxt3 = Entry(gevframe,borderwidth=5)
        addtxt3.insert(0,"Pincode")
        addtxt3.grid(row=7,column=0,padx=5,pady=10)

        confirmbutton = Button(gevframe,text ="Confirm Booking",borderwidth=10,fg='red',command = GDWCmd)
        confirmbutton.grid(row=8,column=0,ipadx=10,ipady=10,pady=10)
        leave=Button(gevframe,text="Cancel",fg="red",command=GDWCancel,borderwidth=10)
        leave.grid(row=8,column=2,ipadx=10,ipady=10,pady=10)
        
    #Function to validate user inputs from Room availability window
    def availability_window():
        global current_occupancy, date1, date2, noadults, nochild, norooms
        def AWCmd():
            guest_details_window()
            avwindow.destroy()
        def AWCancel():
            avwindow.destroy()
            details_window()
            
        avwindow = Toplevel(root)
        avwindow.title("Room Availability Status")
        avwindow.geometry("800x600")
        avframe=LabelFrame(avwindow,text="Confirmation of Room Details: ",padx=50,pady=50)
        avframe.place(relx=0.5,rely=0.5,anchor=CENTER)
       
        #flag that holds true if all validations have passed
        validation_flag = 0
       
        #Text validation for number of rooms
        #No of rooms should be non negative integer values
        norooms = roomtxt.get()
        if ((norooms.isalpha() == True) or (norooms.isalnum() == True)):
            if(norooms.isdigit() == False):
                avlabel1=Label(avframe,text="Room entry must be a numeric integer value",font=("Californian FB",16))
                avlabel1.pack(pady=10)
                validation_flag = 1
            else:
                if (int(norooms)!= 0):                
                    if(int(norooms)>max_no_of_rooms_in_hotel):
                        avlabel1=Label(avframe,text="Room entry surpassses maximum rooms in the hotel",font=("Californian FB",16))
                        avlabel1.pack(pady=8)
                        validation_flag = 1
                    else:
                        avlabel1=Label(avframe,text="Room selected : "+norooms,font=("Californian FB",16))
                        avlabel1.pack(pady=8)
                else:
                    avlabel1=Label(avframe,text="Invalid data for room selection",font=("Californian FB",16))
                    avlabel1.pack(pady=8)
                    validation_flag = 1        
        else:
            avlabel1=Label(avframe,text="Invalid data for room selection",font=("Californian FB",16))
            avlabel1.pack(pady=8)
            validation_flag = 1

        #Text validation for number of adults
        noadults = adtxt.get()
        if(noadults.isdigit() == False):
            avlabel2=Label(avframe,text="No. of adults must be a numeric integer value",font=("Californian FB",16))
            avlabel2.pack(pady=8)
            validation_flag = 1
        nochild = chtxt.get()
        if(nochild.isdigit() == False):
            avlabel2=Label(avframe,text="No. of children must be a numeric integer value",font=("Californian FB",16))
            avlabel2.pack(pady=8)
            validation_flag = 1
        if(validation_flag == 0):
            if ((noadults.isalpha() == True) or (noadults.isalnum() == True)):
                current_occupancy=int(noadults)+int(nochild)
                max_occupancy=int(max_occupancy_per_room)*int(norooms)
                hotel_room_req=int(math.ceil(current_occupancy/int(max_occupancy_per_room)))
                if(current_occupancy > max_occupancy):
                    avlabel2=Label(avframe,text="No. of guests surpassses maximum allowed per room. Please increase number of rooms.",font=("Californian FB",16))
                    avlabel2.pack(pady=8)
                    validation_flag = 1
                else:
                    if(hotel_room_req<int(norooms)):
                        avlabel2=Label(avframe,text="You have selected more rooms than required for given occupancy",font=("Californian FB",16))
                        avlabel2.pack(pady=8)
                        validation_flag = 1                    
                    else:
                        avlabel2=Label(avframe,text="No. of guests : "+noadults+ " adults and "+nochild+" children",font=("Californian FB",16))
                        avlabel2.pack(pady=8)                
            else:
                if (int(noadults)<=0):
                    avlabel2=Label(avframe,text="Invalid data for number of adults",font=("Californian FB",16))
                    avlabel2.pack(pady=8)
                    validation_flag = 1                

        #Text validation for number of children
        if(validation_flag == 0):
            if ((nochild.isalpha() == True) or (nochild.isalnum() == True)):
                if(nochild.isdigit() == False):
                    avlabel3=Label(avframe,text="No. of children must be a numeric integer value",font=("Californian FB",16))
                    avlabel3.pack(pady=8)
                    validation_flag = 1
                elif (current_occupancy > max_occupancy):
                    avlabel3=Label(avframe,text="No. of guests surpassses maximum allowed per room. Please increase number of rooms.",font=("Californian FB",16))
                    avlabel3.pack(pady=8)
                    validation_flag = 1
            else:
                if(int(nochild)<=0):
                    avlabel3=Label(avframe,text="Invalid data for number of children",font=("Californian FB",16))
                    avlabel3.pack(pady=8)
                    validation_flag = 1

        #Validation for date with reference to current date
        if(validation_flag == 0):          
            date1=ckintxt.get()
            format="%Y-%m-%d"
            #Determining basic date validity for check in date
            ischeckin_valid_date=0
            ischeckin_valid_date = validate_date(date1)
            if(extention_flag==1):
                avlabel4=Label(avframe,text="We are not taking bookings for more than a year away",font=("Californian FB",16))
            date2=ckouttxt.get()
            #Determining basic date validity for check out date
            ischeckout_valid_date = 0
            ischeckout_valid_date = validate_date(date2)
           
            if (ischeckin_valid_date == 0):
                #Get today's date from the system
                tday=datetime.today()
                #Get the check in date from the user
                userckin=datetime.strptime(date1, format)
                #calculate the time delta between today and check in date
                timeto_checkin = userckin.date() - tday.date()
                if (timeto_checkin.days <1):
                    avlabel4=Label(avframe,text="Check In Date should be at least a day away",font=("Californian FB",16))
                    avlabel4.pack(pady=8)
                    validation_flag = 1
                else:
                    if(timeto_checkin.days>365):
                        avlabel4=Label(avframe,text="We are not taking bookings for more than a year away",font=("Californian FB",16))
                        avlabel4.pack(pady=8)
                        validation_flag = 1
                    else:
                        avlabel4=Label(avframe,text="Check In Date : "+ date1,font=("Californian FB",16))
                        avlabel4.pack(pady=8)        
               
            if (validation_flag == 0):
                if ((ischeckout_valid_date == 0) and (ischeckin_valid_date == 0)):
                    #Get the check out date from the user
                    userckout=datetime.strptime(date2, format)
                    #calculate the time delta between check in and check out date
                    global timeto_checkout
                    timeto_checkout = userckout.date() - userckin.date()

                    if (timeto_checkout.days <1):
                        avlabel5=Label(avframe,text="Minimum duration of stay should be 1 day",font=("Californian FB",16))
                        avlabel5.pack(pady=8)
                        validation_flag = 1
                    else:
                        if(timeto_checkout.days>30):
                            avlabel5=Label(avframe,text="Extented stays are not supported at our hotel",font=("Californian FB",16))
                            avlabel5.pack(pady=8)
                            validation_flag = 1
                        else:
                            avlabel5=Label(avframe,text="Check Out Date : "+ date2,font=("Californian FB",16))
                            avlabel5.pack(pady=8)
                            avlabel6=Label(avframe,text="No. of days left for check in : " +str(timeto_checkin.days),font=("Californian FB",16))
                            avlabel6.pack(pady=8)
                            avlabel7=Label(avframe,text="No. of days for stay : " +str(timeto_checkout.days),font=("Californian FB",16))
                            avlabel7.pack(pady=8)
                            avlabel8=Label(avframe,text="Type of room selected : " + room_selection,font=("Californian FB",16))
                            avlabel8.pack(pady=8)
            
           
        #Setting button in availability window based on validation
        if(validation_flag == 0):
            frame=Frame(avframe)
            frame.pack(pady=20)
            bkbutton=Button(frame,text="Proceed to Book",fg="red",borderwidth=10,command=AWCmd)
            bkbutton.grid(row=0,column=0,pady=15,padx=10)
            canbutton=Button(frame,text="Cancel",fg="red",borderwidth=10,command=AWCancel)
            canbutton.grid(row=0,column=2,pady=15,padx=10)
        else:
            returnbutton=Button(avframe,text="Return",fg="red",borderwidth=10,command=AWCancel)
            returnbutton.pack(pady=15,padx=10)

    #Function that accepts user inputs for room selection
    #Number of rooms, check in and check out dates, number of guests and room type
            
    def details_window():
        def room_select(e):
            global room_selection, room_list
            room_selection = room_type.get()
        def DWCmd():
            availability_window()
            availabiltyWindow.destroy()
            
        availabiltyWindow = Toplevel(root)
        availabiltyWindow.title("Room Selection window")
        availabiltyWindow.geometry("600x600")
        aevframe=LabelFrame(availabiltyWindow,text="Enter room details below: ",padx=50,pady=50)
        aevframe.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        roomlbl=Label(aevframe,text="Enter number of rooms",font=("Californian FB",16))
        roomlbl.grid(row=1, column=0,padx=5,pady=10)
        global roomtxt
        roomtxt = Entry(aevframe,borderwidth=5)
        roomtxt.insert(0,"1")
        roomtxt.grid(row=1,column=2,padx=5,pady=10)
       
        ckinlbl=Label(aevframe,text="Enter Check In Date",font=("Californian FB",16))
        ckinlbl.grid(row=2, column=0,padx=5,pady=10)
        global ckintxt
        ckintxt = Entry(aevframe,borderwidth=5)
        ckintxt.insert(0,date.today())
        ckintxt.grid(row=2,column=2,padx=5,pady=10)
       
        ckoutlbl=Label(aevframe,text="Enter Check Out Date",font=("Californian FB",16))
        ckoutlbl.grid(row=3, column=0,padx=5,pady=10)
        global ckouttxt
        ckouttxt = Entry(aevframe,borderwidth=5)
        ckouttxt.insert(0,date.today())
        ckouttxt.grid(row=3,column=2,padx=5,pady=10)

        adlbl=Label(aevframe,text="Enter Number of Adults",font=("Californian FB",16))
        adlbl.grid(row=4,column=0,padx=5,pady=10)
        global adtxt
        adtxt = Entry(aevframe,borderwidth=5)
        adtxt.insert(0,"1")
        adtxt.grid(row=4,column=2,padx=5,pady=10)

        chlbl=Label(aevframe,text="Enter Number of Children",font=("Californian FB",16))
        chlbl.grid(row=5, column=0,padx=5,pady=10)
        global chtxt
        chtxt = Entry(aevframe,borderwidth=5)
        chtxt.insert(0,"0")
        chtxt.grid(row=5,column=2,padx=5,pady=10)

        rooms=Label(aevframe,text="Enter type of room",font=("Californian FB",16))
        rooms.grid(row=6,column=0,padx=5,pady=10)
        roomlist=[
            "Executive Double Room",
            "Executive Twin Room",
            "Family Suite",
            "King Suite"
            ]
        
        global room_type
        room_type = ttk.Combobox(aevframe,value=roomlist)
        room_type.current(0)
        room_type.grid(row=6,column=2,padx=5)
        room_type.bind("<<ComboboxSelected>>",room_select)
       
        ckbutton = Button(aevframe,text ="Check Availabilty",borderwidth=10,fg='red',command =DWCmd )
        ckbutton.grid(row=7,column=0,ipadx=10,ipady=10,pady=10)
        leave=Button(aevframe,text="Cancel",fg="red",command=availabiltyWindow.destroy,borderwidth=10)
        leave.grid(row=7,column=2,ipadx=10,ipady=10,pady=10)
   
    def aboutmenu():
        aboutwindow = Toplevel(root)
        aboutwindow.title("About")
        aboutwindow.geometry("900x600")
        aboutframe=LabelFrame(aboutwindow,text="About Hotel Hillside Exotica ",padx=50,pady=50)
        aboutframe.place(relx=0.5,rely=0.5,anchor=CENTER)
               
        l1=Label(aboutframe,text="The Hotel Hillside Exotica is a haven of peace tucked away in the lap of nature,",font=("Lucida Handwriting",12))
        l1.grid(row=0,column=0,pady=3,padx=10)
        l2=Label(aboutframe,text="across many destinations.",font=("Lucida Handwriting",12))
        l2.grid(row=1,column=0,pady=3,padx=10)
        l3=Label(aboutframe,text="The stunning scenery from the rooms, dining areas and the lounges,",font=("Lucida Handwriting",12))
        l3.grid(row=4,column=0,pady=3,padx=10)
        l4=Label(aboutframe,text="the 360-degree views, gorgeous mountain treks and the fine dining",font=("Lucida Handwriting",12))
        l4.grid(row=5,column=0,pady=3,padx=10)
        l5=Label(aboutframe,text="take you away from the drudgery of city life to a world of tranquillity and privacy.",font=("Lucida Handwriting",12))
        l5.grid(row=6,column=0,pady=3,padx=10)
        l6=Label(aboutframe,text="Hotel Hillside Exotica has a character and charm unsurpassed...",font=("Lucida Handwriting",12))
        l6.grid(row=7,column=0,pady=3,padx=10)
        l7=Label(aboutframe,text="Heaven is indeed a place on earth.",font=("Lucida Handwriting",12))
        l7.grid(row=8,column=0,pady=3,padx=10)
        awb=Button(aboutframe,text="Back",borderwidth=10,fg="red",command=aboutwindow.destroy)
        awb.grid(row=12,column=0,pady=50,padx=10)
        
    def tariffmenu():
        rtwindow = Toplevel(root)
        rtwindow.title("Room Tariffs")
        rtwindow.geometry("800x500")
                           
        tframe=LabelFrame(rtwindow,text="Room tariffs and taxes applicable",padx=50,pady=50)
        tframe.place(relx=0.5,rely=0.5,anchor=CENTER)
        typelab=Label(tframe,text="ROOM CATEGORY :",font=("Lucida Handwriting",12))
        typelab.grid(row=0,column=0,pady=10)
        costlab=Label(tframe,text="ROOM TARIFF/NIGHT",font=("Lucida Handwriting",12))
        costlab.grid(row=0,column=2,pady=10)
        gstlab=Label(tframe,text="TAXES",font=("Lucida Handwriting",12))
        gstlab.grid(row=0,column=4,pady=10)
        lab1=Label(tframe,text="Executive Double Room",font=("Lucida Handwriting",12))
        lab1.grid(row=1,column=0,pady=10)
        lab2=Label(tframe,text="Rs."+str(800),font=("Lucida Handwriting",12))
        lab2.grid(row=1,column=2,pady=10)
        lab3=Label(tframe,text="10%",font=("Lucida Handwriting",12))
        lab3.grid(row=1,column=4,pady=10)
        lab4=Label(tframe,text="Executive Twin Room",font=("Lucida Handwriting",12))
        lab4.grid(row=2,column=0,pady=10)
        lab5=Label(tframe,text="Rs."+str(900),font=("Lucida Handwriting",12))
        lab5.grid(row=2,column=2,pady=10)
        lab6=Label(tframe,text="10%",font=("Lucida Handwriting",12))
        lab6.grid(row=2,column=4,pady=10)
        lab7=Label(tframe,text="Family Suite",font=("Lucida Handwriting",12))
        lab7.grid(row=3,column=0,pady=10)
        lab8=Label(tframe,text="Rs."+str(1600),font=("Lucida Handwriting",12))
        lab8.grid(row=3,column=2,pady=10)
        lab9=Label(tframe,text="15%",font=("Lucida Handwriting",12))
        lab9.grid(row=3,column=4,pady=10)
        lab10=Label(tframe,text="King Suite",font=("Lucida Handwriting",12))
        lab10.grid(row=4,column=0,pady=10)
        lab11=Label(tframe,text="Rs."+str(1800),font=("Lucida Handwriting",12))
        lab11.grid(row=4,column=2,pady=10)
        lab12=Label(tframe,text="15%",font=("Lucida Handwriting",12))
        lab12.grid(row=4,column=4,pady=10)

        rb=Button(tframe,text="Back",fg="red",borderwidth=10,command=rtwindow.destroy)
        rb.grid(row=6,column=1,pady=20)
        
    def servicesmenu():
        swindow = Toplevel(root)
        swindow.title("Services")
        swindow.geometry("650x450")
        sframe=LabelFrame(swindow,text="Services offered at the hotel: ",padx=50,pady=50)
        sframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        l1=Label(sframe,text="1. Wifi coverage",font=("Lucida Handwriting",12))
        l1.grid(row=0,column=0)
        l2=Label(sframe,text="2. Laundry",font=("Lucida Handwriting",12))
        l2.grid(row=1,column=0)
        l3=Label(sframe,text="3. Treks, nature walks, bird watching guides available",font=("Lucida Handwriting",12))
        l3.grid(row=2,column=0)
        l4=Label(sframe,text="4. Conference rooms and business centres",font=("Lucida Handwriting",12))
        l4.grid(row=3,column=0)
        l5=Label(sframe,text="5. Surface sanitization twice a day for common areas",font=("Lucida Handwriting",12))
        l5.grid(row=4,column=0)
        swb=Button(sframe,text="Back",borderwidth=10,fg="red",command=swindow.destroy)
        swb.grid(row=5,column=0,pady=50)
        
    def facilitiesmenu():
        fwindow = Toplevel(root)
        fwindow.title("Facilities")
        fwindow.geometry("650x500")
        fframe=LabelFrame(fwindow,text="Facilities offered at the hotel: ",padx=50,pady=50)
        fframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        l1=Label(fframe,text="1. Infinity heated pool",font=("Lucida Handwriting",12))
        l1.grid(row=0,column=0)
        l2=Label(fframe,text="2. Children's play area",font=("Lucida Handwriting",12))
        l2.grid(row=1,column=0)
        l3=Label(fframe,text="3. 24-hour coffee shop",font=("Lucida Handwriting",12))
        l3.grid(row=2,column=0)
        l4=Label(fframe,text="4. All-day fine dining restaurant",font=("Lucida Handwriting",12))
        l4.grid(row=3,column=0)
        l5=Label(fframe,text="5. Basketball and tennis courts",font=("Lucida Handwriting",12))
        l5.grid(row=4,column=0)
        l6=Label(fframe,text="6. Indoor games like pool, carrom, table tennis.",font=("Lucida Handwriting",12))
        l6.grid(row=5,column=0)
        swb=Button(fframe,text="Back",borderwidth=10,fg="red",command=fwindow.destroy)
        swb.grid(row=6,column=0,pady=50)
        
    def contactmenu():
        cwindow = Toplevel(root)
        cwindow.title("Contact")
        cwindow.geometry("600x500")
        cframe=LabelFrame(cwindow,text="You can reach us here: ",padx=55,pady=55)
        cframe.place(relx=0.5,rely=0.5,anchor=CENTER)
               
        add=Label(cframe,text="HO Address :",font=("Lucida Handwriting",12))
        add.grid(row=0,column=0,pady=10)
        address1=Label(cframe,text="UB City, Lavelle Road,",font=("Lucida Handwriting",12))
        address1.grid(row=0,column=1,pady=10)
        address2=Label(cframe,text="Bangalore, Karnataka 560075",font=("Lucida Handwriting",12))
        address2.grid(row=1,column=1,pady=10)
        phone=Label(cframe,text="Phone numbers :",font=("Lucida Handwriting",12))
        phone.grid(row=3,column=0,pady=10)
        ph1=Label(cframe,text="9845312345",font=("Lucida Handwriting",12))
        ph1.grid(row=3,column=1,pady=10)
        ph2=Label(cframe,text="9845412345",font=("Lucida Handwriting",12))
        ph2.grid(row=4,column=1,pady=10)
        email=Label(cframe,text="E-mail :",font=("Lucida Handwriting",12))
        email.grid(row=6,column=0,pady=10)
        eid=Label(cframe,text="info@hillsideexotica.com",font=("Lucida Handwriting",12))
        eid.grid(row=6,column=1,pady=10)
        cb=Button(cframe,text="Back",fg="red",borderwidth=10,command=cwindow.destroy)
        cb.grid(row=7,column=1,pady=10,padx=10)

    #Function for menu options
    def menu_window():           
        menuWindow = Toplevel(root)
        menuWindow.title("Menu Selection window")
        menuWindow.geometry("600x600")
        mevframe=LabelFrame(menuWindow,text="Select to view information",padx=100,pady=100)
        mevframe.place(relx=0.5,rely=0.5,anchor=CENTER)
       
        aboutbutton = Button(mevframe,text ="About",borderwidth=10,fg='black',command=aboutmenu)
        aboutbutton.grid(row=7,column=0,ipadx=10,ipady=10,pady=10)
        
        contactbutton=Button(mevframe,text="Contact",borderwidth=10,fg="black",command=contactmenu)
        contactbutton.grid(row=7,column=8,ipadx=10,ipady=10,pady=10)
       
        tariffbutton = Button(mevframe,text ="Tariff",borderwidth=10,fg='black',command=tariffmenu)
        tariffbutton.grid(row=7,column=16,ipadx=10,ipady=10,pady=10)

        servicesbutton=Button(mevframe,text="Services",borderwidth=10,fg="black",command=servicesmenu)
        servicesbutton.grid(row=8,column=0,ipadx=10,ipady=10,pady=10)

        facilitiesbutton=Button(mevframe,text="Facilities",borderwidth=10,fg="black",command=facilitiesmenu)
        facilitiesbutton.grid(row=8,column=8,ipadx=10,ipady=10,pady=10)

        leavebutton=Button(mevframe,text="Exit",fg="black",command=menuWindow.destroy,borderwidth=10)
        leavebutton.grid(row=8,column=16,ipadx=10,ipady=10,pady=10)        
        
    global max_no_of_rooms_in_hotel, max_adults_per_room, child_per_room, max_occupancy_per_room
    max_no_of_rooms_in_hotel=100
    max_adults_per_room=3
    child_per_room=2
    max_occupancy_per_room=max_adults_per_room + child_per_room

    main=Frame(main_label)
    main.place(x=5,y=105)
    global bg
    bg = ImageTk.PhotoImage(file = "main3.jpeg")
    my_canvas=Canvas(main,width=1525,height=650)
    my_canvas.pack(fill="both",expand=True)

    my_canvas.create_image(0,0,image=bg,anchor="nw")
    my_canvas.create_text(700,75,text="HOTEL HILLSIDE EXOTICA",fill="black",font=("Lucida Handwriting",26))
    my_canvas.create_text(700,150,text="Rediscover...Revitalize...Rejuvenate!",fill="black",font=("Lucida Handwriting",20))

    bookingbutton=Button(main,text ="Make a Booking",borderwidth=10,fg='black',command = details_window)
    exitbutton=Button(main,text="Exit",fg="black",command=main.destroy,borderwidth=10)
    menubutton=Button(main,text ="Menu",borderwidth=10,fg='black',command = menu_window)

    b1window = my_canvas.create_window(700,500,window=bookingbutton)
    b2window = my_canvas.create_window(900,500,window=exitbutton)
    b3window = my_canvas.create_window(500,500,window=menubutton)



def bill():
    frame3 = Frame(main_label, bd=2, bg='white',highlightbackground="white", highlightthickness=2,relief=SOLID, padx=10, pady=10)
    frame3.place(x=5,y=105)
    Label(frame3, text="REPORT:",bg='lightgrey', font=('Courier 20 bold')).grid(row=1, column=0)
    
    Label(frame3, text="The Total Number of Seats Occupied",bg='lightgrey', font=('Courier 16')).grid(row=2, column=0)
    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(frame3, column=("Flight Name", "Seats"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="FName")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Seats")
    with open("rec.txt",'r')as bi:
        list2 =bi.read()
        dat=list(eval(list2))
    for i in dat:
        tree.insert('', 'end', text="1", values=(i[0],i[1]))
    tree.grid(row=3,column=0)
    Label(frame3, text="Details of Guests with Most Preferred Room Type:Executive Twin Room",bg='lightgrey', font=('Courier 16')).grid(row=4, column=0)
    tr = ttk.Treeview(frame3, column=("Name", "Ph No","Gmail","Payment Methord","Cost"), show='headings', height=5)
    tr.heading("# 1", text="Name",anchor=CENTER)
    tr.heading("# 2", text="Ph No", anchor=CENTER)
    tr.heading("# 3", text="Gmail", anchor=CENTER)
    tr.heading("# 4", text="Payment Methord", anchor=CENTER)
    tr.heading("# 5", text="Cost",anchor=CENTER)
    
    with open("REPORT.txt",'r')as bo:
        list3 =bo.read()
        dat=list(eval(list3))
    for i in dat:
        for j in i:
            tr.insert('', 'end', text="1", values=(j[0],j[1],j[2],j[6],j[7]))
    tr.grid(row=5,column=0)

    
    Button(frame3,text=" X ",bg='red',command=frame3.destroy).grid(row=0, column=2,sticky='e')

       
#Creating a button
button1=Button(top_frame, text = "Home",font=("Courier New", 20),borderwidth=0,bg="black",fg="white").grid(row=1,column=2,padx=10)
button2=Button(top_frame, text = "Flight",font=("Courier New", 20),borderwidth=0,bg="black",fg="white",command=flight).grid(row=1,column=3,padx=10)
button3=Button(top_frame, text = "Hotel",font=("Courier New", 20),borderwidth=0,bg="black",fg="white",command=hotel).grid(row=1,column=4,padx=10)
button5=Button(top_frame, text = "Report",font=("Courier New", 20),borderwidth=0,bg="black",fg="white",command=bill).grid(row=1,column=6,padx=10)
button6=Button(top_frame, text = "Login",font=("Courier New", 20),borderwidth=0,bg="black",fg="white",command=LOG).grid(row=1,column=7,padx=10)


root.mainloop()
