from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import csv
import pandas

AMOUNT_PER_MEMBER = 200

# Declare global variables
nameEntries = []
membersEntry = None
hrsEntry = None
cashAmountEntry = None
gpayAmountEntry = None
screen_window = None

# Functionality Part for Blue Star Swimming Pool

def iexit():
    result = messagebox.askyesno('Confirm', 'Do You want to exit?')
    if result:
        root.destroy()
    else:
        pass

def save_to_csv():
    url = filedialog.asksaveasfilename(defaultextension='.csv', initialfile='bluestar_swimmingpool_data.csv')
    if url:
        indexing = swimmingTable.get_children()
        newlist = []
        for index in indexing:
            content = swimmingTable.item(index)
            datalist = content['values']
            newlist.append(datalist)
        table = pandas.DataFrame(newlist, columns=['Name', 'Members', 'Hrs', 'Amount', 'Payment Mode', 'All Names'])
        try:
            table.to_csv(url, index=False)
            messagebox.showinfo('Success', 'Data Saved to CSV Successfully')
        except Exception as e:
            messagebox.showerror('Error', f'Error saving data to CSV: {e}')

def generate_bill():
    selected_item = swimmingTable.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Please select an entry to generate a bill.')
        return

    bill_data = swimmingTable.item(selected_item, 'values')
    if not bill_data:
        messagebox.showerror('Error', 'Could not retrieve data for the bill.')
        return

    main_name = bill_data[0]
    members = int(bill_data[1])
    hrs = bill_data[2]
    amount_str = bill_data[3]  # Get the amount as a string from the table
    payment_mode = bill_data[4]
    all_member_names = bill_data[5] if len(bill_data) > 5 else "" # Retrieve all names

    bill_window = Toplevel(root)
    bill_window.title('Blue Star Swimming Pool Bill')

    bill_text = Text(bill_window, font=('courier', 12))
    bill_text.pack(padx=20, pady=20)

    bill_text.insert(END, "============= Blue Star Swimming Pool Bill ============\n")
    bill_text.insert(END, f"Date: {time.strftime('%d/%m/%Y %H:%M:%S')}\n")
    bill_text.insert(END, f"Main Member Name: {main_name}\n")
    bill_text.insert(END, f"Number of Members: {members}\n")
    if all_member_names:
        bill_text.insert(END, "Member Names: " + all_member_names + "\n")
    else:
        bill_text.insert(END, "Member Names: (Not available)\n")
    bill_text.insert(END, f"Hours Used: {hrs}\n")
    bill_text.insert(END, f"------------------------------------------------------\n")
    try:
        amount = float(amount_str)  # Convert the amount to a float
        bill_text.insert(END, f"Total Amount: ₹{amount:.2f}\n")
    except ValueError:
        bill_text.insert(END, f"Total Amount: ₹{amount_str} (Error: Could not format)\n") # Handle potential conversion error
    bill_text.insert(END, f"Payment Mode: {payment_mode}\n")
    bill_text.insert(END, "======================================================\n")
    bill_text.config(state=DISABLED) # Make it read-only

    def save_bill():
        file = filedialog.asksaveasfile(defaultextension=".txt", initialfile=f"{main_name}_bill.txt")
        if file:
            bill_content = bill_text.get("1.0", END)
            file.write(bill_content)
            file.close()
            messagebox.showinfo('Success', 'Bill saved successfully.')

    save_button = ttk.Button(bill_window, text='Save Bill', command=save_bill)
    save_button.pack(pady=10)

def export_data():
    generate_bill()

def create_member_name_fields(num_members, parent):
    global nameEntries
    for entry in nameEntries:
        entry.destroy()
    nameEntries = []
    for i in range(num_members):
        name_label = Label(parent, text=f'Member {i+1} Name:', font=('times new roman', 16))
        name_label.grid(row=5 + i, column=0, pady=5, padx=30, sticky=W)
        name_entry = Entry(parent, font=('roman', 15), width=24)
        name_entry.grid(row=5 + i, column=1, pady=5, padx=10)
        nameEntries.append(name_entry)
    add_button.grid(row=5 + num_members, columnspan=2, pady=15)

