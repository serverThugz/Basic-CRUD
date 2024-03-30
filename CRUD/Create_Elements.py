from tkinter import *
from tkinter import messagebox
from CRUD import Selection_Window


def create_array(sizeArray_entry, num_ofArray_entry):
    try:
        size_of_array = int(sizeArray_entry.get())
        elements_in_list = num_ofArray_entry.get().split(',')

        # Convert input elements to integers
        elements_in_list = [int(element) for element in num_ofArray_entry.get().split(',')]

        if len(elements_in_list) != size_of_array:
            messagebox.showerror("Error", "Number of elements does not match the specified size of the array.")
            return

        # Check for presence of numbers
        array = list(range(1, size_of_array + 1))
        all_present = all(num in array for num in elements_in_list)
        some_present = any(num in array for num in elements_in_list)

        if all_present:
            manipulating_array_window.destroy()
            Selection_Window.display_array_elements(elements_in_list)
        elif some_present:
            messagebox.showinfo("Result", "Some of the entered numbers are present in the array.")
        else:
            messagebox.showinfo("Result", "None of the entered numbers are present in the array.")
    except ValueError as e:
        messagebox.showinfo("Error","Please Fill Up correctly")
        messagebox.showerror("Error", str(e))

def clear():
    sizeArray_entry.delete(0, END)
    num_ofArray_entry.delete(0, END)


# This is the GUI part
manipulating_array_window = Tk()
manipulating_array_window.title("Create Read Update and Delete")
manipulating_array_window.geometry("800x600")

# This is the main Frame for interface
main_frm = Frame(manipulating_array_window, width=800, height=600, bg="black")
main_frm.place(x=0, y=0)

# This is the label for size of array
sizeArray_lbl = Label(main_frm, text="Size of Array:", font=("Poppins", 18, "bold"), fg="white", bg="black")
sizeArray_lbl.place(x=230, y=180)

# This is the label for Number of array
num_ofArray_lbl = Label(main_frm, text="Enter number  of Array:", font=("Poppins", 18, "bold"),fg="white", bg="black")
num_ofArray_lbl.place(x=120, y=240)

# This is Entry for size of Array
sizeArray_entry = Entry(main_frm, width=20, font=("Poppins", 18, "bold"), fg="white", bg="black")
sizeArray_entry.place(x=400, y=180)

# This is Entry for Number of array
num_ofArray_entry = Entry(main_frm, width=20, font=("Poppins", 18, "bold"), fg="white", bg="black")
num_ofArray_entry.place(x=400, y=240)

# This is for create button
create_btn = Button(main_frm, text="Create", font=("Poppins", 18, "bold"), fg="black",bg="orange",command=lambda: create_array(sizeArray_entry, num_ofArray_entry))
create_btn.place(x=120, y=350)

# This is for back button
clear_btn = Button(main_frm, text="Clear", font=("Poppins", 18, "bold"), fg="white", bg="black", width=5,command=clear)
clear_btn.place(x=270, y=350)

manipulating_array_window.mainloop()