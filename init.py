from tkinter import *
from tkinter import messagebox as ms
from passengerDetailsGUI import *
from reservationGUI import *
import sqlite3



#main Class
class main:
    def __init__(self,master):
        # Window 
        self.master = master
        master.configure(background ="#062428")
            # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        #Create Widgets
        self.image01 = PhotoImage(file='01.png', height=120, width=120)
        self.image13 = PhotoImage(file='13.png', height=218, width=490)
        self.image15 = PhotoImage(file='15.png', height=200, width=555)
        self.image17 = PhotoImage(file='17.png', height=155, width=361)
        self.widgets1()

    #Login Function
    def login(self):
        #Establish Connection
        with sqlite3.connect('airplanereservation.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM passenger WHERE email = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            if result:
                if len(self.username.get()) == 0:
                 ms.showinfo("Warning!", "Username is empty! Write something")
                else:
                    self.redirectToReservation()
            
        else:
            ms.showerror('Oops!','Username Not Found. Please re - enter')

    def passengerInfoPage(self):
        self.mainframe.forget()
        self.head1.forget()
        self.logf1.forget()
        self.logz1.forget()
        self.top1.forget()
        PassengerDetailsGUI()
        
    def redirectToReservation(self):
        self.mainframe.forget()
        self.head1.forget()
        self.logf1.forget()
        self.logz1.forget()
        self.top1.forget() 
        ReservationGUI()

    #Draw Widgets
    def widgets1(self):
        self.mainframe = Frame(self.master, bg="#062428")
        self.mainframe.pack(fill=BOTH)
        # 1st frame
        self.lab = Label(self.mainframe,text=' ', font=('Helvetica', 30, 'bold italic'), bg="#062428", fg="#ffffff")
        self.lab.pack(fill=BOTH)
        self.l1 = Label(self.lab, bg="#062428")
        self.l1.pack(fill=BOTH)
        self.f1 = Frame(self.l1, bg="#062428")
        self.f1.pack(fill=BOTH, side=TOP)
        self.f2 = Frame(self.l1, bg="#062428")
        self.f2.pack(fill=BOTH, side=TOP)
        self.head0 = Label(self.f1, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head0.grid(row=0, column=0, padx=200, pady=100)

        self.head1 = Label(self.f1, image=self.image13, bg="#062428", fg="#ffffff")
        self.head1.grid(row=1, column=1)
        self.head1 = Label(self.f1, image=self.image17, bg="#062428", fg="#ffffff")
        self.head1.grid(row=2, column=2)
        self.head2 = Label(self.lab, text=' ', font=('Helvetica', 1000, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head2.pack(fill=BOTH, side=BOTTOM, ipady=100)
        self.l1.after(4000, lambda: self.lab.destroy())

        # 2nd frame
        self.lab1 = Label(self.mainframe, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#062428", fg="#ffffff")
        self.lab1.pack(fill=BOTH)
        self.l2 = Label(self.lab1,bg="#062428")
        self.l2.pack(fill=BOTH, pady=30)
        self.f1 = Frame(self.l2, bg="#062428")
        self.f1.pack(fill=BOTH, side=TOP)
        self.f2 = Frame(self.l2, bg="#062428")
        self.f2.pack(fill=BOTH, side=TOP)

        head = Label(self.f1, text=' ', font=('Coda Regular', 2, 'italic'), bg="#062428", fg="#ffffff")
        head.pack(fill=BOTH, side=TOP, pady=50)
        self.head0 = Label(self.f1, text=' "  You haven’t seen a tree until ', font=('Coda Regular', 25, 'italic'),
                           bg="#062428", fg="#ffffff")
        self.head0.pack(fill=BOTH, side=TOP)
        self.head01 = Label(self.f1, text=' you’ve seen its shadow from the sky. " ',
                            font=('Coda Regular', 25, 'italic'), bg="#062428", fg="#ffffff")
        self.head01.pack(fill=BOTH, side=TOP)

        self.head2 = Label(self.f2, image=self.image15, bg="#062428", fg="#ffffff")
        self.head2.pack(fill=BOTH, side=BOTTOM, pady=130)
        # self.head3 = Label(self.lab, text=' ',font=('Helvetica', 1000, 'bold italic'), bg="#062428", fg="#ffffff")
        # self.head3.pack(fill=BOTH,side=BOTTOM)

        self.l2.after(10000, lambda: self.lab1.destroy())

        # 3rd frame
        self.lab2 = Label(self.mainframe, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#062428", fg="#ffffff")
        self.lab2.pack(fill=BOTH)
        self.l3 = Label(self.lab2, bg="#062428")
        self.l3.pack(fill=BOTH)
        self.f1 = Frame(self.l3, bg="#062428")
        self.f1.pack(fill=BOTH, side=LEFT, ipadx=65)
        self.f2 = Frame(self.l3, bg="#062428")
        self.f2.pack(fill=BOTH, side=RIGHT, ipadx=65)

        self.head1 = Label(self.f1, text=' ', font=('Helvetica', 5, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head1.pack(fill=BOTH, side=TOP, ipady=20)
        self.head2 = Label(self.f1, image=self.image15, bg="#062428", fg="#ffffff")
        self.head2.pack(fill=BOTH, side=TOP, pady=60)
        self.head3 = Label(self.lab, text=' ', font=('Helvetica', 1000, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head3.pack(fill=BOTH, side=BOTTOM)

        self.head = Label(self.f2, text=' ', font=('Coda Regular', 2, 'italic'), bg="#062428", fg="#ffffff")
        self.head.pack(fill=BOTH, side=TOP, ipady=200)
        self.head0 = Label(self.f2, text=' “  To most people, the sky is the limit. ',
                           font=('Coda Regular', 25, 'italic'), bg="#062428", fg="#ffffff")
        self.head0.pack(fill=BOTH, side=TOP)
        self.head01 = Label(self.f2, text=' To those who love aviation,  ', font=('Coda Regular', 25, 'italic'),
                            bg="#062428", fg="#ffffff")
        self.head01.pack(fill=BOTH, side=TOP)
        self.head02 = Label(self.f2, text=' the sky is home. ”', font=('Coda Regular', 25, 'italic'), bg="#062428",
                            fg="#ffffff")
        self.head02.pack(fill=BOTH, side=TOP)
        self.head03 = Label(self.f2, text=' ', font=('Coda Regular', 20, 'italic'), bg="#062428", fg="#ffffff")
        self.head03.pack(fill=BOTH, side=BOTTOM, ipady=90)

        self.l3.after(16000, lambda: self.lab2.destroy())

        # 4th frame
        self.lab3 = Label(self.mainframe, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#062428", fg="#ffffff")
        self.lab3.pack(fill=BOTH)
        self.l4 = Label(self.lab3, bg="#062428")
        self.l4.pack(fill=BOTH)
        self.f1 = Frame(self.l4, bg="#062428")
        self.f1.pack(fill=BOTH, side=LEFT, ipadx=70, padx=0)
        self.f2 = Frame(self.l4, bg="#062428")
        self.f2.pack(fill=BOTH, side=RIGHT, ipadx=100)

        self.head = Label(self.f1, text=' ', font=('Coda Regular', 2, 'italic'), bg="#062428", fg="#ffffff")
        self.head.pack(fill=BOTH, side=TOP, pady=100)
        self.head0 = Label(self.f1, text=' “  Aeronautics was neither an industry', font=('Coda Regular', 25, 'italic'),
                           bg="#062428", fg="#ffffff")
        self.head0.pack(fill=BOTH, side=TOP)
        self.head01 = Label(self.f1, text=' nor a science.  ', font=('Coda Regular', 25, 'italic'), bg="#062428",
                            fg="#ffffff")
        self.head01.pack(fill=BOTH, side=TOP)
        self.head02 = Label(self.f1, text='It was a miracle. ”', font=('Coda Regular', 25, 'italic'), bg="#062428",
                            fg="#ffffff")
        self.head02.pack(fill=BOTH, side=TOP)
        self.head03 = Label(self.f1, text=' ', font=('Coda Regular', 25, 'italic'), bg="#062428", fg="#ffffff")
        self.head03.pack(fill=BOTH, side=BOTTOM, pady=50)

        self.head1 = Label(self.f2, text=' ', font=('Helvetica', 5, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head1.pack(fill=BOTH, side=TOP, ipady=130)
        self.head2 = Label(self.f2, image=self.image15, bg="#062428", fg="#ffffff")
        self.head2.pack(fill=BOTH, side=BOTTOM, pady=70)
        self.head3 = Label(self.lab, text=' ', font=('Helvetica', 1000, 'bold italic'), bg="#062428", fg="#ffffff")
        self.head3.pack(fill=BOTH, side=BOTTOM)
        self.l4.after(22000, lambda: self.lab3.destroy())



        self.lab5 = Label(self.mainframe, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#062428", fg="#ffffff")
        self.lab5.pack(fill=BOTH)
        self.logz1 = Frame(self.lab5, padx=10, pady=10, bg="#062428")
        self.top1 = Label(self.logz1, text=" ", font=('Helvetica', 35, 'bold italic'), pady=30, padx=20, bg="#062428", fg="#ffffff")
        self.top1.pack()
        self.head1 = Label(self.logz1, image=self.image01, font=('Helvetica', 35, 'bold italic'), pady=30, padx=20, bg="#062428", fg="#ffffff")
        self.head1.pack()
        self.logz1.pack()
        self.logf1 = Frame(self.logz1, padx=10, pady=10, bg="#062428")
        Label(self.logf1, text=' Username / Email : ', font=('Coda Regular', 19, 'italic'), bg="#062428", fg="#ffffff",
              pady=10, padx=10).grid(sticky=W, pady=10, padx=10)
        Entry(self.logf1, textvariable=self.username, bd=5, font=('Coda Regular', 14, 'italic')).grid(row=0, column=1)
        Label(self.logf1, text=' Password : ', font=('Coda Regular', 19, 'italic'), bg="#062428", fg="#ffffff",
              pady=10, padx=10).grid(sticky=W, pady=10, padx=10)
        Entry(self.logf1, textvariable=self.password, bd=5, font=('Coda Regular', 14, 'italic'), show='*').grid(row=1, column=1, pady=10,
                                                                                         padx=10)
        Button(self.logf1, text=' Login ', bd=3, font=('Coda Regular', 13, 'italic'), padx=0, pady=0,
               command=self.login).grid(pady=20, padx=20)
        Button(self.logf1, text=' Create Account ', bd=3, font=('Coda Regular', 13, 'italic'), padx=0, pady=0,
               command=self.passengerInfoPage).grid(row=2, column=1, pady=25, padx=20)
        self.logf1.pack()
        
        

if __name__ == '__main__':
    #Create Object
    #and setup window
    root1 = Tk()
    root1.title('Travel World')
    #root.geometry('1366x768')
    root1.state("zoomed")
    main(root1)
    root1.mainloop()
