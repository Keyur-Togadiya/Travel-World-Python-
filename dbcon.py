#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('airplanereservation.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE IF NOT EXISTS airplane(
         planeID 		INT 	PRIMARY KEY     NOT NULL,
         manufacturer  CHAR(50)    				NOT NULL,
         model          CHAR(50)     			NOT NULL);''')


conn.execute('''CREATE TABLE IF NOT EXISTS flight(
          origin      CHAR(20) NOT NULL,
          destination CHAR(20) NOT NULL,
          departure   TEXT NOT NULL,
          arrival     TEXT NOT NULL,
          seatleft    INT(50)  NOT NULL,
          price       INT(20)  NOT NULL,
          type        CHAR(20) NOT NULL,
          planeID 	  INT(10) NOT NULL,
          flightID    INT(10) PRIMARY KEY NOT NULL);''')

conn.execute('''CREATE TABLE IF NOT EXISTS passenger
          (firstname  CHAR(20) NOT NULL,
           lastname   CHAR(20) NOT NULL,
           dob        TEXT NOT NULL,
           email      VARCHAR(20) PRIMARY KEY NOT NULL,
           phone      INT(10) NOT NULL,
           address    VARCHAR(50) NOT NULL,
           cardnumber VARCHAR(20)NOT NULL,
           city       CHAR(20) NOT NULL,
           state      CHAR(20) NOT NULL,
           zip        VARCHAR(20) NOT NULL,
           country    CHAR(20) NOT NULL,
           password   VARCHAR(20) NOT NULL);''')

conn.execute('''CREATE TABLE IF NOT EXISTS reservation
          (flightID  INT NOT NULL,
           email INT NOT NULL,
	   dogoing   TEXT NOT NULL,
	   doreturning  TEXT NOT NULL);''')

 #insert queries
conn.execute("INSERT INTO flight VALUES('Mumbai' ,'Delhi' ,'03:00:30' ,'06:00:30' ,50,5000 ,'One Way' ,1, 1)");    
conn.execute("INSERT INTO flight VALUES('Mumbai' ,'Goa' ,'05:00:30' ,'07:00:30' ,50,21000 ,'Two Way', 2, 2)");
conn.execute("INSERT INTO flight VALUES('Mumbai' ,'Chennai' ,'08:00:30' ,'10:00:30' ,5,12000 ,'One Way', 3, 3)");
conn.execute("INSERT INTO flight VALUES('Mumbai' ,'Hyderabad' ,'11:00:30' ,'14:00:30' ,30,9000 ,'Two Way', 4, 4)");

conn.execute("INSERT INTO flight VALUES('Delhi' ,'Mumbai' ,'03:00:30' ,'06:00:30' ,20,4000 ,'Two Way', 1, 6)");
conn.execute("INSERT INTO flight VALUES('Delhi' ,'Goa' ,'06:00:30' ,'09:00:30' ,50,15000 ,'One Way', 5, 7)");
conn.execute("INSERT INTO flight VALUES('Delhi' ,'Chennai' ,'03:00:30' ,'06:00:30' ,40,12000 ,'Two Way', 6, 8)");
conn.execute("INSERT INTO flight VALUES('Delhi' ,'Hyderabad' ,'08:00:30' ,'11:00:30' ,30,16000 ,'One Way', 7, 9)");

conn.execute("INSERT INTO flight VALUES('Chennai' ,'Goa' ,'00:00:30' ,'05:00:30' ,50,27000 ,'One Way', 8, 11)");
conn.execute("INSERT INTO flight VALUES('Chennai' ,'Delhi' ,'15:00:30' ,'18:00:30' ,40,9000 ,'Two Way', 9, 13)");
conn.execute("INSERT INTO flight VALUES('Chennai' ,'Hyderabad' ,'13:00:30' ,'16:00:30' ,30,12000 ,'One Way', 10, 15)");

conn.execute("INSERT INTO flight VALUES('Goa' ,'Delhi' ,'20:00:30' ,'23:00:30' ,50,7000 ,'Two Way', 5, 12)");
conn.execute("INSERT INTO flight VALUES('Goa' ,'Mumbai' ,'03:00:30' ,'5:00:30' ,30,9000 ,'Two Way', 2, 14)");
conn.execute("INSERT INTO flight VALUES('Goa' ,'Chennai' ,'04:00:30' ,'06:00:30' ,20,12000 ,'One Way', 8, 25)");

conn.execute("INSERT INTO flight VALUES('Hyderabad' ,'Mumbai' ,'08:00:30' ,'11:00:30' ,20,9000 ,'Two Way', 4, 21)");
conn.execute("INSERT INTO flight VALUES('Hyderabad' ,'Chennai' ,'09:00:30' ,'12:00:30' ,50,8000 ,'One Way', 10, 22)");
conn.execute("INSERT INTO flight VALUES('Hyderabad' ,'Goa' ,'10:00:30' ,'14:00:30' ,40,17000 ,'Two Way', 9, 24)");
conn.execute("INSERT INTO flight VALUES('Hyderabad' ,'Delhi' ,'18:00:30' ,'19:00:30' ,10,12000 ,'One Way', 7, 23)");

conn.execute("INSERT INTO airplane VALUES(1, 'Kingfisher', 'K1')");
conn.execute("INSERT INTO airplane VALUES(2, 'Kingfisher', 'K2')");
conn.execute("INSERT INTO airplane VALUES(3, 'Etihad', 'E1')");
conn.execute("INSERT INTO airplane VALUES(4, 'Air India', 'A1')");
conn.execute("INSERT INTO airplane VALUES(5, 'Jet Airways', 'J1')");

conn.execute("INSERT INTO airplane VALUES(6, 'Vistara', 'V1')");
conn.execute("INSERT INTO airplane VALUES(7, 'GoAir', 'G1')");
conn.execute("INSERT INTO airplane VALUES(8, 'SpiceJet', 'S1')");
conn.execute("INSERT INTO airplane VALUES(9, 'Indigo', 'I1')");
conn.execute("INSERT INTO airplane VALUES(10, 'Pawan Hans', 'P1')");

conn.execute("INSERT INTO passenger VALUES('test', 'test', '03-01-1998', 'test@gmail.com', '1111111111', 'test addrees', 'a12123', 'Mumbai','Maharastra','68','India','test')");

conn.execute("INSERT INTO passenger VALUES('admin', 'admin', '03-01-1998', 'admin@gmail.com', '1111111111', 'test addrees', 'a12123', 'Mumbai','Maharastra','68','India','admin')");


conn.commit()
conn.close()
    
