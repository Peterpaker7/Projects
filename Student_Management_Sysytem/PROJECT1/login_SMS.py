#for GUI

from tkinter import * 

from tkinter import messagebox
#for import the jpg image to the python,for that we had installed lib "pip install pillow"

from PIL import ImageTk,Image 

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='admin69' and passwordEntry.get()=='6969':
        messagebox.showinfo('Success','Welcome admin69')
        tk.destroy()
        import selection_SMS
        
    else:
        messagebox.showerror('Error','Please Enter Correct Username And Password')


#create the main window 
tk=Tk()


#Set the geomentry of the window
#here we used geomentry function for the hegiht and width of the window (give a value in str format)

tk.geometry('1280x700+0+0')
#here why we are using 0+0 here they mentioned that 0 in y axis and 0 in x axis this will stable your window at one place

tk.title('Login System Of Student Mangement System')


#we can't maximize the window
tk.resizable(False,False)

#Load the background image
#if we use .jpg image we need to use ImageTk 
bg=ImageTk.PhotoImage(file='BG(1).jpg') #explaination given by me ; taking the image into the venv(enviroment)

#if we need to diplay the window with that picture we need to use label here,
bglabel=Label(tk,image=bg)
#fix the image properly
bglabel.place(x=0,y=0)

#crating the frame (after adding the bg(backgroundimage)we need to add some elements like login button logo like that that we are able to add in the frame thats why we are creating a frame now)
#frame is which like a continer which we can kept the labels 

loginFrame=Frame(tk)

#place the loginframe

loginFrame.place(x=400,y=150)              

#creating Label for inserting the logo image
#if we use .png image we can use PhotoImage only 
logoimage=PhotoImage(file='PATH.png')

# create a label and add image

logo_image=Label(loginFrame,image=logoimage,bg='white')

# to place the image into the frame
logo_image.grid(row=0,column=0,columnspan=2)
#we have two types in insert the image into frame one is place and grid method here,
#we had used grid method here we need to use rows and columns the rows and columns should be declered as 0
#because in this frame we are adding the first image so that we declered 0

#USERLOGO AND ENTRY

#taken the photo into the venv
username_Label=PhotoImage(file='username.png')
#creates a label for the usename
usernameLabel=Label(loginFrame,image=username_Label,text='Username',compound=LEFT  #COMPOUND is used for seeing the text left or right (displaying the text)
                    , font=('times new roman',20,'bold'))#font for the text and size
#place the logo
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

#for creating the entry and placing on windows
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)#use fg="<color>"for the text
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

#PASSWORD LOGO AND ENTRY
passwordImage=PhotoImage(file='padlock.png')
#creates a label for the usename
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT  #COMPOUND is used for seeing the text left or right (displaying the text)
                    , font=('times new roman',20,'bold'))#font for the text and size
#place the logo
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

#for creating the entry and placing on windows
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)#use fg="<color>"for the text
passwordEntry.grid(row=2,column=1,pady=10,padx=20)


'''#taken the photo into the venv
password_label=PhotoImage(file='padlock.png')

#creates a label for the usename
passwordlabel=Label(loginFrame,image=password_label,text='Password',compound=LEFT
                    ,font=('times new roman',20,'bold'))
#place the logo
passwordlabel.grid(row=2,column=2,pady=10,padx=20)
#for creating the entry and placing on windows
passwordentry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
passwordentry.grid(row=2,column=1,pady=10,padx=20)'''

#login button

loginButton=Button(loginFrame,text='Log in',font=('times new roman',14,'bold'),width=15
                   ,fg="white",bg='cornflowerblue',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)






#to create a window(why we are using mainloop?,to see the window,if we didnt use the mainloop the code will execute but we cant see the window)
tk.mainloop()