def members_changed(event):
    try:
        num_members = int(membersEntry.get())
        if num_members >= 0:
            create_member_name_fields(num_members, screen_window)
        else:
            messagebox.showerror('Error', 'Number of members cannot be negative', parent=screen_window)
            create_member_name_fields(0, screen_window) # Clear fields
            membersEntry.set('0')
    except ValueError:
        messagebox.showerror('Error', 'Invalid number of members', parent=screen_window)
        create_member_name_fields(0, screen_window) # Clear fields
        membersEntry.set('0')

def add_entry():
    global membersEntry, hrsEntry, cashAmountEntry, gpayAmountEntry, screen_window, add_button, nameEntries

    screen_window = Toplevel()
    screen_window.title('Add New Entry')
    screen_window.grab_set()
    screen_window.resizable(False, False)

    membersLabel = Label(screen_window, text='No. of Members:', font=('times new roman', 20, 'bold'))
    membersLabel.grid(row=0, column=0, pady=15, padx=30, sticky=W)
    membersEntry = Entry(screen_window, font=('roman', 15, 'bold'), width=24)
    membersEntry.grid(row=0, column=1, pady=15, padx=10)
    membersEntry.insert(0, '0') # Default to 0
    membersEntry.bind("<KeyRelease>", members_changed) # Call function when members change

    hrsLabel = Label(screen_window, text='Hours:', font=('times new roman', 20, 'bold'))
    hrsLabel.grid(row=1, column=0, pady=15, padx=30, sticky=W)
    hrsEntry = Entry(screen_window, font=('roman', 15, 'bold'), width=24)
    hrsEntry.grid(row=1, column=1, pady=15, padx=10)
    hrsEntry.insert(0, '1')

    cashLabel = Label(screen_window, text='Cash Amount Paid:', font=('times new roman', 20, 'bold'))
    cashLabel.grid(row=2, column=0, pady=15, padx=30, sticky=W)
    cashAmountEntry = Entry(screen_window, font=('roman', 15, 'bold'), width=24)
    cashAmountEntry.grid(row=2, column=1, pady=15, padx=10)
    cashAmountEntry.insert(0, '0')

    gpayLabel = Label(screen_window, text='GPay Amount Paid:', font=('times new roman', 20, 'bold'))
    gpayLabel.grid(row=3, column=0, pady=15, padx=30, sticky=W)
    gpayAmountEntry = Entry(screen_window, font=('roman', 15, 'bold'), width=24)
    gpayAmountEntry.grid(row=3, column=1, pady=15, padx=10)
    gpayAmountEntry.insert(0, '0')

    add_button = ttk.Button(screen_window, text='Add Entry', command=add_data)
    add_button.grid(row=5, columnspan=2, pady=15) # Initial placement

    create_member_name_fields(0, screen_window) # Initialize with 0 members

def add_data():
    global nameEntries, membersEntry, hrsEntry, cashAmountEntry, gpayAmountEntry, screen_window

    if not membersEntry or not hrsEntry or not cashAmountEntry or not gpayAmountEntry:
        messagebox.showerror('Error', 'Internal error: Entry widgets not initialized.')
        return

    try:
        members = int(membersEntry.get())
    except ValueError:
        messagebox.showerror('Error', 'Invalid number of members', parent=screen_window)
        return

    member_names = [entry.get() for entry in nameEntries]
    all_member_names = ", ".join(member_names) # Join names with comma

    main_member_name = member_names[0] if member_names else "" # Keep the first name as main

    try:
        hrs = int(hrsEntry.get())
        if hrs < 0:
            messagebox.showerror('Error', 'Hours cannot be negative', parent=screen_window)
            return
    except ValueError:
        messagebox.showerror('Error', 'Invalid hours', parent=screen_window)
        return

    try:
        cash_amount = float(cashAmountEntry.get())
        if cash_amount < 0:
            messagebox.showerror('Error', 'Cash amount cannot be negative', parent=screen_window)
            return
    except ValueError:
        messagebox.showerror('Error', 'Invalid cash amount', parent=screen_window)
        return

    try:
        gpay_amount = float(gpayAmountEntry.get())
        if gpay_amount < 0:
            messagebox.showerror('Error', 'GPay amount cannot be negative', parent=screen_window)
            return
    except ValueError:
        messagebox.showerror('Error', 'Invalid GPay amount', parent=screen_window)
        return

    total_amount = AMOUNT_PER_MEMBER * members
    payment_mode_str = ""
    if cash_amount > 0:
        payment_mode_str += f"Cash: {cash_amount}"
    if gpay_amount > 0:
        if payment_mode_str:
            payment_mode_str += ", "
        payment_mode_str += f"GPay: {gpay_amount}"

    swimmingTable.insert('', END, values=(main_member_name, members, hrs, total_amount, payment_mode_str, all_member_names)) # Store all names

    messagebox.showinfo('Success', 'Entry Added Successfully', parent=screen_window)
    screen_window.destroy()

