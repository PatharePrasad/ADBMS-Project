from tkinter import Label, Tk
<<<<<<< HEAD


class Employee(Tk):
    def __init__(self):
        super().__init__()

        # Configuring the main window!
        self.title('Employee Management System')
        self.geometry("1530x790+0+0")

        # Adding label 
        self.label = Label(self, text="EMPLOYEE MANAGEMENT SYSTEM", font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        self.label.place(x=0,y=0,width=1530,height=50)

=======
>>>>>>> 60928afc0d9f0984216339cdf125db2fcdc924e3


class Employee(Tk):
    def __init__(self):
        super().__init__()
        
        # Configuring the main window!
        self.title('Employee Management System')
        self.geometry("1530x790+0+0")
        
        # Adding label 
        self.label = Label(self, text="EMPLOYEE MANAGEMENT SYSTEM", font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        self.label.place(x=0,y=0,width=1530,height=50)


if __name__=="__main__":
<<<<<<< HEAD
        app = Employee()
        app.mainloop()

=======
    app = Employee()
    app.mainloop()
>>>>>>> 60928afc0d9f0984216339cdf125db2fcdc924e3
