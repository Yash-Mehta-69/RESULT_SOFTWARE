from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as con
from PIL import Image,ImageTk


root = Tk()
root.title("ZETA CORE")
root.state('zoomed')
root.configure(bg="#7395AE")
screenheight = root.winfo_screenheight()
screenwidth = root.winfo_screenwidth() 
# print(screenwidth,screenheight)
mydb = con.connect(host="localhost",user="root",password="yash1234",database="airport_school1")
cur = mydb.cursor()
signup=Frame(root,width=500,height=500,bg="#557A95")
signup.place(x=(screenwidth//2)-250,y=(screenheight//2)-250)






def admin_main():
    for widget in root.winfo_children():
        widget.destroy() 


    MENU_FRAME=Frame(root,relief=RIDGE,bg="lightblue",height=screenheight/8,width=screenwidth,borderwidth=5)
    MENU_FRAME.place(x=0,y=0)

    MAIN_FRAME=Frame(root,relief=RIDGE,bg="white",height=screenheight//1.5,width=screenwidth//1.25,borderwidth=4) 
    MAIN_FRAME.place(x=150,y=150)

    def add_teacher():
        print("add_teacher")

    def edit_teacher():
        print("edit_teacher")

    def update_year():
        print("update_year")

    def reports():
        print("reports")

    def approvals():

        class ApproveTable(Frame):
            def __init__(self, master, headings, data):
                super().__init__(master)
                self.master = master
                self.headings = headings
                self.data = data
                self.create_table()

            def create_table(self):



                if not self.data:
                    # If no data, display a message
                    empty_label = Label(self, text="No pending approvals", padx=10, pady=5)
                    empty_label.grid(row=0, column=0, columnspan=len(self.headings)+2, padx=5, pady=5)
                    return
                

                
                # Create heading labels
                for j, heading in enumerate(self.headings):
                    label = Label(self, text=heading, padx=10, pady=5, borderwidth=3, relief="solid", width=15)
                    label.grid(row=0, column=j, padx=5, pady=5)


                # Create data labels and buttons
                for i, row_data in enumerate(self.data):
                    for j, column_data in enumerate(row_data):
                        label = Label(self, text=column_data, padx=10, pady=5, borderwidth=1, relief="solid", width=15)
                        label.grid(row=i+1, column=j, padx=5, pady=5)

                    yes_button = Button(self, text="Yes", command=lambda i=i: self.approve(i, True), width=8)
                    yes_button.grid(row=i+1, column=len(row_data), padx=5, pady=5)

                    no_button = Button(self, text="No", command=lambda i=i: self.approve(i, False), width=8)
                    no_button.grid(row=i+1, column=len(row_data)+1, padx=5, pady=5)

            def approve(self, index, approval):
                if approval:
                    print(f"Approved: {self.data[index]}")
                    cur.execute("UPDATE teachers SET isApproved = 1 WHERE TID = {}".format(self.data[index][0]))
                    mydb.commit()
                else:
                    print(f"Not approved: {self.data[index]}")
                    cur.execute("delete from teachers WHERE TID = {}".format(self.data[index][0]))
                    mydb.commit()
                # Delete the row
                del self.data[index]
                self.refresh_table()

            def refresh_table(self):
                # Clear current widgets
                for widget in self.winfo_children():
                    widget.destroy()
                # Recreate the table with updated data
                self.create_table()


        sample_headings  = ["TID","TNAME","CLASS","YEAR","APPROVE","REJECT"]

        cur.execute("SELECT TID,TNAME,CLASS,YEAR FROM teachers WHERE isApproved = 0")
        non_approved_teachers = cur.fetchall()
        # print(non_approved_teachers)

        approve_table = ApproveTable(MAIN_FRAME, sample_headings, non_approved_teachers)
        approve_table.place(x=MAIN_FRAME.winfo_width()//6, y=10)



    image_teacher= Image.open(r"ICONS\teacher.png")
    image_teacher= image_teacher.resize((55,55))
    img_teacher= ImageTk.PhotoImage(image_teacher)
    teacher_BTN=Button(MENU_FRAME,image = img_teacher,bg='lightblue',compound=TOP,text="ADD TEACHER",command=add_teacher,padx=2,pady=2,activebackground='lightblue',relief=FLAT)
    teacher_BTN.place(x=100,y=5)

    image_edit= Image.open(r"ICONS\user.png")
    image_edit= image_edit.resize((55,55))
    img_edit= ImageTk.PhotoImage(image_edit)
    edit_BTN=Button(MENU_FRAME,image = img_edit,bg='lightblue',compound=TOP,text="EDIT TEACHER",command=edit_teacher,padx=2,pady=2,activebackground='lightblue',relief=FLAT)
    edit_BTN.place(x=250,y=5) 


    image_year= Image.open(r"ICONS\years.png")
    image_year= image_year.resize((55,55))
    img_year= ImageTk.PhotoImage(image_year)
    year_BTN=Button(MENU_FRAME,image = img_year,bg='lightblue',compound=TOP,text="UPDATE YEAR",command=update_year,padx=2,pady=2,activebackground='lightblue',relief=FLAT)
    year_BTN.place(x=400,y=5) 


    image_fees_report= Image.open(r"ICONS\report.png")
    image_fees_report= image_fees_report.resize((55,55))
    img_fees_report= ImageTk.PhotoImage(image_fees_report)
    FEES_REPORT_BTN=Button(MENU_FRAME,image = img_fees_report,bg='lightblue',compound=TOP,text="REPORTS",command=reports,padx=2,pady=2,activebackground='lightblue',relief=FLAT)
    FEES_REPORT_BTN.place(x=550,y=5) 

    image_fees_approve= Image.open(r"ICONS\approve.png")
    image_fees_approve= image_fees_approve.resize((55,55))
    img_fees_approve= ImageTk.PhotoImage(image_fees_approve)
    FEES_approve_BTN=Button(MENU_FRAME,image = img_fees_approve,bg='lightblue',compound=TOP,text="Pending Approvals",command=approvals,padx=2,pady=2,activebackground='lightblue',relief=FLAT)
    FEES_approve_BTN.place(x=700,y=5) 

    root.mainloop()




def teacher_main(user):
    print(user)





def teacher_login():
    signup = Frame(root, width=1000, height=500, bg="#B6D0E2")
    signup.place(x=(screenwidth // 2) - 500, y=(screenheight // 2) - 250)

    def sign_in():
        id1 = id_entry.get()
        password = code.get()
        year = clicked_year.get()

        cur.execute("select * from teachers where TID=%s and TPASS=%s and YEAR=%s", (id1, password, year))
        user = cur.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            if user[0] == '1' and user[2] == "Admin@321":
                admin_main()
            else:
                teacher_main(user)
        else:
            messagebox.showerror("ERROR", "Invalid Id Or Password")

    def on_enter(e):
        id_entry.delete(0, 'end')

    def on_leave(e):
        name = id_entry.get()
        if name == '':
            id_entry.insert(0, "ID")

    def on_enter_password(e):
        code.delete(0, 'end')

    def on_leave_password(e):
        name = code.get()
        if name == '':
            code.insert(0, "Password")

    bgmainteacher = PhotoImage(file="ICONS/banner.png")
    background_label = Label(signup, image=bgmainteacher)
    background_label.place(x=0, y=0)

    identify = Label(signup, text="Account Login", padx=5, pady=5, bg="white", fg="blue",
                     font=("Arial Rounded MT Bold", 20))
    identify.place(x=640, y=30)

    id_entry = Entry(signup, width=35, border=1, bg="#F0F0F0", fg="black", font=("Microsoft yaHei UI light", 11),
                     justify="center")
    id_entry.place(x=600, y=140)
    id_entry.insert(0, "ID")
    id_entry.bind("<FocusIn>", on_enter)
    id_entry.bind("<FocusOut>", on_leave)

    code = Entry(signup, width=35, border=1, bg="#F0F0F0", fg="black", font=("Microsoft yaHei UI light", 11),
                 justify="center")
    code.place(x=600, y=200)
    code.insert(0, "Password")
    code.bind("<FocusIn>", on_enter_password)
    code.bind("<FocusOut>", on_leave_password)

    clicked_year = StringVar()
    year_options = ["2021_22", "2022_23", "2023_24"]
    clicked_year.set(year_options[-1])  # default value

    YEAR_MENU = OptionMenu(signup, clicked_year, *year_options)
    YEAR_MENU.place(x=700, y=260)
    YEAR_MENU.configure(background='#F0F0F0', border=1)

    Button(signup, width=30, pady=7, text="Sign in", command=sign_in, bg='#F0F0F0', fg="black", cursor="hand2",
           border=0).place(x=630, y=320)

    root.mainloop()


teacher_login()




root.mainloop()
