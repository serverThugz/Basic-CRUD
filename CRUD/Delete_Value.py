from tkinter import *
from CRUD import Selection_Window


def delete_the_value(elements_in_list):
    def back():
        delete_value_window.destroy()
        Selection_Window.display_array_elements(elements_in_list)
    def delete_the_value(delete_value_entry):
        value = int(delete_value_entry.get())
        for element in elements_in_list:
            if value == element:
                del elements_in_list[value - 1]

        see_elements = Label(del_main_frm, text=f"Elements: {elements_in_list}", font=("Poppins", 18, "bold"),
                             fg="white",
                             bg="black")
        see_elements.place(x=280, y=330)
        back_btn = Button(del_main_frm, text="Back", font=("Poppins", 18, "bold"), fg="white", bg="black", width=5,
                          command=back)
        back_btn.place(x=280, y=380)

    delete_value_window = Tk()
    delete_value_window.title("Create Read Update and Delete")
    delete_value_window.geometry("800x600")
    del_main_frm = Frame(delete_value_window, width=800, height=600, bg="black")
    del_main_frm.place(x=0, y=0)

    # This is a Label for Insert value
    delete_value_lbl = Label(del_main_frm, text="Delete value: ", font=("Poppins", 18, "bold"), fg="white",
                             bg="black")
    delete_value_lbl.place(x=280, y=220)

    # This is an Entry for Insert label
    delete_value_entry = Entry(del_main_frm, width=3, font=("Poppins", 18, "bold"), fg="white", bg="black")
    delete_value_entry.place(x=443, y=220)

    # This is for search button
    delete_btn = Button(del_main_frm, text="DELETE", font=("Poppins", 18, "bold"), fg="black", bg="orange",
                        command=lambda: delete_the_value(delete_value_entry))
    delete_btn.place(x=280, y=270)
    delete_value_window.mainloop()