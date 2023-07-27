from tkinter import* 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
     

     
     


 #======variable======
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        img=Image.open(r"D:\Projects\Final Year Project (Face detection attendance system)\college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)

        img1=Image.open(r"D:\Projects\Final Year Project (Face detection attendance system)\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=510,height=130)


        img2=Image.open(r"D:\Projects\Final Year Project (Face detection attendance system)\college_images\face_detector1.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=510,height=130)



        #b_g img

        img3=Image.open(r"D:\Projects\Final Year Project (Face detection attendance system)\college_images\bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

       

        #title

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman", 28,"bold"),bg="white", fg="red" )
        title_lbl.place(x=0,y=0,width=1530,height=50)
       
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580) 

        img_left=Image.open(r"D:\Projects\Final Year Project (Face detection attendance system)\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        #current course information

        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=120) 
    
        #department

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_combo['values']=("Select Department","Computer Science", "IT","CIVIL", "MECHANICAL", "ELECTRICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course

        course_label=Label(current_course_frame,text="Courses",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo['values']=("Select Course","BCA", "B-Tech", "B-Pharma", "MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
       
        #year

        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo['values']=("Select Year","2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester

        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        semester_combo['values']=("Select Semester","First", "Second", "Third", "Fourth","Fifth","Sixth","Seventh","Eight")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information

        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=260,width=720,height=310) 

        #studentid

        studentID_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"))
        studentID_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)  
        

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #studentname

        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)  
        

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #Rollno.

        rollNo_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"))
        rollNo_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)  
        

        rollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rollNo_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #ClassDivision

        classDivision_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"))
        classDivision_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)  
        

        #classDivision_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        #classDivision_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo['values']=("A","B", "C")
        div_combo.current(0)
        div_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)

        #gender

        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)  
        

        #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo['values']=("Male","Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)

        #Dob

        dob_label=Label(class_student_frame,text="Date of Birth:",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)  
        

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Email

        #email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"))
        #email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)  
        

        #email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        #email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)




# Define a regular expression pattern for a valid email address
        EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# Create a validation function to check if the entered email address is valid
        def validate_email():
         email = self.var_email.get()
         if email == "":
          return True
         if re.match(EMAIL_PATTERN, email):
          return True
         else:
           messagebox.showerror("Error", "Please enter a valid email address.")
           return False

# Create a function to bind to the email_entry widget for when the focus is lost
        def on_email_focusout(event):
         validate_email()

# Create the email_label widget
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)  

# Create the email_entry widget
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        email_entry.bind("<FocusOut>", on_email_focusout)

       




        #Phone No

        phoneNo_label=Label(class_student_frame,text="Phone NO:",font=("times new roman",12,"bold"))
        phoneNo_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)  
        

        def validate_phone_number(new_value):
          return len(new_value) <= 10

        phoneNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"), validate="key")
        phoneNo_entry['validatecommand'] = (phoneNo_entry.register(validate_phone_number), '%P')
        phoneNo_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)



        #phoneNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        #phoneNo_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6,column=0,padx=10)


        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=6,column=1,padx=10)

        #button frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=210,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        

        #update
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #delete
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn2_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn2_frame.place(x=0,y=245,width=715,height=35)


        take_photo_btn=Button(btn2_frame,text="Take Sample Photo",command=self.generate_dataset,width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        

        update_photo_btn=Button(btn2_frame,text="Update Sample Photo",width=37,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        
        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=800,y=10,width=660,height=580) 

        img_right=Image.open(r"D:\Projects\Final Year Project (Face detection attendance system)\college_images\smart-attendance.jpg")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #=======Search System=============

        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=650,height=70)
        
        
        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)  

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo['values']=("Select","Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        search_btn=Button(search_frame,text="Search",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)


        showAll_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5)


        #table frame



        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #======function declaration====
    def add_data(self):
         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error", "All Fields are required",parent=self.root)

         else: 
             try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Saroj@0003",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()

                                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student Details Added",parent=self.root)
             except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
