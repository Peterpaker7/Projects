from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'admin69' and passwordEntry.get() == '6969':
        messagebox.showinfo('Success', 'Welcome admin69')
        tk.destroy()
        import swimming_pool_app
    else:
        messagebox.showerror('Error', 'Please Enter Correct Username And Password')

# Create the main window
tk = Tk()

# Set the geometry of the window
tk.geometry('1280x700+0+0')
tk.title('Bule Star Login')

# We can't maximize the window
tk.resizable(False, False)

# Load and resize the background image
def resize_image(image_path, width, height):
    try:
        img = Image.open(image_path)
        resized_img = img.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_img)
    except FileNotFoundError:
        messagebox.showerror('Error', f'Background image not found at: {image_path}')
        return None

bg_image_path = 'login_pic.jpg'  # Replace with the actual path to your background image
bg = resize_image(bg_image_path, 1280, 700)

# If the background image loaded successfully, display it
if bg:
    bglabel = Label(tk, image=bg)
    bglabel.place(x=0, y=0, relwidth=1, relheight=1)
    bglabel.image = bg  # Keep a reference!
else:
    # If the background image failed to load, you might want to set a default background color
    tk.config(bg='lightblue') # Example default background color

# Creating the frame for login elements
loginFrame = Frame(tk, bg='white') # Added a background color for the frame
loginFrame.place(x=400, y=150)

# Creating Label for inserting the logo image
try:
    logoimage = PhotoImage(file='logo1.png')
    logo_image = Label(loginFrame, image=logoimage, bg='white')
    logo_image.grid(row=0, column=0, columnspan=2, pady=20)
except FileNotFoundError:
    messagebox.showerror('Error', 'Logo image not found!')

# USERLOGO AND ENTRY
try:
    username_Label = PhotoImage(file='username.png')
    usernameLabel = Label(loginFrame, image=username_Label, text='Username', compound=LEFT,
                          font=('times new roman', 20, 'bold'), bg='white')
    usernameLabel.grid(row=1, column=0, pady=10, padx=20, sticky='w') # Use sticky to align text
except FileNotFoundError:
    messagebox.showerror('Error', 'Username icon not found!')
    usernameLabel = Label(loginFrame, text='Username', font=('times new roman', 20, 'bold'), bg='white')
    usernameLabel.grid(row=1, column=0, pady=10, padx=20, sticky='w')

usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5)
usernameEntry.grid(row=1, column=1, pady=10, padx=20, sticky='ew') # Use sticky to expand entry

# PASSWORD LOGO AND ENTRY
try:
    passwordImage = PhotoImage(file='padlock.png')
    passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT,
                          font=('times new roman', 20, 'bold'), bg='white')
    passwordLabel.grid(row=2, column=0, pady=10, padx=20, sticky='w')
except FileNotFoundError:
    messagebox.showerror('Error', 'Password icon not found!')
    passwordLabel = Label(loginFrame, text='Password', font=('times new roman', 20, 'bold'), bg='white')
    passwordLabel.grid(row=2, column=0, pady=10, padx=20, sticky='w')

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, show='*') # Added show='*' for password masking
passwordEntry.grid(row=2, column=1, pady=10, padx=20, sticky='ew')

# Login button
loginButton = Button(loginFrame, text='Log in', font=('times new roman', 14, 'bold'), width=15,
                      fg="white", bg='cornflowerblue', cursor='hand2', command=login)
loginButton.grid(row=3, column=0, columnspan=2, pady=20) # Center the button

# To create a window
tk.mainloop()
