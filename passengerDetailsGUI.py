from tkinter import *
from tkinter import messagebox as ms
from reservationGUI import *
import sqlite3


#main Class
class PassengerDetailsGUI:
    def __init__(self):
        # Window
        #self.master = master
        #.configure(background = "#a1dbcd")
            # Some Usefull variables
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.email = StringVar()
        self.dob = StringVar()
        self.phone = StringVar()
        self.address = StringVar()
        self.cardnumber = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.zip = StringVar()
        self.country = StringVar()
        self.password = StringVar()
        self.image04 = PhotoImage(file='09.png', height=95, width=95)
        self.image02 = PhotoImage(file='10.png', height=30, width=120)
        self.image03 = PhotoImage(file='04.png', height=500, width=550)
        #Create Widgets
        self.widgets()


    def submitDetails(self):
        #Establish Connection
        with sqlite3.connect('airplanereservation.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT email FROM passenger WHERE email = ?')
        c.execute(find_user,[(self.email.get())])
        if c.fetchone():
            ms.showerror('Error!','Username taken.')
        elif len(self.email.get()) == 0:
            ms.showinfo("Warning!","User Name Required")
        elif len(self.firstname.get()) == 0:
            ms.showinfo("Warning!", "First Name Required")
        elif len(self.lastname.get()) == 0:
            ms.showinfo("Warning!", "Last Name Required")
        elif len(self.password.get()) == 0:
            ms.showinfo("Warning!", "Password Required")    
        else:
            insert = ('INSERT INTO passenger VALUES(?,?,?,?,?,?,?,?,?,?,?,?)')
            c.execute(insert,[(self.firstname.get()),(self.lastname.get()),(self.dob.get()),(self.email.get()),(self.phone.get()),(self.address.get()),(self.cardnumber.get()),(self.city.get()),(self.state.get()),(self.zip.get()),(self.country.get()),(self.password.get())])
            db.commit()
            ms.showinfo(message = "User Created")
            self.redirectToReservation()
        #if len(self.firstname.get()) == 0:
         #    ms.showinfo("Warning!", "Fields are empty! * fields can't be empty")
        #else:
                # do_something()
            #db.commit()
            #ms.showinfo(message = "User Created")
            #self.redirectToReservation()

        #Frame Packing Methords
    def redirectToReservation(self):
        self.head.forget()
        self.logf.forget()
        self.main.forget()
        ReservationGUI()


    #Draw Widgets

    def widgets(self):
        self.main=Frame(bg="#062428")

        self.left = Frame(self.main, bg="#062428")
        self.right = Frame(self.main, bg="#062428")
        self.left.pack(side=LEFT, fill=BOTH)
        self.right.pack(side=RIGHT, fill=BOTH)

        self.leftsub = Label(self.left, image=self.image03, pady=30, padx=20, bg="#062428", fg="#ffffff")
        self.leftsub.pack(side=LEFT,padx=85)





        self.top = Frame(self.right,padx =5,pady = 10, bg="#062428")
        self.top.pack(side=TOP,fill=BOTH,pady=10)
        self.top1 = Label(self.top, text = '', bg="#062428",fg="#ffffff" )
        self.top1.grid(row=0,column=0,sticky=W)
        self.head = Label(self.top1, text = 'Passenger Details',font = ('Blue Vinyl ',42,'bold italic'), bg="#062428",fg="#ffffff" )
        self.head1 = Label( self.top1, image=self.image04, pady=10, padx=20,bg="#062428", fg="#ffffff")
        self.head1.pack(side=RIGHT,fill=BOTH)
        self.head.pack(side=RIGHT, padx=20,fill=BOTH)


        self.logf = Frame(self.right,padx =35,pady = 16, bg="#062428")
        Label(self.logf,text = ' First Name* : ',font = ('',19),pady=4,padx=10, bg="#062428",fg="#ffffff").grid(row=0,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.firstname,font = ('',15)).grid(row=0,column=2,  sticky = E)
        Label(self.logf,text = ' Last Name* : ',font = ('',19),pady=4,padx=10, bg="#062428",fg="#ffffff").grid(row=1,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.lastname,  font = ('',15)).grid(row=1,column=2,  sticky = E)
        Label(self.logf,text = ' Date of Birth : ',font = ('',19),pady=4,padx=10, bg="#062428",fg="#ffffff").grid(row=2,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.dob,  font = ('',15)).grid(row=2,column=2,  sticky = E)
        Label(self.logf,text = ' Username / Email* : ',font = ('',19),pady=4,padx=10, bg="#062428",fg="#ffffff").grid(row=3,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.email,  font = ('',15)).grid(row=3,column=2,  sticky = E)
        Label(self.logf,text = ' Phone number : ',font = ('',19),pady=4,padx=10, bg="#062428",fg="#ffffff").grid(row=4,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.phone,  font = ('',15)).grid(row=4,column=2,  sticky = E)
        Label(self.logf,text = ' Address : ',font = ('',19),pady=4,padx=10,bg="#062428",fg="#ffffff").grid(row=5,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.address,  font = ('',15)).grid(row=5,column=2,  sticky = E)
        Label(self.logf,text = ' Card number : ',font = ('',19),pady=4,padx=10,bg="#062428",fg="#ffffff").grid(row=6,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.cardnumber,  font = ('',15)).grid(row=6,column=2,  sticky = E)
        Label(self.logf,text = ' City : ',font = ('',19),pady=4,padx=10,bg="#062428",fg="#ffffff").grid(row=7,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.city,  font = ('',15)).grid(row=7,column=2,  sticky = E)
        Label(self.logf,text = ' State : ',font = ('',19),pady=4,padx=10,bg="#062428",fg="#ffffff").grid(row=8,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.state,  font = ('',15)).grid(row=8,column=2,  sticky = E)
        Label(self.logf,text = ' ZIP : ',font = ('',19),pady=4,padx=10,bg="#062428",fg="#ffffff").grid(row=9,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.zip,  font = ('',15)).grid(row=9,column=2,  sticky = E)
        Label(self.logf,text = ' Country : ',font = ('',19),pady=4,padx=10,bg="#062428",fg="#ffffff").grid(row=10,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.country,  font = ('',15)).grid(row=10,column=2,  sticky = E)
        Label(self.logf,text = ' Password* : ',font = ('',19),pady=4,padx=10,bg="#062428",fg="#ffffff").grid(row=11,column=0, sticky = W,ipadx=14)
        Entry(self.logf,textvariable = self.password,  font = ('',15),show = '*').grid(row=11,column=2,  sticky = E)
        Button(self.logf,image=self.image02,bd = 3 ,padx=10,pady=10,command =self.submitDetails).grid(row=12,columnspan=3,pady=25)
        Label(self.logf, text='  ', font=('', 100), pady=4, padx=10, bg="#062428", fg="#ffffff").grid(row=13,rowspan=15,column=0,sticky=W)
        self.logf.pack(fill=BOTH)

        self.main.pack(fill=BOTH)



if __name__ == '__main__':
    #Create Object
    #and setup window
    root = Tk()
    root.title('Passenger details')
    #root.geometry('1366x768')
    root.state("zoomed")
    PassengerDetailsGUI()
    root.mainloop()
