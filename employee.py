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
        Main_frame.place(x=10,y=210,width=1500,height=560)

if __name__=="__main__":
    app = Employee()
    app.mainloop()
    