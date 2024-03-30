from tkinter import *
from CRUD import Selection_Window

def insert_value(elements_in_list):
    def insert_the_value(insert_value_entry):
        value = int(insert_value_entry.get())
        elements_in_list.append(value)
        see_elements = Label(iv_main_frm, text=f"Elements: {elements_in_list}", font=("Poppins", 18, "bold"),
                             fg="white",
                             bg="black")
        see_elements.place(x=280, y=330)

    def back():
        insert_value_window.destroy()
        Selection_Window.display_array_elements(elements_in_list)

    insert_value_window = Tk()
    insert_value_window.title("Create Read Update and Delete")
    insert_value_window.geometry("800x600")
    iv_main_frm = Frame(insert_value_window, width=800, height=600, bg="black")
    iv_main_frm.place(x=0, y=0)

    # This is a Label for Insert value
    insert_value_lbl = Label(iv_main_frm, text="Insert value: ", font=("Poppins", 18, "bold"), fg="white",
                             bg="black")
    insert_value_lbl.place(x=280, y=220)

    # This is an Entry for Insert label
    insert_value_entry = Entry(iv_main_frm, width=3, font=("Poppins", 18, "bold"), fg="white", bg="black")
    insert_value_entry.place(x=443, y=220)

    # This is for search button
    insert_btn = Button(iv_main_frm, text="INSERT", font=("Poppins", 18, "bold"), fg="black", bg="orange",
                        command=lambda: insert_the_value(insert_value_entry))
    insert_btn.place(x=280, y=270)

    # This is for back button
    back_btn = Button(iv_main_frm, text="BACK", font=("Poppins", 16, "bold"), fg="white", bg="black", command=back)
    back_btn.place(x=400, y=280)

    # This is the Label for the Inputted Elements of the user

    insert_value_window.mainloop()
