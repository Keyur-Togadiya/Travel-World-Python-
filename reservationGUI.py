from tkinter import *
from tkinter import messagebox as ms
from reservationGUI import *
#from exp import *
import sqlite3


#main Class
class ReservationGUI:
    def __init__(self):
        # Window 
        #self.master = master
        #.configure(bg="#062428",fg="#ffffff")
            # Some Usefull variables
        #Create Widgets
        self.seats = StringVar()
        self.var_1 = StringVar()
        self.var_2 = StringVar()
        self.var = StringVar()
        self.flightID = StringVar()
        self.planeID = StringVar()
        self.email = StringVar()
        self.dogoing = StringVar()
        self.doreturning = StringVar()
        self.image05 = PhotoImage(file='02.png', height=65, width=65)
        self.image06 = PhotoImage(file='03.png', height=30, width=120)
        self.image07 = PhotoImage(file='05.png', height=40, width=40)
        self.image08 = PhotoImage(file='06.png', height=40, width=40)
        self.image09 = PhotoImage(file='11.png', height=400, width=518)
        self.image10 = PhotoImage(file='10.png', height=30, width=120)
        self.image11 = PhotoImage(file='03.png', height=500, width=600)
        self.image12 = PhotoImage(file='12.png', height=125, width=125)
        self.image16 = PhotoImage(file='16.png', height=75, width=75)
        self.image18 = PhotoImage(file='18.png', height=270, width=452)
        self.widgets()

    def reserveseats(self):
         self.redirectToexp()

    def redirectToexp(self):
        self.head.forget()
        self.logf.forget()
        self.main.forget()
        self.widgets1()
        
    def reserveDetails(self):
        # Establish Connection
        with sqlite3.connect('airplanereservation.db') as db:
            c = db.cursor()

        # Find if Existing username and flight id exist if any take proper action
        find_useremail = ('SELECT email FROM passenger WHERE email = ?')
        find_userflightid = ('SELECT flightID FROM flight WHERE flightID = ?')
        cursor = c.execute(find_useremail, [(self.email.get())])
        cursor = c.execute(find_userflightid, [(self.flightID.get())])
        if c.fetchall():
            insert = ('INSERT INTO reservation VALUES(?,?,?,?)')
            c.execute(insert,
                      [(self.flightID.get()), (self.email.get()), (self.dogoing.get()), (self.doreturning.get())])
            db.commit()
            ms.showinfo(message="Found! Details are as follows")
            # ms.showerror('Error!','Username / Flight ID not Found.')
        else:
            ms.showerror('Error!', 'Username / Flight ID not Found.')
            # insert = ('INSERT INTO reservation VALUES(?,?,?,?)')
            # c.execute(insert,[(self.flightID.get()),(self.email.get()),(self.dogoing.get()),(self.doreturning.get())])
            # db.commit()
            # ms.showinfo(message = "Found! Details are as follows")
        
        print("*** THESE ARE THE DEATAILS OF ALL OTHER PASSENGER WHO HAVE RESERVED THEIR SEAT ***")
        final_seat = ('SELECT * FROM reservation')
        cursor = c.execute(final_seat)
        row = c.fetchall()
        #ms.showerror('Note',str(row))
        print(row)

        
        check_plane = ('SELECT * FROM airplane WHERE planeID LIKE ?')
        cursor = c.execute(check_plane, [(self.planeID.get())])
        all_rows = c.fetchall()
        print("*** THESE ARE THE AVAILABLE FLIGHT TO YOUR DESTINATION ***")
        print(all_rows)

    def widgets1(self):
        self.main = Frame(bg="#062428")
        self.main.pack(fill=BOTH, side=TOP)
        self.f = Frame(self.main, height=768, width=683, bg="#062428")
        self.f1 = Frame(self.main, height=768, width=683, bg="#062428")
        self.f.propagate(0)
        self.f.pack(fill=BOTH, side=LEFT)
        self.f1.pack(fill=BOTH, side=RIGHT)

        self.top = Label(self.f, text=" ", font=('Helvetica', 30, 'bold italic'), pady=6, bg="#062428", fg="#ffffff")
        self.top.pack(fill=BOTH, side=TOP)
        self.label1 = Label(self.f, text=" ", font=('Helvetica', 5, 'bold italic'), pady=6, bg="#062428", fg="#ffffff")
        self.label1.pack(fill=BOTH, side=TOP)
        self.logz = Frame(self.label1, bg="#062428")
        self.logz.pack(side=TOP)
        self.head = Frame(self.logz, bg="#062428")
        self.head.pack(side=TOP)
        self.head12 = Label(self.head, image=self.image16, bg="#062428",fg="#ffffff")
        self.head12.pack(side=LEFT)
        self.head2 = Label(self.head, text='Seat  Reservation', font=('Coda Regular', 45, 'italic'), bg="#062428",fg="#ffffff")
        self.head2.pack(side=LEFT, padx=10)


        self.logf = Frame(self.logz, padx=20, pady=45, bg="#062428")
        self.logf.pack(fill=BOTH, side=TOP)
        self.logf.propagate(0)
        self.l1 = Label(self.logf, text='Flight ID : ', font=('Coda Regular', 15, 'italic'), bg="#062428",fg="#ffffff").grid(row=0, column=0, pady=12, padx=3, sticky=W)
        self.val1 = StringVar()
        self.e1 = Entry(self.logf, textvariable=self.flightID, width=18, font=('Coda Regular', 12, 'italic')).grid(row=0, column=2, pady=12, padx=3, sticky=W)

        self.l2 = Label(self.logf, text='Plane ID : ', font=('Coda Regular', 15, 'italic'), bg="#062428", fg="#ffffff").grid(row=1, column=0, pady=12, padx=3, sticky=W)
        self.e2 = Entry(self.logf, textvariable=self.planeID, width=18, font=('Coda Regular', 12, 'italic')).grid(row=1, column=2, pady=12, padx=3, sticky=W)

        self.l3 = Label(self.logf, text='Username / Email : ', font=('Coda Regular', 15, 'italic'), bg="#062428", fg="#ffffff").grid(row=2, column=0, pady=12, padx=3, sticky=W)
        self.e3 = Entry(self.logf, textvariable=self.email, width=18, font=('Coda Regular', 12, 'italic')).grid(row=2, column=2, pady=12,padx=3, sticky=W)

        self.l4 = Label(self.logf, text='Date Of Journey : ', font=('Coda Regular', 15, 'italic'), bg="#062428", fg="#ffffff").grid(row=3, column=0, pady=12, padx=3, sticky=W)
        self.e4 = Entry(self.logf, textvariable=self.dogoing, width=18, font=('Coda Regular', 12, 'italic')).grid(row=3,column=2,  pady=12,  padx=3, sticky=W)

        self.l5 = Label(self.logf, text='Return Date Of Journey : ', font=('Coda Regular', 15, 'italic'), bg="#062428",fg="#ffffff").grid(row=4, column=0, pady=12, padx=3, sticky=W)
        self.e5 = Entry(self.logf, textvariable=self.doreturning, width=18, font=('Coda Regular', 12, 'italic')).grid(row=4, column=2, pady=12, padx=3, sticky=W)
        self.val1 = StringVar()
        self.b1 = Button(self.logf, text="  Submit  ", font=('Coda Regular', 12, 'bold italic'), command=self.reserveDetails).grid(row=5, columnspan=1, pady=29, padx=5)
        self.b2 = Button(self.logf, text="  Print  ", font=('Coda Regular', 12, 'bold italic'),command=self.display).grid(row=5, column=2, columnspan=1, pady=29, padx=5)

        self.ra = Label(self.f1, text=' ', font=('Coda Regular', 65, 'italic'), pady=35, padx=20, bg="#062428", fg="#ffffff")
        self.ra.pack(side=TOP)

        self.rl1 = Label(self.ra, text=' ', font=('Coda Regular', 65, 'italic'), pady=35, padx=20, bg="#062428",fg="#ffffff")
        self.rl1.pack(side=TOP)

        self.rl2 = Label(self.ra, image=self.image11, pady=40, padx=20, bg="#062428", fg="#ffffff")
        self.rl2.pack(side=LEFT, padx=20, pady=20)

        self.head2 = Label(self.main, text=' ', font=('Helvetica', 1000, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head2.pack(fill=BOTH, side=BOTTOM)

    def display(self):
        self.ra.forget()

        self.ra = Label(self.f1, text=' ', font=('Coda Regular', 10, 'italic'), bg="#062428", fg="#ffffff")
        self.ra.pack(side=TOP)
        self.rl1 = Label(self.ra, text=' ', font=('Coda Regular', 10, 'italic'), bg="#062428", fg="#ffffff")
        self.rl1.pack(side=TOP)
        self.f12 = Frame(self.ra, bg="#062428")
        self.f12.pack(fill=BOTH, side=LEFT)

        self.a1 = Label(self.f12, text=" ", bg="#062428", fg="#ffffff")
        self.a1.pack(side=LEFT)
        self.r = Label(self.a1, text=" ", bg="#062428", fg="#ffffff")
        self.r.pack(side=LEFT, padx=2, pady=5,ipady=5)
        self.rl2 = Label(self.r, image=self.image12, bg="#062428", fg="#ffffff")
        self.rl2.grid(row=0, column=0, pady=10)
        self.rl3 = Label(self.r, text='  Ticket  Detail', font=('Coda Regular', 45, 'italic'), bg="#062428", fg="#ffffff")
        self.rl3.grid(row=0, column=0, pady=10)
        self.rl3 = Label(self.r, text='        ', font=('Coda Regular', 35, 'bold italic'), bg="#062428", fg="#ffffff")
        self.rl3.grid(row=0, column=1, pady=10)

        self.l7 = Label(self.r, text='Flight ID  :  ' + self.flightID.get(), font=('Coda Regular', 15, 'italic'), bg="#062428", fg="#ffffff").grid(row=1, column=0, pady=12, padx=3, sticky=W)
        self.l8 = Label(self.r, text='Plane ID  :  ' + self.planeID.get(), font=('Coda Regular', 15, 'italic'), bg="#062428", fg="#ffffff").grid(row=2, column=0, pady=12, padx=3, sticky=W)
        self.l9 = Label(self.r, text='Username / Email  :  ' + self.email.get(), font=('Coda Regular', 15, 'italic'), bg="#062428", fg="#ffffff").grid(row=3, column=0, pady=12, padx=3, sticky=W)
        self.l10 = Label(self.r, text='Date Of Journey  :  ' + self.dogoing.get(), font=('Coda Regular', 15, 'italic'),bg="#062428",fg="#ffffff").grid(row=4, column=0, pady=12, padx=3, sticky=W)
        self.l11 = Label(self.r, text='Return Date Of Journey  :  ' + self.doreturning.get(),font=('Coda Regular', 15, 'italic'), bg="#062428",fg="#ffffff").grid(row=5, column=0, pady=12, padx=3, sticky=W)
        self.b11 = Button(self.r, text="  OK  ", font=('Coda Regular', 12, 'bold italic'), command=self.next).grid(row=6, columnspan=2, pady=25, padx=5)

    def next(self):
        self.main.forget()
        #  self.root = Frame(bg="#062428")
        self.f2 = Label(bg="#062428", width=1366, height=768)
        self.f2.pack(fill=BOTH)

        # image1 = PhotoImage(file='11.png', height=200, width=600)
        self.head0 = Label(self.f2, text=' ', font=('Helvetica', 110, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head0.pack(fill=BOTH, side=TOP)

        self.head1 = Label(self.f2, image=self.image09, bg="#062428", fg="#ffffff")
        self.head1.pack(fill=BOTH)
        self.head2 = Label(self.f2, text=' ', font=('Helvetica', 1000, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head2.pack(fill=BOTH, side=BOTTOM)
        self.f2.after(4000, lambda: self.f2.destroy())
        self.l100 = Label(image=self.image18,font=('Coda Regular', 50, 'bold italic'), bg="#062428", fg="#ffffff")
        self.l100.pack(pady=200,fill=BOTH)
       



    def checkAndRegister(self):
        #Establish Connection
        with sqlite3.connect('airplanereservation.db') as db:
            c = db.cursor()
        print('----------Details Before Check----------')
        check_flight = ('SELECT * FROM flight WHERE origin LIKE ? and destination LIKE ?')
        cursor = c.execute(check_flight,[(self.var_1.get()),(self.var_2.get())])
        all_rows = c.fetchall()
        print(all_rows)

        
        #Find user If there is any take proper action
        check_seats = ('SELECT seatleft FROM flight WHERE origin LIKE ? and destination LIKE ?')
        cursor = c.execute(check_seats,[(self.var_1.get()),(self.var_2.get())])
        for row in cursor:
                seatsleft = int(row[0]) - int(self.seats.get())

        if seatsleft >= 0:
            update = ('UPDATE flight SET seatleft = ? WHERE origin LIKE ? and destination LIKE ?')
            c.execute(update,[(seatsleft),(self.var_1.get()),(self.var_2.get())])
            db.commit()
            ms.showinfo(message = "Seats left = " + str(seatsleft))
        else:
            ms.showerror('Error',message = "flight / seats unavailable")
    #Frame Packing Methords

        print('----------Details After Check----------')
        check_flight = ('SELECT * FROM flight WHERE origin LIKE ? and destination LIKE ?')
        cursor = c.execute(check_flight,[(self.var_1.get()),(self.var_2.get())])
        all_rows = c.fetchall()
        print(all_rows)
        print('origin , destination , departure, arrival, seat left, price, type, planeid , flightid')
        ms.showinfo('INFO',message = 'PLEASE NOTE THE  "FLIGHT ID"  FOR FURTHER REFERENCE')
        ms.showinfo('INFO',message = 'PLEASE NOTE THE  "PLANE ID"  FOR FURTHER REFERENCE')
        ms.showinfo('INFO',message = 'PLEASE NOTE THE  " *** ALL DETAILS ARE DISPLAYED ON PROMPT *** "')
        db.close()
        

    #Draw Widgets
    def widgets(self):
        self.main = Frame( bg="#062428")
        self.main.pack(fill=BOTH,side=TOP)

        self.top = Label(self.main,text=" ", font=('Helvetica', 25, 'bold italic'), pady=30, padx=20, bg="#062428", fg="#ffffff")
        self.top.pack(fill=BOTH,side=TOP)

        self.label1 = Label(self.main,text=" ", font=('Helvetica', 5,'bold italic'), pady=10, padx=20, bg="#062428", fg="#ffffff")
        self.label1.pack(fill=BOTH,side=TOP)

        self.logz = Frame(self.label1,padx=10, pady=10, bg="#062428")
        self.logz.pack(side=TOP)

        self.head = Label(self.logz,text = 'Reservation Details',font = ('comic sans MS',40,'bold italic'), bg="#062428",fg="#ffffff")

        self.head1 = Label(self.logz, image=self.image05, font=('Helvetica', 30, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head1.pack(side=LEFT)
        self.head.pack(side=LEFT, padx=8)
        self.logz.pack(side=TOP)


        self.logf = Frame(self.label1,padx =10,pady = 20,bg="#062428")
        self.logf.columnconfigure(0, weight = 1)
        self.logf.rowconfigure(0, weight = 1)
        self.logf.pack(pady = 8, padx = 20)

        self.op1 = Label(self.logf,text=" ", font=('Helvetica', 20, 'bold italic'), pady=30, padx=20, bg="#062428", fg="#ffffff")
        self.op1.grid(row = 0, column = 1,padx=2)
        self.op2 = Label(self.logf,text=" ", font=('Helvetica', 20, 'bold italic'), pady=30, padx=20, bg="#062428", fg="#ffffff")
        self.op2.grid(row = 0, column = 3,padx=55)

        self.head2 = Label(self.op1, image=self.image07, pady=30, padx=30, bg="#062428", fg="#ffffff")
        self.head2.pack(side=LEFT, ipadx=5, ipady=5)
        self.head2 = Label(self.op2, image=self.image08, pady=30, padx=30, bg="#062428", fg="#ffffff")
        self.head2.pack(side=LEFT, ipadx=5, ipady=5)

        choices = {
            'Mumbai',
            'Delhi',
            'Chennai',
            'Goa',
            'Hyderabad'
        }
        option_1 = OptionMenu(self.op1, self.var_1, *choices)
        self.var_1.set('    Origin    ')
        option_1.pack(side=LEFT,padx=10)
        option_1.config(font = ('comic sans MS',12,'bold italic'), bg="#062428", fg="#ffffff", width=25)
        option_1['menu'].config(font=('comic sans MS', 12, 'bold italic'), bg="#062428", fg="#ffffff")
        choices = {
            'Mumbai',
            'Delhi',
            'Chennai',
            'Goa',
            'Hyderabad'
        }

        option_2 = OptionMenu(self.op2, self.var_2, *choices)
        self.var_2.set(' Destination ')
        option_2.pack(side=LEFT,padx=10)
        option_2.config(font=('comic sans MS', 12, 'bold italic'),bg="#062428", fg="#ffffff",  width=25)
        option_2['menu'].config(font=('comic sans MS', 12, 'bold italic'), bg="#062428", fg="#ffffff")

        Label(self.logf, text=" Number of Seats : ", font = ('comic sans MS',20,'bold italic'),pady = 20, bg="#062428",fg="#ffffff").grid(row = 2, column = 1)
        self.var = StringVar()

        # 
        seats_ent = Entry(self.logf, textvariable = self.seats, width = 55).grid(column= 3, row = 2, ipadx=0,ipady=5)


        Button(self.logf, text="Submit",font = ('comic sans MS',10,'bold italic'), command=self.checkAndRegister).grid(row = 3, column = 1,padx = 1, pady=25,ipadx = 15, ipady=1 )
        Button(self.logf, text="Continue",font = ('comic sans MS',10,'bold italic'),command=self.redirectToexp ).grid(row=3, column=3, padx=0, pady=25,ipadx = 15, ipady=1)

        self.head2 = Label(self.main, text=' ', font=('Helvetica', 1000, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head2.pack(fill=BOTH, side=BOTTOM)

        self.logf.pack()

        
    def change_Seats(*args):
        seats_ = choices[self.var.get()]
        Seat.set(Seats_)        
         

if __name__ == '__main__':
    #Create Object
    #and setup window
    root = Tk()
    root.title('Reservation details')
    root.state("zoomed")
    #root.geometry('1000x750')
    root.configure(bg="#062428")
    ReservationGUI()
    root.mainloop()
