from tkinter import RIDGE, Frame, Label, Tk


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
    app = Employee()
    app.mainloop()

#Adding Borders
    img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
    img_frame.place(x=0,y=50,width=1530,height=160)
