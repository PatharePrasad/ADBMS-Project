from tkinter import RIDGE, W, Frame, Image, Label, Tk
from PIL import Image, ImageTk
class Employee(Tk):
    def __init__(self):
        super().__init__()
        
        # Configuring the main window!
        self.title('Employee Management System')
        self.geometry("1530x790+0+0")
        
        # Adding label 
        self.label = Label(self, text="EMPLOYEE MANAGEMENT SYSTEM", font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        self.label.place(x=0,y=0,width=1530,height=50)

        # Preparing Image
        img_logo=Image.open('./images/empLogo.png')
        img_logo=img_logo.resize((50,50),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        # Placing Image
        self.labelImg = Label(image=self.photo_logo)
        self.labelImg.place(x=0, y=60)
        # Why to use this?
        # img_frame=Frame(self,bd=2,relief=RIDGE,bg='white')
        # img_frame.place(x=0,y=50,width=1530,height=160)


if __name__=="__main__":
    app = Employee()
    app.mainloop()
    