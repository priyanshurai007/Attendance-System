from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="Developer",font=("times new roman", 35,"bold"),bg="white", fg="red" )
        title_lbl.place(x=0,y=0,width=1530,height=50)

        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=55,width=500,height=600)

        img_top1=Image.open(r"college_images\finalgp.jpeg")
        img_top1=img_top1.resize((500,600),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=0,y=0,width=500,height=600)

        





if __name__=="__main__":
        root=Tk()
        obj=Developer(root)
        root.mainloop()
