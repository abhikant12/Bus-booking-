
from tkinter import *
from tkinter.messagebox import *
import sqlite3
from datetime import date
con=sqlite3.Connection("abhi_kant")
cur=con.cursor()


class  abhikant:
    
    def firstscreen(self):
        root = Tk()
        h,w = root.winfo_screenheight() , root.winfo_screenwidth()
        root.state('zoomed')
        root.title("Bus Booking")

        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 3,columnspan = 8 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 1,column = 3, padx = w//3)
        Label(root , text = "\n\n Name : Abhikant kumar \n" , fg = 'blue' , font = 'Arial 12 bold').grid(row = 2,column = 3, padx = w//3)
        Label(root , text = "\n Er. : 211b408 \n" , fg = 'blue' , font = 'Arial 12 bold').grid(row = 3,column = 3, padx = w//3)
        Label(root , text = "\n Mobile : 9304324380 \n" , fg = 'blue' , font = 'Arial 12 bold').grid(row = 4,column = 3, padx = w//3)
        Label(root , text = "Submitted to : Dr. Mahesh kumar " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 5,column = 3, padx = w//3)
        Label(root , text = "Project Based Learning " ,  fg = 'red' , font = 'Arial 11 bold').grid(row = 6,column = 3, padx = w//3)
       
        def funtion1(abhi = 0):
            root.destroy()
            self.secondscreen()
        root.bind('<KeyPress>',funtion1)
        
        root.mainloop()


        
    def secondscreen(self):
        root = Tk()
        h,w = root.winfo_screenheight() , root.winfo_screenwidth()
        root.state('zoomed')
        root.title("Bus Booking")
        
        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 0,columnspan = 8 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 1,column = 0,columnspan = 8, padx = w//3)

        def Seat_Booking(abhi=0):
            root.destroy()
            self.thirdscreen()

        def Check_Booked_Seat(abhi=0):
            root.destroy()
            self.fifthscreen()
            
        def add_bus_details(abhi=0):
            root.destroy()
            self.sixthscreen()
            
        
        Button(root , text = " Seat Booking" , bg = 'lightgreen' , fg = 'black' , font = 'Arial 12 bold' , command=Seat_Booking).grid(row = 3,column = 3 , pady = 40)
        Button(root , text = "Check Booked Seat" , bg = 'limegreen' , fg = 'black' , font = 'Arial 12 bold' , command=Check_Booked_Seat).grid(row = 3,column = 4)
        Button(root , text = "Add Bus Details" , bg = 'forestgreen' , fg = 'black' , font = 'Arial 12 bold' , command=add_bus_details).grid(row = 3,column = 5)
        Label(root , text = "For Admin Only" , fg = 'red' , font = 'Arial 11 bold').grid(row = 4,column = 5)
        root.mainloop()





    def thirdscreen(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.state('zoomed')
        root.title("Bus Booking")
        
        frame1=Frame(root)
        frame1.grid(row=3,column=0,columnspan=16,padx=250)
        frame2=Frame(root)
        frame2.grid(row=4,column=0,padx=250)
        frame3=Frame(root)
        frame3.grid(row=7,column=0,columnspan=10,padx=100)

        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 0,columnspan = 35 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 1,column = 0,columnspan = 35)
        Label(root , text = "Enter Journey Details" , bg = 'lightgreen' , fg = 'green' , font = 'Arial 15 bold').grid(row = 2,column = 0,columnspan = 35 , pady = 20)


        Label(frame1 ,text="To :",font='Arial 10 bold').grid(row=3,column=0,sticky=E)
        To=Entry(frame1)
        To.grid(row=3,column=1 ,sticky=W)
        Label(frame1,text="       From :",font='Arial 10 bold').grid(row=3,column=2,sticky=E)
        From=Entry(frame1)
        From.grid(row=3,column=3,sticky=W)
        Label(frame1,text='       Journey Date',font='Arial 10 bold' ).grid(row=3,column=4,sticky=E)
        Jdate=Entry(frame1)
        Jdate.grid(row=3,column=5,sticky=W)


        bus_select = IntVar()
        gender = StringVar()

        def show_bus():
            a = To.get()
            b = From.get()
            c = Jdate.get()

            
            if(len(a)==0 or len(b)==0 or len(c)==0):
                showerror('Error','Please Fill all info...')
                
            else: 
                global r
                r = IntVar()
                cur.execute('select * from route where station_name = (?)' , (a , ))
                to_records = cur.fetchall()
             
                cur.execute('select * from route where station_name = (?)' , (b , ))
                from_records = cur.fetchall()
                
                if(to_records == []  or from_records == []):
                    showinfo("sorry"," we have no bus on this route")
                    return 
               
                tempid = 0
                for rec in to_records:
                    for rec1 in from_records:
                        if(rec[0] == rec1[0]):
                            if(rec[2] > rec1[2]):
                                tempid = rec[0]                      #finding the route where station_id of to_record is greater then station_id of from_record;
   
                if(tempid == 0):
                    showinfo('No bus found','sorry ,no buses are available')
                    return
                
                cur.execute('select * from run where b_id in(select bus_id from bus where r_id = (?)) and running_date = (?) and seat_available >= 0',(tempid , c))
                global run_info
                run_info = cur.fetchall()
                
                if(run_info == []):
                    showinfo("sorry","no bus found")
                    return
             
                Label(frame2,text='Select Bus',font='Arial 10 bold',fg='dark green').grid(row=4,column=0,pady=10,padx=20)
                Label(frame2,text='Operator',font='Arial 10 bold',fg='dark green').grid(row=4,column=2,pady=10,padx=20)
                Label(frame2,text='Bus Type',font='Arial 10 bold',fg='dark green').grid(row=4,column=4,pady=10,padx=20)
                Label(frame2,text='Available/Capacity',font='Arial 10 bold',fg='dark green').grid(row=4,column=6,pady=10,padx=20)
                Label(frame2,text='Fare',font='Arial 10 bold',fg='dark green').grid(row=4,column=8,pady=10,padx=20)
                
                enteries = len(run_info)
                counter = 0
                while(enteries > 0):
                    cur.execute('select * from bus where bus_id = (?)' ,(run_info[counter][0] , ))
                    bus_info=cur.fetchall()

                    cur.execute("select name from operator where op_id = (?)" , (bus_info[0][5] , ))                  
                    op_name=cur.fetchall()

                    
                    Radiobutton(frame2 , text = 'bus'+str(counter+1) , value = counter+1  ,variable = r , bg='steel blue').grid(row = counter+5,column=0,pady=10,padx=20)
                    Label(frame2,text=op_name[0][0],fg='blue',font='helvetica 12 italic').grid(row = counter+5,column=2,pady=10,padx=20)
                    Label(frame2,text=bus_info[0][1],fg='blue',font='helvetica 12 bold').grid(row = counter+5,column=4,pady=10,padx=20)
                    Label(frame2,text=str(run_info[counter][2])+'/'+str(bus_info[0][2]),fg='blue',font='helvetica 12 bold').grid(row = counter+5,column=6,pady=10,padx=20)
                    Label(frame2,text=bus_info[0][3],fg='blue',font='helvetica 12 bold').grid(row = counter+5,column=8,pady=10,padx=20)
                    counter = counter+1
                    enteries = enteries - 1

                


                def proceed_to_book():
                    if(r.get() == 0):
                        showerror('info','Please Select any Bus')
                        return 
                    else:
                        
                        Label(frame3,text='Fill Passenger Details to book the bus ticket',font="Arial 20 bold",bg='light blue',fg='red').grid(row=6,column=0,columnspan=15,pady=20)
                        Label(frame3,text='Name',font='Arial 10 bold').grid(row=8,column=0)
                        Name=Entry(frame3)
                        Name.grid(row=8,column=1)
                        Label(frame3,text='   Gender',font='Arial 10 bold').grid(row=8,column=2)
                        gender.set("Male")
                        option=['Male','Female','other Gender']
                        menu=OptionMenu(frame3,gender,*option)
                        #gender.config(font="Arial 11 bold")
                        menu.grid(row=8,column=4)
                        Label(frame3,text='   No of seats',font='Arial 10 bold').grid(row=8,column=5)
                        No_of_seat=Entry(frame3)
                        No_of_seat.grid(row=8,column=7)
                        Label(frame3,text='   Mobile No',font='Arial 10 bold').grid(row=8,column=8)
                        Mob_no=Entry(frame3)
                        Mob_no.grid(row=8,column=9)
                        Label(frame3,text='   Age',font='Arial 10 bold').grid(row=8,column=10)
                        Age=Entry(frame3)
                        Age.grid(row=8,column=11)
                           
                        def Book_seat():
                            n = Name.get()
                            no = No_of_seat.get()
                            m = Mob_no.get()
                            A = Age.get()
                            if(len(n)==0 or len(no)==0 or len(m)==0 or len(A)==0 or gender.get() == 0):
                                showerror('Error','Please Fill all info...')
                                return 
                            elif(int(A) > 125):
                                showerror('Error','Please enter a valid age...')
                                Age.delete(0,END)
                                return
                            elif(len(m) != 10):
                                showerror('Error','Please enter valid moblie number...')
                                Mob_no.delete(0,END)
                                return
                            elif(int(no) > run_info[(r.get()) - 1][2] or int(no) <= 0):
                                showerror('Error','please enter a valid number of seats')
                                No_of_seat.delete(0,END)
                                return
                            else:

                                cur.execute("select booking_id , phone from booking_history")
                                check = cur.fetchall()
                                for ph in check:                
                                    if(int(ph[1]) == int(m)):
                                        showinfo("record exist" , "booking from this number already exit..")
                                        return    

                                global booking_id    
                                booking_id = len(check) + 1                        #booking_id is  total no of booking in past + 1;
                                cur.execute('select * from bus where bus_id = (?)' , (run_info[r.get() - 1][0] , ))
                                bus_info = cur.fetchall()                          
                               
                                choice = askyesno("confimation","your fare is "+str(int(no)*bus_info[0][3])+'\nConfirm booking?')
                                
                                if(choice == True):
                                    showinfo('Success','Seat booked!')
                                    today = str(date.today())                  #2019-12-11   so converted into  11/12/2019
                                    ans = today[8]+today[9] + "/" + today[5]+today[6] + "/" + today[0]+today[1]+today[2]+today[3] 
                                    cur.execute("INSERT INTO Booking_history(booking_id,p_name,phone,travel_on,booked_on,gender,age,source,destination,fare,seats) VALUES(?, ?, ?,?, ?, ?,?,?,?,?,?)", (booking_id, n , m,c, ans, gender.get(), A, b, a, (int(no)*bus_info[0][3]),no))
                                 
                                    new = run_info[r.get() - 1][2]-int(no)
                                    cur.execute("update run     set seat_available = (?)      where b_id = (?) and running_date = (?) ", (new , bus_info[0][0] , c))
                                    
                                    root.destroy()
                                    self.fourthscreen()
                                else:
                                    showerror('Cancel' , 'Booked seat cancelled..')
                                    return
                                                                    
                        Button(frame3,text = 'Book seat' ,command = Book_seat ,font = 'Arial 12 bold' ,bg = 'light green').grid(row=8,column=12,padx = 15)
                Button(frame2,text='Proceed to Book',command = proceed_to_book,font = 'Arial 12 bold',bg = 'light green').grid(row=5,column=9,pady=0,padx=20)
        Button(frame1 , text = " Show Bus" , command = show_bus, bg = 'lightgreen' , fg = 'black' , font = 'Arial 12 bold').grid(row=3,column=7,padx = 10)

        def HOME1(abhi = 0):
            root.destroy()
            self.secondscreen()
            
        home = PhotoImage(file='.\\home.png')
        Button(frame1,image = home , command = HOME1).grid(row=3,column=8 , padx = 20)
        root.mainloop()




    def fourthscreen(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.state('zoomed')
        root.title("Bus Ticket")

        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 0,columnspan = 35 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 20 bold').grid(row = 1,column = 0,columnspan = 35)
        Label(root , text = "Bus Ticket" , fg = 'black' ,  font = 'Arial 15 bold').grid(row = 2,column = 0,columnspan = 35 , pady = 10)

        frame2 =  Frame(root, relief = "groove" , bd = 3)
        frame2.grid(row = 3 ,column = 0 ,columnspan=10 , padx = 450)

        cur.execute("SELECT * FROM booking_history where booking_id = (?) ", (booking_id , ))                   #comma to make tuple
        info = cur.fetchall()
    
        ans = "Passengers : " + str(info[0][1]) + "      Gender : " + str(info[0][5]) + "\nNo. of seats : " + str(info[0][10]) + "      Phone : " + str(info[0][2]) + "\n Age : " + str(info[0][6]) + "      Fare Rs : " + str(info[0][9])
        ans = ans + "\nBooking Ref : " + str(info[0][0]) + "      Travel On : " + str(info[0][3]) + "\n Booked on : " + str(info[0][4]) + "                                   " + "\n boarding point : " + str(info[0][7]) + "    Destination point : " + str(info[0][8])  
        Label(frame2, text = ans ,font = 'Arial 13 bold').grid(row = 3,column=0 , sticky = E)
        Label(frame2 , text='* Total fare of '+str(info[0][9])+' /- to be paid at the time of boarding the bus' , font='Arial 12 italic').grid(row = 4,column=0,columnspan=10)

        def exitt():
            root.destroy()
        def home(abhi = 0):
            root.destroy()
            self.secondscreen()
       
        Button(root,text='Exit' , font='Times_new_roman 10',command = exitt).grid(row=5,column=1,columnspan=10)
        photu=PhotoImage(file="home.png")
        Button(root,image=photu,font='Times_new_roman 10',command = home).grid(row=5,column=0,columnspan=10)
        root.mainloop()




        
    def fifthscreen(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.state('zoomed')
        
       
        def check_booking():           
            if(len(Enter_your_mobile_no_entry.get()) != 10):
                showerror('Invalid','Please Enter valid mobile number')
            else :
                frame2 =  Frame(frame1 , relief = "sunken" , bd = 3)
                frame2.grid(row = 4 ,column = 0 ,columnspan=10 , pady = 30)
                
                cur.execute("select * from booking_history where phone = (?)" , (Enter_your_mobile_no_entry.get(),))                 #comma to make tuple
                info = cur.fetchall()
                
                if(len(info) > 0):
                    ans = "Passengers : " + str(info[0][1]) + "      Gender : " + str(info[0][5]) + "\nNo. of seats : " + str(info[0][10]) + "      Phone : " + str(info[0][2]) + "\n Age : " + str(info[0][6]) + "      Fare Rs : " + str(info[0][9])
                    ans = ans + "\nBooking Ref : " + str(info[0][0]) + "      Travel On : " + str(info[0][3]) + "\n Booked on : " + str(info[0][4]) + "                                   " + "\n boarding point : " + str(info[0][7]) + "    Destination point : " + str(info[0][8])  
                    Label(frame2, text = ans ,font = 'Arial 13 bold').grid(row = 4,column=0 , sticky = E)
                    Label(frame2 , text='* Total fare of '+str(info[0][9])+' /- to be paid at the time of boarding the bus' , font='Arial 12 italic').grid(row = 5,column=0,columnspan=10)            
                else:
                    choice = askyesno("no records found","do you want to book the seat ?")
                    if(choice == True):
                        root.destroy()
                        self.thirdscreen()
                    else:
                        choice1 = askyesno("EXIT" , "do you want to leave ")
                        if(choice1 == True):
                            root.destroy()
                          
                        
        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 0,columnspan = 35 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 1,column = 0,columnspan = 35)
        Label(root , text = "Check Your Booking" , bg = 'lightgreen' , fg = 'green' , font = 'Arial 15 bold').grid(row = 2,column = 0,columnspan = 35 , pady = 40)

        frame1 = Frame(root)
        frame1.grid(row=3,column=0,columnspan=16,padx=450)
        Label(frame1 ,text = "Enter Your Mobile No:" , font='Arial 10 bold').grid(row=3,column=0)
        Enter_your_mobile_no_entry = Entry(frame1)
        Enter_your_mobile_no_entry.grid(row=3,column = 1)
        
        Button(frame1,text="Check Booking",command=check_booking).grid(row=3,column = 2 , padx = 30)

        
        def home(abhi=0):
            root.destroy()
            self.secondscreen()
            
        img_1 = PhotoImage(file=".\\home.png")
        Button(frame1,image = img_1,command = home).grid(row=3,column = 3)
        root.mainloop()




    def sixthscreen(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.state('zoomed')

        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 0,columnspan = 35 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 1,column = 0,columnspan = 35)
        Label(root , text = "Add New Details to DataBase" , bg = 'lightgreen' , fg = 'green' , font = 'Arial 15 bold').grid(row = 2,column = 0,columnspan = 35 , pady = 40)


        def add_operator():
            root.destroy()
            self.seventhscreen()
        def add_new_bus():
            root.destroy()
            self.ninthscreen()
        def add_new_route():
            root.destroy()
            self.tenthscreen()
        def add_new_run():
            root.destroy()
            self.eleventhscreen()


        frame1 = Frame(root)
        frame1.grid(row=3,column=0,columnspan=16,padx=450)
        Button(frame1,text="New Operator",bg="light green",command=add_operator).grid(row=3,column=1)
        Button(frame1,text="New Bus",bg="orange red",command=add_new_bus).grid(row=3,column=2 , padx = 40)
        Button(frame1,text="New Route",bg="royal blue",command=add_new_route).grid(row=3,column=3)
        Button(frame1,text="New Run",bg="rosy brown",command=add_new_run).grid(row=3,column=4 , padx = 40)
        root.mainloop()




    def seventhscreen(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.state('zoomed')


        def insert():
            if(len(operator_id_entry.get())== 0 or len(name_entry.get())== 0 or len(address_entry.get())== 0 or len(phone_entry.get())== 0 or len(email_entry.get())== 0):
                showerror('Value Missing','Please Enter all the details')
            else :
                cur.execute('insert into operator(op_id,name,address,phone,email) values(?,?,?,?,?)',(operator_id_entry.get(),name_entry.get(),address_entry.get(),phone_entry.get(),email_entry.get()))
                a=str(operator_id_entry.get())+' '+str(name_entry.get())+' '+str(address_entry.get())+' '+str(phone_entry.get())+' '+str(email_entry.get())
                Label(frame1,text=a).grid(row=4,column=4,columnspan=10)
                con.commit()
                
                
        def edit():
             
            if(len(operator_id_entry.get())== 0 or len(name_entry.get())== 0 or len(address_entry.get())== 0 or len(phone_entry.get())== 0 or len(email_entry.get())== 0):
                showerror('Value Missing','Please Enter all the details')
            else:
                cur.execute('delete from operator where op_id = (?)' , (operator_id_entry.get() , ))
                con.commit()
                cur.execute('insert into operator(op_id,name,address,phone,email) values(?,?,?,?,?)',(operator_id_entry.get(),name_entry.get(),address_entry.get(),phone_entry.get(),email_entry.get()))
                a=str(operator_id_entry.get())+' '+str(name_entry.get())+' '+str(address_entry.get())+' '+str(phone_entry.get())+' '+str(email_entry.get())
                Label(frame1,text=a).grid(row=4,column=4,columnspan=10)
                con.commit()
               


        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 0,columnspan = 35 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 1,column = 0,columnspan = 35)
        Label(root , text = "Add Bus Operator Details " , bg = 'lightgreen' , fg = 'green' , font = 'Arial 15 bold').grid(row = 2,column = 0,columnspan = 35 , pady = 40)


        frame1 = Frame(root)
        frame1.grid(row=3,column=0,columnspan=16,padx=100)

        Label(frame1 ,text="Operator id" ,font='Arial 10 bold').grid(row=3,column=0,sticky=E)
        operator_id_entry = Entry(frame1)
        operator_id_entry.grid(row=3,column=1 ,sticky=W)
        Label(frame1,text="     Name",font='Arial 10 bold').grid(row=3,column=2,sticky=E)
        name_entry = Entry(frame1)
        name_entry.grid(row=3,column=3 ,sticky=W)
        Label(frame1,text="      Address",font='Arial 10 bold' ).grid(row=3,column=4,sticky=E)
        address_entry = Entry(frame1)
        address_entry.grid(row=3,column=5,sticky=W)
        Label(frame1,text="      Phone",font='Arial 10 bold' ).grid(row=3,column=6,sticky=E)
        phone_entry = Entry(frame1)
        phone_entry.grid(row=3,column=7,sticky=W)
        Label(frame1,text="      Email",font='Arial 10 bold' ).grid(row=3,column=8,sticky=E)
        email_entry = Entry(frame1)
        email_entry.grid(row=3,column=9,sticky=W)

        Button(frame1,text="Add",bg="light green",command = insert).grid(row=3,column=10,sticky=W , padx = 20)
        Button(frame1,text="Edit",bg="light green",command = edit).grid(row=3,column=11,sticky=W)

        def home(abhi=0):
            root.destroy()
            self.secondscreen()

        img_1 = PhotoImage(file=".\\home.png")
        Button(frame1,image=img_1,command=home).grid(row=3,column=12 , padx = 20)
        root.mainloop()


   


    def ninthscreen(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.state('zoomed')

        def insert():
            
            if(len(bus_id_entry.get()) == 0 or len(capacity_entry.get()) == 0 or len(fare_entry.get())== 0 or len(route_id_entry.get())== 0 or len(operator_id_entry.get()) == 0):
                showerror('Value Missing','Please Enter all the details')
            else :
                cur.execute('insert into bus(bus_id,bus_type,capacity,fare,r_id,operator_id) values(?,?,?,?,?,?)',(bus_id_entry.get(),bus_type.get(),capacity_entry.get(),fare_entry.get(),route_id_entry.get(),operator_id_entry.get()))    
                st = str(bus_id_entry.get())+' '+str(bus_type.get())+' '+str(capacity_entry.get())+'   '+str(fare_entry.get())+'   '+str(route_id_entry.get())+'   '+str(operator_id_entry.get())
                Label(frame1,text=st).grid(row=4,column=0,columnspan=10)
                con.commit()
                
                
        def edit():           
             
            if(len(bus_id_entry.get()) == 0 or len(capacity_entry.get()) == 0 or len(fare_entry.get())== 0 or len(route_id_entry.get())== 0 or len(operator_id_entry.get()) == 0):
                showerror('Value Missing','Please Enter all the details')
            else:
                cur.execute('delete from bus where bus_id = (?)' , (bus_id_entry.get() , ))
                con.commit()
                
                cur.execute('insert into bus(bus_id,bus_type,capacity,fare,r_id,operator_id) values(?,?,?,?,?,?)',(bus_id_entry.get(),bus_type.get(),capacity_entry.get(),fare_entry.get(),route_id_entry.get(),operator_id_entry.get()))
                st = str(bus_id_entry.get())+' '+str(bus_type.get())+' '+str(capacity_entry.get())+'   '+str(fare_entry.get())+'   '+str(route_id_entry.get())+'   '+str(operator_id_entry.get())
                Label(frame1,text = st).grid(row=4,column=4,columnspan=10)
                con.commit()
               


        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 0,columnspan = 35 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 1,column = 0,columnspan = 35)
        Label(root , text = "Add Bus Details " , bg = 'lightgreen' , fg = 'green' , font = 'Arial 15 bold').grid(row = 2,column = 0,columnspan = 35 , pady = 40)


        frame1 = Frame(root)
        frame1.grid(row=3,column=0,columnspan=16,padx=10)
        Label(frame1 ,text="Bus ID" ,font='Arial 10 bold').grid(row=3,column=0,sticky=E)
        bus_id_entry = Entry(frame1)
        bus_id_entry.grid(row=3,column=1 ,sticky=W)
        Label(frame1,text="     Bus Type",font='Arial 10 bold').grid(row=3,column=2,sticky=E)
        bus_type = StringVar()
        bus_type.set("Bus Type")
        option = ["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC-Sleeper 2x1","Non-AC sleeper 2x1"]
        d_menu = OptionMenu(frame1,bus_type,*option)
        d_menu.grid(row=3,column=3,sticky=W)
        Label(frame1,text="      Capacity",font='Arial 10 bold' ).grid(row=3,column=4,sticky=E)
        capacity_entry = Entry(frame1)
        capacity_entry.grid(row=3,column=5,sticky=W)
        Label(frame1,text="      Fare Rs",font='Arial 10 bold' ).grid(row=3,column=6,sticky=E)
        fare_entry = Entry(frame1)
        fare_entry.grid(row=3,column=7,sticky=W)
        Label(frame1,text="      Route id",font='Arial 10 bold' ).grid(row=3,column=8,sticky=E)
        route_id_entry = Entry(frame1)
        route_id_entry.grid(row=3,column=9,sticky=W)
        Label(frame1,text="      operator id",font='Arial 10 bold' ).grid(row=3,column=10,sticky=E)
        operator_id_entry = Entry(frame1)
        operator_id_entry.grid(row=3,column=11,sticky=W)

        
        Button(frame1,text="Add Bus",bg="light green",command = insert).grid(row=3,column=12,sticky=W , padx = 20)
        Button(frame1,text="Edit Bus",bg="light green",command = edit).grid(row=3,column=13,sticky=W)

        def home(abhi=0):
            root.destroy()
            self.secondscreen()

            
        img_1 = PhotoImage(file=".\\home.png")
        Button(frame1,image=img_1,command=home).grid(row=4,column=12)
        root.mainloop()



        
    def tenthscreen(self):
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.state('zoomed')

        def insert():
            if(len(route_id.get()) == 0 or len(station_name.get()) == 0 or len(station_id.get()) == 0):
                showerror('Value Missing','Please Enter all the details')
            else :
                cur.execute('insert into route(route_id,station_name,station_id) values(?,?,?)',(route_id.get(),station_name.get(),station_id.get()))    
                st = str(route_id.get())+' '+str(station_name.get())+' '+str(station_id.get())
                Label(frame1 , text = st).grid(row = 4,column=0,columnspan=10)
                con.commit()
            
        def delete():
            cur.execute('''delete from route where route_id = (?) and station_id = (?)''',(route_id.get() ,station_id.get()))
            con.commit()
         
            
        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 0,columnspan = 35 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 1,column = 0,columnspan = 35)
        Label(root , text = "Add Bus Route Details " , bg = 'lightgreen' , fg = 'green' , font = 'Arial 15 bold').grid(row = 2,column = 0,columnspan = 35 , pady = 40)


        frame1 = Frame(root)
        frame1.grid(row=3,column=0,columnspan=16,padx=200)
        Label(frame1 ,text="Route ID" ,font='Arial 10 bold').grid(row=3,column=0,sticky=E)
        route_id = Entry(frame1)
        route_id.grid(row=3,column=1 ,sticky=W)
        Label(frame1,text="     Station Name",font='Arial 10 bold').grid(row=3,column=2,sticky=E)
        station_name = Entry(frame1)
        station_name.grid(row=3,column=3,sticky=W)        
        Label(frame1,text="     Station ID",font='Arial 10 bold' ).grid(row=3,column=4,sticky=E)
        station_id = Entry(frame1)
        station_id.grid(row=3,column=5,sticky=W)
        Button(frame1,text="Add Route",bg="light green",command = insert).grid(row=3,column=6,sticky=W , padx = 20)
        Button(frame1,text="delete Route",bg="light green",command = delete).grid(row=3,column=7,sticky=W)

        def home(abhi=0):
            root.destroy()
            self.secondscreen()

            
        img_1 = PhotoImage(file=".\\home.png")
        Button(frame1,image=img_1,command=home).grid(row=3,column=8,sticky=W , padx = 20)
        root.mainloop()



        
    def eleventhscreen(self):
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.state('zoomed')

        def insert():
            if(len(bus_id.get()) == 0 or len(running_date.get()) == 0 or len(seat_avail.get()) == 0):
                showerror('Value Missing','Please Enter all the details')
            else :
                cur.execute('insert into run(b_id,running_date,seat_available) values(?,?,?)',(bus_id.get(),running_date.get(),seat_avail.get()))    
                st = str(bus_id.get())+' '+str(running_date.get())+' '+str(seat_avail.get())
                Label(frame1 , text = st).grid(row = 4,column=0,columnspan=10)
                con.commit()
            
        def delete():
            cur.execute('''delete from run where b_id=(?) and running_date=(?)''',(bus_id.get(),running_date.get()))
            con.commit()
         

            
        bus = PhotoImage(file = '.\\Bus_for_project.png')
        Label(root , image = bus).grid(row = 0,column = 0,columnspan = 35 , padx = w//3)
        Label(root , text = "Online Bus Booking System " , bg = 'lightblue' , fg = 'red' , font = 'Arial 18 bold').grid(row = 1,column = 0,columnspan = 35)
        Label(root , text = "Add Bus Running Details" , bg = 'lightgreen' , fg = 'green' , font = 'Arial 15 bold').grid(row = 2,column = 0,columnspan = 35 , pady = 40)


        frame1 = Frame(root)
        frame1.grid(row=3,column=0,columnspan=16,padx=200)
        Label(frame1 ,text="Bus ID" ,font='Arial 10 bold').grid(row=3,column=0,sticky=E)
        bus_id = Entry(frame1)
        bus_id.grid(row=3,column=1 ,sticky=W)
        Label(frame1,text="     Running Date",font='Arial 10 bold').grid(row=3,column=2,sticky=E)
        running_date = Entry(frame1)
        running_date.grid(row=3,column=3,sticky=W)        
        Label(frame1,text="     Seat Available",font='Arial 10 bold' ).grid(row=3,column=4,sticky=E)
        seat_avail = Entry(frame1)
        seat_avail.grid(row=3,column=5,sticky=W)
        Button(frame1,text="Add run",bg="light green",command = insert).grid(row=3,column=6,sticky=W , padx = 20)
        Button(frame1,text="delete run",bg="light green",command = delete).grid(row=3,column=7,sticky=W)

        def home(abhi=0):
            root.destroy()
            self.secondscreen()

            
        img_1 = PhotoImage(file=".\\home.png")
        Button(frame1,image=img_1,command=home).grid(row=3,column=8,sticky=W , padx = 20)
        root.mainloop()

 
text = abhikant()
text.firstscreen()


