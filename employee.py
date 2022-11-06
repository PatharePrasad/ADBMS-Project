from tkinter import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, Y, Button, Frame, Image, Label, LabelFrame, StringVar, Tk, messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
from dotenv import dotenv_values
from tkinter import messagebox
class Employee(Tk):
    config = dotenv_values(".env")

    def __init__(self):
        super().__init__()

        # Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        
        # Configuring the main window!
        self.title('Employee Management System')
        self.geometry("1530x790+0+0")
        
        # Adding label 
        self.label = Label(self, text="EMPLOYEE MANAGEMENT SYSTEM", font=('times new roman',37,'bold'),fg='cyan',bg='white')
        self.label.place(x=0,y=0,width=1530,height=50)

        # Preparing Image
        img_logo=Image.open('./images/empLogo.png')
        img_logo=img_logo.resize((50,50),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        # Placing Image
        self.labelImg = Label(image=self.photo_logo)
        self.labelImg.place(x=270, y=0, width=50, height=50)
        #Add Frame
        img_frame=Frame(self,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)
        
        # image 1  
        img1=Image.open('./images/pic1.png')
        img1=img1.resize((540,160),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.labelImg = Label(img_frame, image=self.photo1)
        self.labelImg.place(x=0, y=0, width=460, height=156)

        # image 2
        img2=Image.open('./images/pic2.png')
        img2=img2.resize((540,160),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.labelImg = Label(img_frame, image=self.photo2)
        self.labelImg.place(x=440, y=0, width=562, height=156)

        # image 3 
        img3=Image.open('./images/pic3.jpg')
        img3=img3.resize((540,160),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.labelImg = Label(img_frame, image=self.photo3)
        self.labelImg.place(x=1000, y=0, width=560, height=156)

        #Main Frame
        Main_frame=Frame(self,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)
 
        #upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white', text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text='Department',font=('aerial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('aerial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Depamrtment', 'HR', 'Software Engineer', 'Manager', 'Team Leader', 'Data Scientist')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Name
        lbl_Name=Label(upper_frame,font=("aerial",12,"bold"),text="Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("aerial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # lbl_Designition
        lbl_Designition=Label(upper_frame,font=("aerial",12,"bold"),text="Designition:",bg="white")
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=("aerial",11,"bold"))
        txt_Designition.grid(row=1,column=1,padx=2,pady=7)
        
        # Email
        lbl_Email=Label(upper_frame,font=("aerial",12,"bold"),text="Email:",bg="white")
        lbl_Email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_Email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("aerial",11,"bold"))
        txt_Email.grid(row=1,column=3,padx=2,pady=7)

        # Address
        lbl_address=Label(upper_frame,font=("aerial",12,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("aerial",11,"bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        # Married
        lbl_married_status=Label(upper_frame,text='Married Status',font=('aerial',12,'bold'),bg='white')
        lbl_married_status.grid(row=2,column=2,padx=2,sticky=W)

        combo_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('aerial',12,'bold'),width=18,state='readonly')
        combo_txt_married['value']=("Married", "Unmarried")
        combo_txt_married.current(0)
        combo_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        # DOB
        lbl_dob=Label(upper_frame,font=("aerial",12,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("aerial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        # DOJ
        lbl_doj=Label(upper_frame,font=("aerial",12,"bold"),text="DOJ:",bg="white")
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("aerial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        self.com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('aerial',12,'bold'),width=18,state='readonly')
        self.com_txt_proof['value']=("Select ID Proof", "PAN CARD", "AADHAR CARD", "DRIVING LICENCE")
        self.com_txt_proof.current(0)
        self.com_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        # ID Proof
        self.txt_proof=Label(upper_frame,textvariable=self.var_idproof,text='ID Proof',width=22,font=('aerial',12,'bold'),bg='white')
        self.txt_proof.grid(row=4,column=1,padx=2,pady=7)

        self.txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof, width=22,font=("aerial",11,"bold"))
        self.txt_proof.grid(row=4,column=1,padx=2,pady=7)

        # Gender
        lbl_gender=Label(upper_frame,text='Gender',font=('aerial',12,'bold'),bg='white')
        lbl_gender.grid(row=4,column=2,padx=2,sticky=W)

        combo_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('aerial',12,'bold'),width=18,state='readonly')
        combo_txt_gender['value']=("Male", "Female", "Other")
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        # Phone
        lbl_phone=Label(upper_frame,font=("aerial",12,"bold"),text="Phone:",bg="white")
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("aerial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        # Country
        lbl_country=Label(upper_frame,font=("aerial",12,"bold"),text="Country:",bg="white")
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("aerial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        # CTC
        lbl_ctc=Label(upper_frame,font=("aerial",12,"bold"),text="Salary(CTC):",bg="white")
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("aerial",11,"bold"))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

        #Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1290,y=10,width=170,height=210)

        btn_add=Button(button_frame,text="Save",command=self.add_data,font=("aerial",15,"bold"),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text="Update",command=self.update_data,font=("aerial",15,"bold"),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=("aerial",15,"bold"),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=("aerial",15,"bold"),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

        #down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white', text='Employee Information Table',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        #Search Frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white', text='Search Employee Information',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1470,height=60)

        Search_By=Label(search_frame,text='Search By:',font=('aerial',12,'bold'),bg='Red',fg='White')
        Search_By.grid(row=0,column=0,padx=5,sticky=W)

        # Search
        self.var_com_search=StringVar()
        combo_txt_searchby=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("aerial",12,"bold"),width=18)
        combo_txt_searchby['value']=("Select Option","Phone","id_Proof")
        combo_txt_searchby.current(0)
        combo_txt_searchby.grid(row=0,column=1,sticky=W,padx=5)
        self.var_search=StringVar()
        txt_searchby=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("aerial",11,"bold"))
        txt_searchby.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="Search",command=self.search_data,font=("aerial",11,"bold"),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame,text="Show All",command=self.fetch_data,font=("aerial",11,"bold"),width=14,bg='blue',fg='white')
        btn_ShowAll.grid(row=0,column=4,padx=5)

        # ============ Employee Table===========
        #Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=None)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("name",text="Name")
        self.employee_table.heading("degi",text="Designition")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("married",text="Marrried Status")
        self.employee_table.heading("dob",text="DOB")
        self.employee_table.heading("doj",text="DOJ")
        self.employee_table.heading("idproofcomb",text="ID Type")
        self.employee_table.heading("idproof",text="ID Proof")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("phone",text="Phone")
        self.employee_table.heading("country",text="Country")
        self.employee_table.heading("salary",text="Salary")

        self.employee_table['show']='headings'
        
        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("degi",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcomb",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #   *********** Function Declarations*****************
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=self.cursor()
                statement = f"""
                INSERT INTO employee 
                (Department, Name, Designition, Email, Address, Married_status, DOB, DOJ, id_proof_type, id_proof, Gender, Phone, Country, Salary)
                VALUES (
                    '{self.var_dep.get()}',
                    '{self.var_name.get()}',
                    '{self.var_designition.get()}',
                    '{self.var_email.get()}',
                    '{self.var_address.get()}',
                    '{self.var_married.get()}',
                    '{self.var_dob.get()}',
                    '{self.var_doj.get()}',
                    '{self.var_idproofcomb.get()}',
                    '{self.var_idproof.get()}',
                    '{self.var_gender.get()}',                                                                                              
                    '{self.var_phone.get()}',
                    '{self.var_country.get()}',
                    '{self.var_salary.get()}'
                );"""
                my_cursor=conn.cursor()
                my_cursor.execute(statement)
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo('success','Employee has been added!')
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}')     

    # fetch data
    def fetch_data(self):
        conn=self.cursor()
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    # Get cursor

    def get_cursor(self, event):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        # self.com_txt_proof.config(state= "disabled")
        self.var_idproof.set(data[9])
        # self.txt_proof.config(state= "disabled")
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this employee')
                if update>0:
                    conn=self.cursor()
                    statement = f"""
                    UPDATE employee
                    SET
                    Department='{self.var_dep.get()}', 
                    Name='{self.var_name.get()}',
                    Designition='{self.var_designition.get()}',
                    Email='{self.var_email.get()}',
                    Address='{self.var_address.get()}',
                    Married_status='{self.var_married.get()}',
                    DOB='{self.var_dob.get()}',
                    DOJ='{self.var_doj.get()}',
                    Gender='{self.var_gender.get()}',
                    Phone='{self.var_phone.get()}',
                    Country='{self.var_country.get()}',
                    Salary='{self.var_salary.get()}'
                    WHERE id_proof='{self.var_idproof.get()}'
                    ;"""
                    my_cursor=conn.cursor()
                    my_cursor.execute(statement)
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee Successfully Updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}')

    # Delete
    def delete_data(self):
        if self.var_idproof.get()=='':
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this employee')
                if Delete>0:
                    conn=self.cursor()
                    statement=f"DELETE FROM employee WHERE id_proof='{self.var_idproof.get()}';"
                    my_cursor=conn.cursor()
                    my_cursor.execute(statement)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Successfully Deleted')
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}')

    # reset 

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")


    # search 
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=self.cursor()
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee where '  +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                    conn.commit()
                    conn.close()
                else:
                    messagebox.showerror('404','Record not found!')
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}')

    def cursor(self):
        return mysql.connector.connect(host=self.config['DB_HOST'],username=self.config['DB_USERNAME'],password=self.config['DB_PASSWORD'],database=self.config['DB_NAME'])
    




if __name__=="__main__":
    app = Employee()
    app.mainloop()
    