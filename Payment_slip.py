from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class PaymentSlip:
    def __init__(self, root):
        self.root = root
        root.title("Employee Payroll System")
        self.root.geometry("1920x1080+0+0")

        # Variables
        self.name = StringVar()
        self.address = StringVar()
        self.department = StringVar()
        self.employee_id = StringVar()
        self.hours_worked = StringVar()
        self.hourly_rate = StringVar()
        self.tax= StringVar()
        self.over_time = StringVar()
        self.gross_pay = StringVar()
        self.net_pay = StringVar()
        self.date_var=StringVar()
        d1 = datetime.datetime.today().strftime("%d-%m-%Y")
        self.date_var.set(d1)
        
        

        # Title label
        labeltitle = Label(self.root, text="Payment Slip Software", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("Times New Roman", 50, "bold"), padx=2, pady=6)
        labeltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # Data frame left
        DataFrameLeft = LabelFrame(frame, text="Employee Payment Slip", bg="powder blue", fg="green", bd=12, relief=RIDGE, font=("Times New Roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=365)

        lblmember = Label(DataFrameLeft, bg="powder blue", text="Employee Name :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblmember.grid(row=0, column=0, sticky=W)
        txtmember = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.name,width=28)
        txtmember.grid(row=0, column=1, padx=2, pady=6)

        lbladdress = Label(DataFrameLeft, bg="powder blue", text="Address :", font=("arial", 13, "bold"), padx=2, pady=6)
        lbladdress.grid(row=1, column=0, sticky=W)
        txtaddress = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address,width=28)
        txtaddress.grid(row=1, column=1, padx=2, pady=6)

        lbldept = Label(DataFrameLeft, bg="powder blue", text="Department :", font=("arial", 13, "bold"), padx=2, pady=6)
        lbldept.grid(row=2, column=0, sticky=W)  
        txtdept = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.department, width=28)
        txtdept.grid(row=2, column=1, padx=2, pady=6)  

        lbleid = Label(DataFrameLeft, bg="powder blue", text="Employee ID :", font=("arial", 13, "bold"), padx=2, pady=6)
        lbleid.grid(row=3, column=0, sticky=W)  
        txteid = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.employee_id,width=28)
        txteid.grid(row=3, column=1, padx=2, pady=6)

        lbldate = Label(DataFrameLeft, bg="powder blue", text="Date :", font=("arial", 13, "bold"), padx=2, pady=6)
        lbldate.grid(row=4, column=0, sticky=W)  
        txtdate = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.date_var, width=28)
        txtdate.grid(row=4, column=1, padx=2, pady=6)

        lblhrsworked = Label(DataFrameLeft, bg="powder blue", text="Hours Worked :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblhrsworked.grid(row=5, column=0, sticky=W)  
        txlhrsworked = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.hours_worked,width=28)
        txlhrsworked.grid(row=5, column=1, padx=2, pady=6)

        lblhrsrate = Label(DataFrameLeft, bg="powder blue", text="Hourly Rate :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblhrsrate.grid(row=6, column=0, sticky=W)  
        txthrsrate = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.hourly_rate, width=28)
        txthrsrate.grid(row=6, column=1, padx=2, pady=6)

        lbltax = Label(DataFrameLeft, bg="powder blue", text="Tax :", font=("arial", 13, "bold"), padx=2, pady=6)
        lbltax.grid(row=7, column=0, sticky=W)  
        lbltax = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.tax, width=28)
        lbltax.grid(row=7, column=1, padx=2, pady=6)

        lblovrtime = Label(DataFrameLeft, bg="powder blue", text="Over Time :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblovrtime.grid(row=8, column=0, sticky=W)  
        lblovrtime = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.over_time, width=28)
        lblovrtime.grid(row=8, column=1, padx=2, pady=6)

        lblgpay = Label(DataFrameLeft, bg="powder blue", text="Gross Pay :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblgpay.grid(row=0, column=2, sticky=W)  
        lblgpay = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.gross_pay, width=28)
        lblgpay.grid(row=0, column=3, padx=2, pady=6)

        lblnpay = Label(DataFrameLeft, bg="powder blue", text="Net pay :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblnpay.grid(row=1, column=2, sticky=W)
        txtnpay = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.net_pay, width=28)
        txtnpay.grid(row=1, column=3, padx=2, pady=6)

        # Dataframe right
        # Single TextBox with Scrollbar
        DataFrameRight = LabelFrame(frame, bd=12, padx=20, relief=RIDGE, bg="powder blue", fg="green",
                                    font=("Times New Roman", 12, "bold"), text="Payment Slip")
        DataFrameRight.place(x=870, y=5, width=580, height=365)

        

        # Scrollbar
        TextScrollbar = Scrollbar(DataFrameRight, orient="vertical")
        TextScrollbar.pack(side=RIGHT, fill=Y)

        # TextBox
        self.txtbox = Text(DataFrameRight, font=("Times New Roman", 12, "bold"), width=70, height=16,
                           padx=2, pady=6, yscrollcommand=TextScrollbar.set, wrap=WORD)
        self.txtbox.pack(side=LEFT, fill=BOTH, expand=True)

        # Connect Scrollbar to TextBox
        TextScrollbar.config(command=self.txtbox.yview)


        # Buttons
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnadddata=Button(Framebutton,command=self.monthly_wages,text="Total Salary",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=0)

        btnadddata=Button(Framebutton,command=self.add_data,text="Add Member",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=1)

        
        btnadddata=Button(Framebutton,command=self.view_payslip,text="View Payslip",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=2)

        btnadddata=Button(Framebutton,command=self.delete,text="Delete",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=3)

        btnadddata=Button(Framebutton,command=self.reset,text="Reset",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=4)

        btnadddata=Button(Framebutton,command=self.exit_system,text="Exit System",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=5)

        # Frame

        Frameinfo = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Frameinfo.place(x=0, y=600, width=1530, height=210)

        # Data Table
        Table_frame = Frame(Frameinfo, bd=6, relief="ridge", bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=180)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.payment_slip=ttk.Treeview(Table_frame,column=("employeename","address","department","employeeid","date","hoursworked","hourlyrate","tax","overtime","grosspay","netpay"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.payment_slip.xview)
        yscroll.config(command=self.payment_slip.yview)

        self.payment_slip.heading("employeename",text="Employee Name")
        self.payment_slip.heading("address",text="Address")
        self.payment_slip.heading("department",text="Department")
        self.payment_slip.heading("employeeid",text="Employee ID")
        self.payment_slip.heading("date",text="Date")
        self.payment_slip.heading("hoursworked",text="Hours Worked")
        self.payment_slip.heading("hourlyrate",text="Hourly Rate")
        self.payment_slip.heading("tax",text="Tax")
        self.payment_slip.heading("overtime",text="Over Time")
        self.payment_slip.heading("grosspay",text="Gross Pay")
        self.payment_slip.heading("netpay",text="Net Pay")

        self.payment_slip["show"]="headings"
        self.payment_slip.pack(fill=BOTH,expand=1)

        self.payment_slip.column("employeename",width=100)
        self.payment_slip.column("address",width=100)
        self.payment_slip.column("department",width=100)
        self.payment_slip.column("employeeid",width=100)
        self.payment_slip.column("date",width=100)
        self.payment_slip.column("hoursworked",width=100)
        self.payment_slip.column("hourlyrate",width=100)
        self.payment_slip.column("tax",width=100)
        self.payment_slip.column("overtime",width=100)
        self.payment_slip.column("grosspay",width=100)
        self.payment_slip.column("netpay",width=100)
        self.fetch_data()

    def add_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vishal@123",
                database="vishal",
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO payment_slip VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
                (
                    self.name.get(),
                    self.address.get(),
                    self.department.get(),
                    self.employee_id.get(),
                    self.date_var.get(),
                    self.hours_worked.get(),
                    self.hourly_rate.get(),
                    self.tax.get(),
                    self.over_time.get(),
                    self.gross_pay.get(),
                    self.net_pay.get(),
                ),
            )

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Data has been inserted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

    def fetch_data(self):
      self.payment_slip.bind("<ButtonRelease-1>",self.get_cursor)
      # try:
      conn = mysql.connector.connect(
          host="localhost",
          username="root",
          password="Vishal@123",
          database="vishal",
        )
      my_cursor = conn.cursor()
      my_cursor.execute("select * from payment_slip")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
              self.payment_slip.delete(*self.payment_slip.get_children())
              for i in rows:
                self.payment_slip.insert("",END,values=i)
              conn.commit()
      conn.close()

    def get_cursor(self,event):
      cursor_row=self.payment_slip.focus()
      content=self.payment_slip.item(cursor_row)
      row=content["values"]

      self.name.set(row[0]),
      self.address.set(row[1]),
      self.department.set(row[2]),
      self.employee_id.set(row[3]),
      self.date_var.set(row[4]),
      self.hours_worked.set(row[5]),
      self.hourly_rate.set(row[6]),
      self.tax.set(row[7]),
      self.over_time.set(row[8]),
      self.gross_pay.set(row[9]),
      self.net_pay.set(row[10])

    # Functions
    def reset(self):
        self.name.set("")
        self.address.set("")
        self.department.set("")
        self.employee_id.set("")
        self.date_var.set("")
        self.hours_worked.set("")
        self.hourly_rate.set("")
        self.tax.set("")
        self.over_time.set("")
        self.gross_pay.set("")
        self.net_pay.set("")

    def view_payslip(self):
        self.welcome_soft()
        self.txtbox.insert(END, "Employee Name :\t\t"+self.name.get()+"\n")
        self.txtbox.insert(END, "Employee ID :\t\t"+self.employee_id.get()+"\n")
        self.txtbox.insert(END, "Department :\t\t"+self.department.get()+"\n")
        self.txtbox.insert(END, "Address :\t\t"+self.address.get()+"\n")
        self.txtbox.insert(END, "Date :\t\t"+self.date_var.get()+"\n")
        self.txtbox.insert(END, "Hours Worked :\t\t"+self.hours_worked.get()+"\n")
        self.txtbox.insert(END, "Hourly Rate :\t\t"+self.hourly_rate.get()+"\n")
        self.txtbox.insert(END, "Tax :\t\t"+self.tax.get()+"\n")
        self.txtbox.insert(END, "Over Time :\t\t"+self.over_time.get()+"\n")
        self.txtbox.insert(END, "Gross Pay :\t\t"+self.gross_pay.get()+"\n")
        self.txtbox.insert(END, "Net Pay :\t\t"+self.net_pay.get()+"\n")

    def monthly_wages(self):
        try:
        # Retrieve and validate input
            hours_worked = self.hours_worked.get()
            hourly_rate = self.hourly_rate.get()

            if not hours_worked or not hourly_rate:
                raise ValueError("Inputs cannot be empty.")

            hours = float(hours_worked) * 4
            rate = float(hourly_rate)

            if hours < 0 or rate < 0:
                raise ValueError("Hours worked and hourly rate must be positive numbers.")

        # Calculate gross pay
            gross_pay = hours * rate
            self.gross_pay.set("INR {:.2f}".format(gross_pay))

        # Calculate tax (20% of gross pay)
            tax = gross_pay * 0.2
            self.tax.set("INR {:.2f}".format(tax))

        # Calculate net pay
            net_pay = gross_pay - tax
            self.net_pay.set("INR {:.2f}".format(net_pay))

        # Calculate overtime pay if applicable
            if hours > 160:
                overtime_hours = hours - 160
                overtime = overtime_hours * (rate * 1.5)
                self.over_time.set("INR {:.2f}".format(overtime))
            else:
                self.over_time.set("INR 0.00")

        except ValueError as e:
         messagebox.showerror("Input Error", str(e))
        except Exception:
         messagebox.showerror("Unexpected Error", "An error occurred while calculating wages.")



    def welcome_soft(self):
        self.txtbox.delete('1.0',END)
        self.txtbox.insert(END,"                                        Welcome To Our Company\n")
        self.txtbox.insert(END,"                                        Landran Road, Punjab, India \n")
        self.txtbox.insert(END,"\nwww.ourcompany.org.in                                                       +91 88800 88800")
        self.txtbox.insert(END,"\n======================================================\n")
        self.txtbox.insert(END,"                                              Employee Payslip")
        self.txtbox.insert(END,"\n======================================================\n")

    def exit_system(self):
        if messagebox.askyesno("Employee System", "Do you want to exit the system?"):
            self.root.destroy()

    def delete(self):
      if self.employee_id.get() == "" or self.name.get() == "":
        messagebox.showerror("Error", "First select the Member for delete")
      else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vishal@123",
                database="vishal",
            )
            my_cursor = conn.cursor()
            query = "DELETE FROM payment_slip WHERE `Employee ID` = %s"
            value = (self.employee_id.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            self.reset()
            
            messagebox.showinfo("Success", "Member has been deleted")
        
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", "Error: " + str(err))
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred: " + str(e))
        
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

if __name__ == "__main__":
    root = Tk()
    app = PaymentSlip(root)
    root.mainloop()
