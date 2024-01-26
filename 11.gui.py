import tkinter
from tkinter import *
root = tkinter.Tk()
root.title("Registration Form")
root.geometry("500x500")

def submit_handle():
    # get input entry
    name_fetch = name_input.get()
    checkbutton_value1 = checkbutton_var1.get()
    checkbutton_value2 = checkbutton_var2.get()
    selected_value = radio_var.get()
    drop_selected_value = dropdown_var.get()
    print(name_fetch,checkbutton_value1,checkbutton_value2,selected_value,drop_selected_value)

formFrame = Frame(root)
formFrame.pack(pady= 50)

# label
heading = Label(formFrame, text='Register',font=('Arial'))
heading.pack()

#label
name = Label(
 formFrame,
 text="Full Name",
 font=("Bookman old style", 16),
)
name.pack(padx=10,pady=5)


# input 
name_input = Entry(formFrame)
name_input.pack(padx=10,pady=5)

#checkbutton 
# variable to store value
checkbutton_var1 = IntVar()
checkbutton1 = Checkbutton(root, text="Check me", variable=checkbutton_var1,onvalue=1)
checkbutton1.pack(pady=10)

checkbutton_var2 = IntVar()
checkbutton2 = Checkbutton(root, text="Check me", variable=checkbutton_var2,onvalue=2)
checkbutton2.pack(pady=10)

# radio button
radio_var = StringVar()
radio_button1 = Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio_button2 = Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio_button3 = Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3")
radio_button1.pack(pady=5)
radio_button2.pack(pady=5)
radio_button3.pack(pady=5)


#drop down
dropdown_var = StringVar()

# Set default value for the dropdown
dropdown_var.set("Option 1")

# Create a dropdown (OptionMenu) and associate it with the variable
options = ["Option 1", "Option 2", "Option 3"]
dropdown = OptionMenu(root, variable = dropdown_var, *options)
dropdown.pack(pady=10)

# button
button = Button(root, text="Get Checkbutton Value", command=submit_handle)
button.pack(pady=10)


root.mainloop()
