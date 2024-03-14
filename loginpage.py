from tkinter import *
from tkinter import messagebox
import mysql.connector as con
import tkinter as tk



root = Tk()
root.title("ZETA CORE")
root.state('zoomed')
root.configure(bg="#000000")
screenwidth = root.winfo_screenwidth() 
screenheight = root.winfo_screenheight()
print(screenwidth,screenheight)
mydb = con.connect(host="localhost",user="root",password="India5254",database="report_system")
cur = mydb.cursor()
signup=Frame(root,width=500,height=500,bg="#C5C5C5")
signup.place(x=(screenwidth//2)-250,y=(screenheight//2)-250)
bgmainteacher = PhotoImage(file ="C://Users//Admin//OneDrive//Desktop//school2//banner.pNg")






def admin_main():
    print("aaaa")



def teacher_main(user):
    print(user)

    this_class = user[2]
    this_year = user[3]

    cur.execute("show tables")
    tables = cur.fetchall()
    # print(tables)
    table_flag = False
    for i in tables:
        if i[0] == "{}_{}".format(this_class,this_year):
            table_flag = True
        
    if table_flag==False:
        print("Table Not Exists")
        messagebox.showerror("Error","Sorry, We dont have the students data!")
    else:
        print("Table Exists")
        # print(this_year,this_exam,this_class)
        cur.execute("select * from {}_{}".format(this_class,this_year))
        students_data = cur.fetchall()
        total_strength = len(students_data)
        print(total_strength)
        print(students_data)

        for widget in signup.winfo_children():
            widget.destroy() 

        signup.configure(width=700)
        signup.place_configure(x=400)
        identify = Label(signup, text = "ENTERING MARKS FOR", padx=5, pady=5, bg="#557A95", font=("Arial Rounded MT Bold",20))
        identify.place(x=175,y=50)

        identify_1 = Label(signup, text = "CLASS : {}".format(user[2]), padx=5, pady=5, bg="#557A95", font=("Arial Rounded MT Bold",20))
        identify_1.place(x=250,y=125)

        clicked_exam = StringVar() 
        exam_options = ["PT 1", "PT 2", "HALF YEARLY", "FINAL EXAMS"]
        clicked_exam.set(exam_options[0]) # default value
        exam_MENU = OptionMenu(signup, clicked_exam, *exam_options)
        exam_MENU.place(x=280,y=300)

        this_exam = clicked_exam.get()

        def ENTER_MARKS():
            for widget in root.winfo_children():
                widget.destroy()


        ENTER_BTN = Button(signup,width=20,pady=7,text="Enter ->",command=ENTER_MARKS,bg='#57a1f8',fg="white",cursor="hand2",border=0)
        ENTER_BTN.place(x=250,y=375)
    

    




def teacher_login():
    signup=Frame(root,width=1000,height=500,bg="#B6D0E2")
    signup.place(x=(screenwidth//2)-500,y=(screenheight//2)-250)
    
    def sign_in():
        id1=id_entry.get()
        password=code.get()
        year = clicked_year.get()
        print(id1,password,year)

        cur.execute("select * from logins where id=%s and password=%s and year=%s",(id1,password,year))
        user = cur.fetchone()
        print(user)
        if user:
            messagebox.showinfo("Success", "Login successful!")
            teacher_main(user)
        else : 
            messagebox.showerror("ERROR","Invalid Id Or Password")

    def on_enter(e):
        id_entry.delete(0,'end')
    def on_leave(e):
        name=id_entry.get()
        if name=='':
            id_entry.insert(0,"id")

    background_label = tk.Label(signup, image=bgmainteacher)
    background_label.place(x=0,y=0)

    identify = Label(signup, text = "Account Login", padx=5, pady=5, bg="white", fg="blue", font=("Arial Rounded MT Bold",20))
    identify.place(x=640,y=30)

    id_entry=Entry(signup,width=35,border=1,bg="#F0F0F0", fg="black",font=("Microsoft yaHei UI light",11),justify="center")
    id_entry.place(x=600,y=140)
    id_entry.insert(0,"ID")
    id_entry.bind("<FocusIn>",on_enter)
    id_entry.bind("<FocusOut>",on_leave)
   

    def on_enter(e):
            code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,"Password")

    code=Entry(signup,width=35,border=1,bg="#F0F0F0", fg="black",font=("Microsoft yaHei UI light",11),justify="center")
    code.place(x=600,y=200)
    code.insert(0,"Password")
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)
   

    clicked_year = StringVar() 
    year_options = ["2021_22","2022_23","2023_24"]
    clicked_year.set(year_options[-1]) # default value
    
    YEAR_MENU = OptionMenu(signup, clicked_year, *year_options)
    YEAR_MENU.place(x=700,y=260)
    YEAR_MENU.configure(background='#F0F0F0',border=1)

    Button(signup,width=30,pady=7,text="Sign in",command=sign_in,bg='#F0F0F0',fg="black",cursor="hand2",border=0).place(x=630,y=320)
    


teacher_login()



root.mainloop()
