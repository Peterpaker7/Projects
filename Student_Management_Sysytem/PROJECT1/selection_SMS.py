from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

#functionality part

def iexit():
    result=messagebox.askyesno('Confirm','Do You want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)
    table=pandas.DataFrame(newlist,columns=['Id','Name','Std','Gender','DOB','Mobileno','email','Addhar','Address','Date','Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Sucess','Data Saved Sucessfully')


def toplevel_data(title,button_text,command):
    global idEntry,nameEntry,stdEntry,genderEntry,DOBEntry,mobileEntry,emailEntry,addhaarEntry,addressEntry,screen_window
    screen_window=Toplevel()
    screen_window.title(title)
    screen_window.grab_set()
    screen_window.resizable(False,False)
    idLabel=Label(screen_window,text='Admission ID',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,pady=15,padx=30,sticky=W)
    idEntry=Entry(screen_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel=Label(screen_window,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,pady=15,padx=30,sticky=W)
    nameEntry=Entry(screen_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    stdLabel=Label(screen_window,text='Standard',font=('times new roman',20,'bold'))
    stdLabel.grid(row=2,column=0,pady=15,padx=30,sticky=W)
    stdEntry=Entry(screen_window,font=('roman',15,'bold'),width=24)
    stdEntry.grid(row=2,column=1,pady=15,padx=10)

    genderLabel=Label(screen_window,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=3,column=0,pady=15,padx=30,sticky=W)
    genderEntry=Entry(screen_window,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=3,column=1,pady=15,padx=10)

    DOBLabel=Label(screen_window,text='D.O.B',font=('times new roman',20,'bold'))
    DOBLabel.grid(row=4,column=0,pady=15,padx=30,sticky=W)
    DOBEntry=Entry(screen_window,font=('roman',15,'bold'),width=24)
    DOBEntry.grid(row=4,column=1,pady=15,padx=10)

    mobileLabel=Label(screen_window,text='Mobile No',font=('times new roman',20,'bold'))
    mobileLabel.grid(row=5,column=0,pady=15,padx=30,sticky=W)
    mobileEntry=Entry(screen_window,font=('roman',15,'bold'),width=24)
    mobileEntry.grid(row=5,column=1,pady=15,padx=10)

    emailLabel=Label(screen_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=6,column=0,pady=15,padx=30,sticky=W)
    emailEntry=Entry(screen_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=6,column=1,pady=15,padx=10)
    
    addhaarLabel=Label(screen_window,text='Addhaar',font=('times new roman',20,'bold'))
    addhaarLabel.grid(row=7,column=0,pady=15,padx=30,sticky=W)
    addhaarEntry=Entry(screen_window,font=('roman',15,'bold'),width=24)
    addhaarEntry.grid(row=7,column=1,pady=15,padx=10)


    addressLabel=Label(screen_window,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=8,column=0,pady=15,padx=30,sticky=W)
    addressEntry=Entry(screen_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=8,column=1,pady=15,padx=10)
    

    student_button=ttk.Button(screen_window,text=button_text,command=command)
    student_button.grid(row=9,columnspan=2,pady=15)

    if title=='Update Student':

        indexing=studentTable.focus()
        content=studentTable.item(indexing)
        listData=content['values']
        idEntry.insert(0,listData[0])
        nameEntry.insert(0,listData[1])
        stdEntry.insert(0,listData[2])
        genderEntry.insert(0,listData[3])
        DOBEntry.insert(0,listData[4])
        mobileEntry.insert(0,listData[5])
        emailEntry.insert(0,listData[6])
        addhaarEntry.insert(0,listData[7])
        addressEntry.insert(0,listData[8])




def update_data():
    query='update student set name=%s,std=%s,gender=%s,dob=%s,mobileno=%s,email=%s,addhaar=%s,adress=%s,date=%s,time=%s where id=%s'
    cur.execute(query,(nameEntry.get(),stdEntry.get(),genderEntry.get(),DOBEntry.get(),mobileEntry.get(),emailEntry.get()
                        ,addhaarEntry.get(),addressEntry.get(),Date,time1,idEntry.get()))
    con.commit()
    messagebox.showinfo('Sucess',f'ID {idEntry.get()} is modified sucessfully',parent=screen_window)
    screen_window.destroy()
    show_student()


    


def show_student():
    query='select * from student'
    cur.execute(query)
    fetched_data=cur.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    cur.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'ID {content_id} deleted sucessfully')
    query='select * from student'
    cur.execute(query)
    fetched_data=cur.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def search_data():
    query='select * from student where id=%s or name=%s or std=%s or gender=%s or dob=%s or mobileno=%s'
    cur.execute(query,(idEntry.get(),nameEntry.get(),stdEntry.get(),genderEntry.get(),DOBEntry.get(),mobileEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=cur.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def add_data():
    if idEntry.get()=='' or nameEntry.get()==''or stdEntry.get()==''or genderEntry.get()=='' or DOBEntry.get()==''or mobileEntry.get()=='':
        messagebox.showerror('Error','Fill it coreectly',parent=screen_window)

    else:
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(query,(idEntry.get(),nameEntry.get(),stdEntry.get(),genderEntry.get(),DOBEntry.get(),mobileEntry.get(),emailEntry.get(),addhaarEntry.get(),addressEntry.get()
                            ,Date,time1))
            con.commit()
            result=messagebox.askyesno('Confirm','Data Added Sucessfully. Do you want to clean a form?',parent=screen_window)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                stdEntry.delete(0,END)
                genderEntry.delete(0,END)
                DOBEntry.delete(0,END)
                mobileEntry.delete(0,END)
                emailEntry.delete(0,END)
                addhaarEntry.delete(0,END)
                addressEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','ID cannot be repeated',parent=screen_window)
            return


        query='select *from student'
        cur.execute(query)
        fetched_data=cur.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            dataList=list(data)
            studentTable.insert('',END,values=dataList)


def connect_database():
    def connect():
        global cur,con
        try:

            con=pymysql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())
            cur=con.cursor()
        except:
            messagebox.showerror('Error','Invaild Details',parent=connectwindow)
            return
        try:
            query='create database pathstudents'
            cur.execute(query)
            query='use pathstudents'
            cur.execute(query)
            query='create table student(id int not null primary key, name varchar(30), std int,gender varchar(20),dob varchar(20),mobileno varchar(10),email varchar(30),addhaar varchar(35),address varchar(100), date varchar(50),time varchar(50))'
            cur.execute(query)
        except:
            query='use pathstudents'
            cur.execute(query)
        messagebox.showinfo('Sucess','DataBase Connection is Sucessfull',parent=connectwindow)
        connectwindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('470x250+730+230')
    connectwindow.title('DataBase Connection')
    connectwindow.resizable(0,0)

    hostnameLabel=Label(connectwindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel=Label(connectwindow,text='Username',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)

    userEntry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    userEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectwindow,text='Password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)

    passwordEntry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton=ttk.Button(connectwindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

def clock():
    global Date,time1
    Date=time.strftime('%d/%m/%Y')
    time1=time.strftime('%H:%M:%S')
    DataTimeLabel.config(text=f'   Date:{Date}\nTime:{time1}')
    DataTimeLabel.after(1000,clock)

count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count] #S
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)

#GUI Part

root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Student Management System')

DataTimeLabel=Label(root,text='hello',font=('times new roman',18,'bold'))
DataTimeLabel.place(x=5,y=5)
clock()


s='Student Management System' #s[count]=t when count value is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect to DaseBase',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student3.png')
logo_label=Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,command=lambda: toplevel_data('Add Student','Add',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,command=lambda:toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,command=lambda:toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Data',width=25,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Std','Gender','DOB','Mobileno','Email','Addhar','Address','Date','Time'),xscrollcommand=scrollBarX.set
                          ,yscrollcommand=scrollBarY.set)
#studentTable.pack(fill=BOTH,expand=1)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='ID')
studentTable.heading('Name',text='NAME')
studentTable.heading('Std',text='STD')
studentTable.heading('Gender',text='GENDER')
studentTable.heading('DOB',text='DOB')
studentTable.heading('Mobileno',text='MOBILE_NO')
studentTable.heading('Email',text='EMAIL')
studentTable.heading('Addhar',text='ADDHAR_NO')
studentTable.heading('Address',text='ADDRESS')
studentTable.heading('Date',text='DATE')
studentTable.heading('Time',text='TIME')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Std',width=50,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('DOB',width=120,anchor=CENTER)
studentTable.column('Mobileno',width=200,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Addhar',width=300,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Date',width=120,anchor=CENTER)
studentTable.column('Time',width=100,anchor=CENTER)

Style=ttk.Style()

Style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),background='white',fieldbackground='white')
Style.configure('Treeview.Heading',font=('arial',14,'bold'))
studentTable.config(show='headings')













root.mainloop()