def show_data():
    try:
        with open('bluestar_swimmingpool.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip the header row
            swimmingTable.delete(*swimmingTable.get_children()) # Clear existing data
            for row in reader:
                swimmingTable.insert('', END, values=row)
    except FileNotFoundError:
        messagebox.showinfo('Info', 'No existing data file found.')
    except Exception as e:
        messagebox.showerror('Error', f'Error reading data file: {e}')

def connect_database():
    messagebox.showinfo('Info', 'This application saves data to a local CSV file and does not require a database connection.')

def clock():
    global Date, time1
    Date = time.strftime('%d/%m/%Y')
    time1 = time.strftime('%H:%M:%S')
    DataTimeLabel.config(text=f'   Date:{Date}\nTime:{time1}')
    DataTimeLabel.after(1000, clock)

count = 0
text = ''
def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)

# GUI Part for Blue Star Swimming Pool

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+0+0')
root.resizable(0, 0)
root.title('Blue Star Swimming Pool')
root.state('zoomed') # Maximize the window

DataTimeLabel = Label(root, text='hello', font=('times new roman', 18, 'bold'))
DataTimeLabel.place(x=5, y=5)
clock()

s = 'Blue Star Swimming Pool'
sliderLabel = Label(root, font=('arial', 28, 'italic bold'), width=30)
sliderLabel.place(x=200, y=0)
slider()

connectButton = ttk.Button(root, text='No Database Needed', state=DISABLED) # Changed text and disabled
connectButton.place(x=980, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

try:
    logo_image = PhotoImage(file='logo1.png') # Changed logo filename
    logo_label = Label(leftFrame, image=logo_image)
    logo_label.grid(row=0, column=0, pady=20)
except FileNotFoundError:
    messagebox.showerror('Error', 'Logo image "logo1.png" not found!')
except TclError:
    messagebox.showerror('Error', 'Could not open or read image file "logo1.png"!')

addEntryButton = ttk.Button(leftFrame, text='Add New Entry', width=25, command=add_entry)
addEntryButton.grid(row=1, column=0, pady=20)

showDataButton = ttk.Button(leftFrame, text='Show Data', width=25, command=show_data) # Modified text
showDataButton.grid(row=2, column=0, pady=20)

exportDataButton = ttk.Button(leftFrame, text='Generate Bill', width=25, command=export_data) # Changed button text
exportDataButton.grid(row=3, column=0, pady=20)

exportCSVButton = ttk.Button(leftFrame, text='Export to CSV', width=25, command=save_to_csv)
exportCSVButton.grid(row=4, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text='Exit', width=25, command=iexit)
exitButton.grid(row=5, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

swimmingTable = ttk.Treeview(rightFrame, columns=('Name', 'Members', 'Hrs', 'Amount', 'Payment Mode', 'All Names'), xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=swimmingTable.xview)
scrollBarY.config(command=swimmingTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

swimmingTable.pack(fill=BOTH, expand=1)

swimmingTable.heading('Name', text='NAME')
swimmingTable.heading('Members', text='MEMBERS')
swimmingTable.heading('Hrs', text='HRS')
swimmingTable.heading('Amount', text='AMOUNT')
swimmingTable.heading('Payment Mode', text='PAYMENT Mode')
swimmingTable.heading('All Names', text='') # Keep this column hidden

swimmingTable.column('Name', width=300, anchor=CENTER)
swimmingTable.column('Members', width=100, anchor=CENTER)
swimmingTable.column('Hrs', width=100, anchor=CENTER)
swimmingTable.column('Amount', width=150, anchor=CENTER)
swimmingTable.column('Payment Mode', width=250, anchor=CENTER) # Increased width
swimmingTable.column('All Names', width=0, stretch=NO) # Hide the 'All Names' column

Style = ttk.Style()
Style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), background='white', fieldbackground='white')
Style.configure('Treeview.Heading', font=('arial', 14, 'bold'))
swimmingTable.config(show='headings')

# Load initial data from CSV if it exists
show_data()

root.mainloop()
