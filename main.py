from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter




class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

      

        #img=Image.open(r"college_images\BestFacialRecognition.jpg")
        img=Image.open("college_images/BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)

        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=510,height=130)


        img2=Image.open(r"college_images\face_detector1.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=510,height=130)



        #b_g img

        img3=Image.open(r"college_images\bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #Title

        title_lbl=Label(bg_img,text="STUDENT ATTENDANCE SYSTEM SOFTWARE",font=("times new roman", 35,"bold"),bg="white", fg="red" )
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
       
        #STUDENT_BUTTON

        img4=Image.open(r"college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100, width=220,height=220)


        b1_1=Button(bg_img,text="Student Detail",command=self.student_details,cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
        b1_1.place(x=200,y=300, width=220,height=40)  
        


        #DETECTFACE_BUTTON

        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100, width=220,height=220)


        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman", 15,"bold"),bg="blue", fg="white")
        b1_1.place(x=500,y=300, width=220,height=40)  


        #Attendance face button

        img6=Image.open(r"college_images\report.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100, width=220,height=220)


        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 15,"bold"),bg="blue", fg="white")
        b1_1.place(x=800,y=300, width=220,height=40)  


        #Help button

        img7=Image.open(r"college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help_desk,cursor="hand2")
        b1.place(x=1100,y=100, width=220,height=220)


        b1_1=Button(bg_img,text="Help_Desk",command=self.help_desk,cursor="hand2",font=("times new roman", 15,"bold"),bg="blue", fg="white")
        b1_1.place(x=1100,y=300, width=220,height=40)  
    
   

         #Train data button

        img8=Image.open(r"college_images\Train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380, width=220,height=220)


        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman", 15,"bold"),bg="blue", fg="white")
        b1_1.place(x=200,y=580, width=220,height=40)  


      
         #Photo button

        img9=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380, width=220,height=220)


        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 15,"bold"),bg="blue", fg="white")
        b1_1.place(x=500,y=580, width=220,height=40)    


         #Developer button

        img10=Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b1.place(x=800,y=380, width=220,height=220)


        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman", 15,"bold"),bg="blue", fg="white")
        b1_1.place(x=800,y=580, width=220,height=40)    

        #Exit button

        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b1.place(x=1100,y=380, width=220,height=220)


        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman", 15,"bold"),bg="blue", fg="white")
        b1_1.place(x=1100,y=580, width=220,height=40)    


    def open_img(self):
          os.startfile("Data")

    def iexit(self):
            self.iexit=tkinter.messagebox.askyesno("Attendance System", "Are you sure you want to exit",parent=self.root)
            if self.iexit>0:
                    self.root.destroy()

            else: return


          #============functions======
    def student_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Student(self.new_window)

    def train_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Train(self.new_window)

    def face_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Attendance(self.new_window)

    def developer_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Developer(self.new_window)

    def help_desk(self):
                self.new_window=Toplevel(self.root)
                self.app=Help(self.new_window)
    




if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()
        
   