#===============fetch data=========== 
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Saroj@0003",database="face_recognizer")
            my_cursor=conn.cursor()    
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()

         
 #===========get cursor=========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        
        self.var_dep.set(data[0]),
        
        self.var_course.set(data[1]) ,
      
        self.var_year.set(data[2]), 
       
        self.var_semester.set(data[3]),
        
        self.var_std_id.set(data[4]), 
       
        self.var_std_name.set(data[5]), 
        
        self.var_div.set(data[6]),  
        
        self.var_roll.set(data[7]),
     
        self.var_gender.set(data[8]), 
       
        self.var_dob.set(data[9]), 
        
        self.var_email.set(data[10]), 
        
        self.var_phone.set(data[11]),
       
        self.var_address.set(data[12]), 
       
        self.var_teacher.set(data[13]), 
        
        self.var_radio1.set(data[14]) 

#==========update function==========
    def update_data(self):
               if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                    messagebox.showerror("Error", "All Fields are required",parent=self.root)
               else:
                try:  
                    Update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                    if Update>0:
                              conn=mysql.connector.connect(host="localhost",username="root",password="Saroj@0003",database="face_recognizer")
                              my_cursor=conn.cursor()
                             # my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s,",(
                              my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                           

                                                                                                              self.var_dep.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              
                                                                                                              self.var_std_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_teacher.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                              self.var_std_id.get()                  
                                                                                                                                                                     
                                                                                                                                                                     
                                                                                                              ))
                    else :
                         if not Update:
                              return
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
     

               

#========delete function======
 
    def delete_data(self):
     if self.var_std_id.get()=="":
          messagebox.showerror("Error","Student ID Must Required",parent=self.root)
     else:
            try:
               delete=messagebox.askyesno("Student Delete Report", "Do you want to delete this student",parent=self.root)
               if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Saroj@0003",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
               else:
                    if not delete:
                         return
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#=======reset======
    def reset_data(self):
         self.var_dep.set("Select Department")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select Semester")
         self.var_std_id.set("")
         self.var_std_name.set("")
         self.var_div.set("Select Division")
         self.var_roll.set("")
         self.var_gender.set("Select Gender")
         self.var_dob.set("")
         self.var_email.set("")
         self.var_phone.set("")
         self.var_address.set("")
         self.var_teacher.set("")
         self.var_radio1.set("")


 #================Generate data set or Take Photo Sample===============

    def generate_dataset(self):
         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                    messagebox.showerror("Error", "All Fields are required",parent=self.root)
         else:
             try:   
                 conn=mysql.connector.connect(host="localhost",username="root",password="Saroj@0003",database="face_recognizer")
                 my_cursor=conn.cursor()
                 my_cursor.execute("select * from student")
                 myresult=my_cursor.fetchall()
                 id=0
                 for x in myresult:
                      id+=1
                 my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                           

                                                                                                              self.var_dep.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              
                                                                                                              self.var_std_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_teacher.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                              self.var_std_id.get()==id+1                  
                                                                                                                                                                     
                                                                                                                                                            
                                                                                                              ))
                 conn.commit()
                 self.fetch_data()
                 self.reset_data()
                 conn.close()

                 #========Load predifend data on face frontals fro op[encv]=====

                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                 def face_cropped(img):
                      gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                      faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                      #scaling factor=1.3
                      #Minimum neigbour =5

                      for(x,y,w,h) in faces:
                           face_cropped=img[y:y+h,x:x+w]
                           return face_cropped
                      
                 cap=cv2.VideoCapture(0)
                 img_id=0
                 while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                              img_id+=1
                              face=cv2.resize(face_cropped(my_frame),(450,450))
                              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                              file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                              cv2.imwrite(file_name_path,face)
                              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                              cv2.imshow("CROPPED FACE", face)



                    if cv2.waitKey(1)==13 or int(img_id)==100:
                           break
                 cap.release()
                 cv2.destroyAllWindows()   
                 messagebox.showinfo("Result","Generating Data Set Completed")  


             except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)








                    
          
                   
              
  
if __name__=="__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()
